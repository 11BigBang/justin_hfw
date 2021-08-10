from settings import Settings

class Deck1:
    def __init__(self, app):
        self.screen = app.screen
        self.settings = Settings()
        self.deck_index = 0
        self.deck_words = ['a', 'away', 'find', 'and', 'in', 'down', 'for', 'I', 'where', 'funny',
                           'big', 'yellow', 'not', 'the', 'we', 'me', 'see', 'is', 'sit', 'my',
                           'very', 'said', 'make', 'here', 'do', 'up', 'run', 'look', 'help', 'come',
                           'two', 'red', 'little', 'go', 'can', 'your', 'to', 'play', 'jump', 'get',
                           'blue', 'you', 'three', 'one', 'it']

    def blitme(self):
        """Display card on screen."""
        self.screen.blit(self.settings.font_1.render(self.word, False,(255, 0, 0)),(300, 150))
