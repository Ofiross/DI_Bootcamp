# Daily Challenge
import translators as ts


french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]


def Convert(lst):
    """Converting a list of words from french into english"""
    translated_words = []
    for i in lst:
        translated_words.append(ts.google(i))
        result_zipped = zip(lst, translated_words)
        result_dict = dict(result_zipped)
    print(f"\n{'-' *80}\nThe translation from French to English is:\n{result_dict}\n{'-' *80}\n")


Convert(french_words)
