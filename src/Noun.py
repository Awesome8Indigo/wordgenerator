import json
from Word import Word
class Noun(Word):
    def __init__(self, word, spelling, meaning, gender, isplural):
        self.word = word
        self.spelling = spelling
        self.meaning = meaning
        self.gender = gender
        self.isplural = isplural

