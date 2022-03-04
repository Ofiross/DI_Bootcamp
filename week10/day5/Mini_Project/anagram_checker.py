
class AnagramChecker:
    def __init__(self, filename):
        self.filename = filename

        try:
            with open(self.filename, 'r') as f:
                self.text = f.read().replace("\n", ',')
                self.text = self.text.split(",")

        except IOError:
            raise IOError(f"{self.filename} not found")

    def is_valid_word(self, word):
        """"Method to check if the user word is in the list"""
        for i in self.text:
            if word == i:
                print('Good, word is in our database.')
                return word

        print(
            'Cannot find word in data base, but we can check the word against another.')

    def is_anagram(self, w1, w2):
        if(sorted(w1) == sorted(w2)):
            print("The words are anagrams.")
            return True
        else:
            print("The words aren't anagrams.")
            return False

    def check_more_words(self, word_check):
        same_letters_words = []
        print('You can also create these words using these letters: ')
        for word in self.text:
            if (set(word) == set(word_check)) and len(word) == len(word_check):
                same_letters_words.append(word)
        print(same_letters_words)
