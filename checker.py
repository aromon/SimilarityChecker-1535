class checkcheck:
    def __init__(self,first_word,second_word):
        self.first_word = first_word
        self.second_word = second_word

    def len_check(self):
        if len(self.first_word) < len(self.second_word):
            self.first_word, self.second_word = self.second_word, self.first_word
        first_len = len(self.first_word)
        second_len = len(self.second_word)
        print(f'{self.first_word},{self.second_word} : {first_len},{second_len}')
        score = (1 - ((first_len - second_len) / second_len)) * 60
        return score

