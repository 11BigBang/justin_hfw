from pygame.font import SysFont

class Settings:
    """Class to store all settings for the app."""

    def __init__(self):
        # Screen settings
        self.screen_width = 900
        self.screen_height = 680
        self.bg_color = (250, 250, 250)

        # Fonts
        self.font_1 = SysFont('impact', 100)
        self.font_2 = SysFont('Arial', 32)