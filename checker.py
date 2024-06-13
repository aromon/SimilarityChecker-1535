class checkcheck:
    def __init__(self, first_word, second_word):
        self.first_word = first_word
        self.second_word = second_word

    def len_check(self):
        if len(self.first_word) < len(self.second_word):
            self.first_word, self.second_word = self.second_word, self.first_word
        first_len = len(self.first_word)
        second_len = len(self.second_word)
        score = (1 - ((first_len - second_len) / second_len)) * 60
        return score

    def alpha_check(self):
        first_list = []
        second_list = []
        score = 0
        for i in self.first_word:
            if i not in first_list:
                first_list.append(i)
        for i in self.second_word:
            if i not in second_list:
                second_list.append(i)
        total_list = second_list.copy()
        for i in first_list:
            if i in second_list:
                score += 1
            if i not in second_list:
                total_list.append(i)
        return (score / len(total_list)) * 40
