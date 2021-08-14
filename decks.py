from settings import Settings

class Deck1:
    def __init__(self, app):
        self.screen = app.screen
        self.settings = Settings()
        self.deck_index = 0
        self.words = ['a', 'away', 'find', 'and', 'in', 'down', 'for', 'I', 'where', 'funny',
                      'big', 'yellow', 'not', 'the', 'we', 'me', 'see', 'is', 'sit', 'my',
                      'very', 'said', 'make', 'here', 'do', 'up', 'run', 'look', 'help', 'come',
                      'two', 'red', 'little', 'go', 'can', 'your', 'to', 'play', 'jump', 'get',
                      'blue', 'you', 'three', 'one', 'it']
        self.deck_len = len(self.words)
        self.cur_word = self.words[self.deck_index]

    def next_word(self):
        if self.deck_index >= self.deck_len - 1:
            self.deck_index = 0
        else:
            self.deck_index += 1
        self.cur_word = self.words[self.deck_index]

    def prev_word(self):
        if self.deck_index <= 0:
            self.deck_index = self.deck_len - 1
        else:
            self.deck_index -= 1
        self.cur_word = self.words[self.deck_index]

    def blit_card(self):
        """Display card on screen."""
        self.screen.blit(self.settings.font_1.render(self.cur_word, False,(255, 0, 0)),(300, 150))
