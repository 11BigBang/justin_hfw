import sys, pygame
from settings import Settings
from decks import Deck1

class HFWords:
    """Class to manage game assets and behavior."""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Justin's HFW")
        self.deck1 = Deck1(self)

    def run_cards(self):
        """Start the main loops for the cards."""
        while True:
            self.check_events()
            self.update_screen()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.deck1.next_word()
                elif event.key == pygame.K_LEFT:
                    self.deck1.prev_word()

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.deck1.blit_card()

        pygame.display.flip()

if __name__ == '__main__':
    jhfw = HFWords()
    jhfw.run_cards()