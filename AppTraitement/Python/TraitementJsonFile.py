import json
import re

class TraitementJsonFile:
    jsonArray = []

# Constructor
    def __init__(self):
        self.jsonArray = []


# Open File And Add To List
    def openFile(self, file, elem, stop = 0):
        with open(file, "r") as filin:
            ligne = filin.readline()
            while ligne != "" and stop != elem:
                if(self.supprUselessLigne(ligne)):
                    self.jsonArray.append(ligne)
                ligne = filin.readline()
                stop += 1


# Check if trump or biden in tweet
    def supprUselessLigne(self, val):
        patternBiden = r"@?(joe)?(\s)?biden | @?biden(\s)?(joe)?"
        patternTrump = r"@?(donald)?(\s)?trump | @?trump(\s)?(donald)?"
        if re.search(patternTrump, val, re.IGNORECASE | re.MULTILINE):
            return True
        if re.search(patternBiden, val, re.IGNORECASE | re.MULTILINE):
            return True
        return False


# Write File jsonArrayList
    def writeFile(self):
        with open("../AppTraitement/JsonFiles/JsonFile1.json", "w") as filout:
            result = json.dumps(self.jsonArray)
            filout.write(result)
