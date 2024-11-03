import json


class noun:
    def __init__(self, word, spelling, meaning, gender):
        self.word = word
        self.spelling = spelling
        self.meaning = meaning
        self.gender = gender

    def search(self):
        with open("dictionary.json", 'r', encoding='utf-8') as dict_file:
            dictionary = json.load(dict_file)  # load instead of read+loads for simplicity
            noundict = dictionary.get("nouns", {})

        # Check if self.word exists in noundict
        if self.word in noundict:
            return True
        return False

    def add(self):
        # Open the JSON file once and store data in jsonlst
        with open("dictionary.json", "rt", encoding='utf-8') as jsonfile:
            jsonlst = json.load(jsonfile)

        noundict = jsonlst.get("nouns", {})

        # Only add if the word does not already exist
        if not self.search():
            newnoun = {
                "spelling": self.spelling,  # Assuming self.spelling is a list
                "meaning": self.meaning,
                "gender": self.gender  # Assuming self.gender is defined
            }
            noundict[self.word] = newnoun  # Add the new noun with the word as key
            jsonlst["nouns"] = noundict  # Update the nouns dict

            # Write the updated list back to the dictionary.json file
            with open("dictionary.json", "wt", encoding='utf-8') as jsonfile:
                json.dump(jsonlst, jsonfile, indent=4)

    def append(self):
        pass

    def getGender(self):
        return self.gender
    def getDef(self):
        return self.meaning
    def getSpelling(self):
        return self.spelling
    def setGender(self, gender):
        if(self.gender):
            self.gender = gender
    def setDef(self, meaning):
        if(self.meaning):
            self.meaning = meaning
    def setSpelling(self, spelling):
        if(self.spelling):
            self.spelling = spelling