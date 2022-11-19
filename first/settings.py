class Settings:

    def __init__(self):
        '''Статические настройки игры'''
        # Настройки экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # Настройки снарядов
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 10

        # Настройки пришельцев
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        # Настройки корабля
        self.ship_limit = 3

        # Ускорение игры
        self.speed_up_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 4
        self.bullet_speed = 3
        self.alien_speed = 1
        self.fleet_direction = 1
        self.alien_points = 1

    def increase_speed(self):
        self.ship_speed *= self.speed_up_scale
        self.bullet_speed *= self.speed_up_scale
        self.alien_speed *= self.speed_up_scale

