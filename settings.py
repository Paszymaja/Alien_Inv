class Settings:
    def __init__(self):
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (230, 230, 230)
        self.bg_image = 'background.png'
        self.bg_speed = 0.45

        # Ship settings
        self.ship_speed = 2.5

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
