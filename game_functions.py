import sys
import pygame

from time import sleep
from bullet import Bullet
from enemy import Enemy

globlast = pygame.time.get_ticks()  # Zmienna globalna ktora przechowuje czas last


def check_events(settings, screen, ship, bullets, stats, play_button, enemies):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y, enemies, bullets)


def update_screen(screen_settings, screen, ship, screen_y, background, bullets, enemy, play_button, stats):
    screen.fill(screen_settings.bg_color)
    rel_y = screen_y % background.height
    screen.blit(background.image, (0, rel_y - background.height))
    if rel_y < screen_settings.screen_height:
        screen.blit(background.image, (0, rel_y))
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    enemy_start(screen_settings, screen, enemy)

    if not stats.game_active:  # przycisk startu
        play_button.draw_button()

    enemy.draw(screen)
    pygame.display.update()


def check_keydown_events(event, settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def update_bullets(bullets, enemies):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    pygame.sprite.groupcollide(bullets, enemies, True, True)


def fire_bullet(settings, screen, ship, bullets):
    if len(bullets) < settings.bullet_allow:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)


def enemy_start(settings, screen, enemies):
    global globlast
    now = pygame.time.get_ticks()
    if now - globlast >= 900:
        if len(enemies) < 5:
            new_enemy = Enemy(screen, settings)
            enemies.add(new_enemy)
            globlast = now


def update_enemies(enemies, ship, settings, stats, screen, bullets):
    enemies.update()
    enemy_bottom(settings, stats, screen, ship, enemies, bullets)
    for enemy in enemies.copy():
        if enemy.rect.bottom == 720:
            enemies.remove(enemy)
    if pygame.sprite.spritecollideany(ship, enemies):
        ship_hit(settings, stats, screen, ship, bullets, enemies)


def ship_hit(settings, stats, screen, ship, bullets, enemies):
    if stats.ship_left > 0:
        stats.ship_left -= 1

        enemies.empty()
        bullets.empty()

        enemy_start(settings, screen, enemies)
        ship.center_ship()

        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def enemy_bottom(settings, stats, screen, ship, enemies, bullets):
    screen_rect = screen.get_rect()
    for enemy in enemies.sprites():
        if enemy.rect.bottom >= screen_rect.bottom:
            ship_hit(settings, stats, screen, ship, bullets, enemies)
            break


def check_play_button(stats, play_button, mouse_x, mouse_y, enemies, bullets):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        pygame.mouse.set_visible(False)
        stats.game_active = True
        stats.reset_stats()

        enemies.empty()
        bullets.empty()
