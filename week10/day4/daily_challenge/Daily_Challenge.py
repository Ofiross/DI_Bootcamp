from collections import defaultdict
import re


class Text:

    def __init__(self, text):
        self.text = text

    def frequency(self):
        str = self.text.split()
        str2 = []

        for i in str:
            if i not in str2:
                str2.append(i)

        for i in range(0, len(str2)):
            if str.count(str2[i]) > 1:
                print(
                    f"Frequency of', {str2[i]}, 'is :', {str.count(str2[i])}")
            else:
                return None

    def most_common(self):
        li = list(self.text.split(" "))
        my_temp = defaultdict(int)

        for sub in li:
            for word in sub.split():
                my_temp[word] += 1

        result = max(my_temp, key=my_temp.get)

        print(f"The most common word is:\n{result}")

    def unique_words(self):
        unique = set(self.text.split(' '))
        return unique

    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as f:
            data = f.read().replace("\n", " ")
            return data


class TextModification(Text):
    def __init__(self, text):
        super().__init__(text)

    def remove_punc(self):
        res = re.sub(r'[^\w\s]', '', self.text)
        return res

    def no_stop_words(self):
        stops = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until",
                 "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

        for word in self.text:
            if word in stops:
                self.text = self.text.replace(word, "")

    def special_char(self):
        spe_char = '''!()-[]{};:'"\,<>./?@#$%^&*_~♦♣♠•◘○☺☻♥'''

        for char in self.text:
            if char in spe_char:
                self.text = self.text.replace(char, "")


text = Text(
    'apple mango apple orange orange orange orange orange guava mango apple mango')
print(text.unique_words())

text_from_file = Text.from_file('the_stranger.txt')
