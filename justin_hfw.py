import sys, pygame
from settings import Settings
from decks import Card

class HFWords:
    """Class to manage game assets and behavior."""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Justin's HFW")
        self.dog_card = Card(self, 'dog')

    def home(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.settings.font_1.render("Justin's", False,(255, 0, 0)),(300, 150))
        self.screen.blit(self.settings.font_2.render('High Frequency Words', False, (255, 0, 0)), (270, 300))

        pygame.draw.rect(self.screen, (255, 0, 0), (400, 500, 120, 60))

    def run_cards(self):
        """Start the main loops for the cards."""
        while True:
            self.check_events()
            self.update_screen()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.dog_card.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    jhfw = HFWords()
    jhfw.run_cards()