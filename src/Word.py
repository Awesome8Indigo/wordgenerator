import json


class Word:
    def __init__(self, word, spelling, meaning, wordtype):
        with open("dictionary.json", "rt", encoding='utf-8') as jsonfile:
            jsonlst = json.load(jsonfile)
            worddict = jsonlst.get("Words", {})
        self.word = word
        self.spelling = spelling
        self.meaning = meaning
        if wordtype in worddict:
            self.wordtype = wordtype

    def search(self):
        with open("dictionary.json", 'r', encoding='utf-8') as dict_file:
            dictionary = json.load(dict_file)  # load instead of read+loads for simplicity
            worddict = dictionary.get("Words", {})
        if self.wordtype not in worddict:
            return False
        # Check if self.word exists in Worddict
        if self.word in worddict[self.wordtype]:
            return True
        else: return False
    def add(self):
        # Open the JSON file once and store data in jsonlst
        with open("dictionary.json", "rt", encoding='utf-8') as jsonfile:
            jsonlst = json.load(jsonfile)

        worddict = jsonlst.get("Words", {})
        typedict = worddict[self.wordtype]

        # Only add if the word does not already exist
        if not self.search():
            newword = {
                "spelling": self.spelling,  # Assuming self.spelling is a list
                "meaning": self.meaning,
            }
            typedict[self.word] = newword  # Add the new word with the word as key
            jsonlst["Words"] = worddict  # Update the words dict

            # Write the updated list back to the dictionary.json file
            with open("dictionary.json", "wt", encoding='utf-8') as jsonfile:
                json.dump(jsonlst, jsonfile, indent=4)
    def append(self, key, value):
        with open("dictionary.json", "rt", encoding='utf-8') as jsonfile:
            jsonlst = json.load(jsonfile)
            worddict = jsonlst.get("Words", {})

        if key not in ["word", "spelling", "meaning", "wordtype"]:
            return

        if not self.search():
            return

        typedict = worddict[self.wordtype]

        if key == "word":
            typedict[value] = typedict.pop(self.word)
            self.word = value
        elif key == "wordtype":
            if value not in worddict:
                a = input("do you want to add new wordtype? Y/N ")
                if a == "Y" or a == "y":
                    worddict[value] = {}
                elif a == "N" or a == "n":
                    return
                else:
                    print("not a valid input")
                    return
            del typedict[self.word]
            self.wordtype = value
            typedict = worddict[self.wordtype]
            typedict[self.word] = {
                "spelling": self.spelling, "meaning": self.meaning
            }
        else:
            typedict[self.word][key] = value

        with open("dictionary.json", "wt", encoding='utf-8') as jsonfile:
            json.dump(jsonlst, jsonfile, indent=4)
    def delete(self):
        with open("dictionary.json", "rt", encoding='utf-8') as jsonfile:
            jsonlst = json.load(jsonfile)
            worddict = jsonlst.get("Words", {})
            typedict = worddict[self.wordtype]
        del typedict[self.word]
        with open("dictionary.json", "wt", encoding='utf-8') as jsonfile:
            json.dump(jsonlst, jsonfile, indent=4)

    def getDef(self):
        return self.meaning
    def getSpelling(self):
        return self.spelling
    def getWordType(self):
        return self.wordtype