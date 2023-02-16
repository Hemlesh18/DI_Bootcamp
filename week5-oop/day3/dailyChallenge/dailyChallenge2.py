# translator
class Translator:
    def __init__(self, french_words):
        self.french_words = french_words

    def get_translation(self):
        translator_dict = {}
        for word in self.french_words:
            if word == "Bonjour":
                translation = "Hello"
            elif word == "Au revoir":
                translation = "Goodbye"
            elif word == "Bienvenue":
                translation = "Welcome"
            else:
                translation = "See you soon"
            translator_dict[word] = translation
        return translator_dict

# create the Translator object 
french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
translator = Translator(french_words)

# get the translation
translation_dict = translator.get_translation()
print(translation_dict)