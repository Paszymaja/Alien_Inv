import sys
import pygame

from bullet import Bullet
from enemy import Enemy



def check_events(settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(screen_settings, screen, ship, screen_y, background, bullets, enemy):
    screen.fill(screen_settings.bg_color)
    rel_y = screen_y % background.height
    screen.blit(background.image, (0, rel_y - background.height))
    if rel_y < screen_settings.screen_height:
        screen.blit(background.image, (0, rel_y))
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    enemy_start(screen_settings, screen, enemy)
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


def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(settings, screen, ship, bullets):
    if len(bullets) < settings.bullet_allow:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)


def enemy_start(settings, screen, enemies):
    if len(enemies) < 3:
        new_enemy = Enemy(screen, settings)
        enemies.add(new_enemy)


def update_enemies(enemies):
    enemies.update()
    for enemy in enemies.copy():
        if enemy.rect.bottom == 720:
            enemies.remove(enemy)

