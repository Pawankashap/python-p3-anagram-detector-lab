# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def _sort_word(self, word):
        return "".join(sorted(word.lower()))

    def match(self, word_list):
        matches = []
        sorted_word = self._sort_word(self.word)

        for word in word_list:
            if self._sort_word(word) == sorted_word and word.lower() != self.word:
                matches.append(word)

        return matches