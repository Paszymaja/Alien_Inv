class Settings:
    def __init__(self):
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (230, 230, 230)
        self.bg_image = 'Sprites/background.png'
        self.bg_speed = 0.45

        # ustawienia statku
        self.ship_speed = 2.5
        self.ship_limit = 0

        # ustawienia pocisku
        self.bullet_speed_factor = 3
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (250, 250, 0)
        self.bullet_allow = 10
