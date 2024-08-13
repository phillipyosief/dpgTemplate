import json


class LanguageHandler:
    def __init__(self, language_file):
        self.language_file = language_file
        self.translations = self.load_language_file()

    def load_language_file(self):
        with open(self.language_file, 'r', encoding='utf-8') as file:
            return json.load(file)

    def get_translation(self, key):
        return self.translations.get(key, key)
