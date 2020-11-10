import json
import re

class TraitementJsonFile:
    jsonArray = []
    jsonConcatenate = ""

# Constructor
    def __init__(self):
        self.jsonArray = []
        self.jsonConcatenate = '{"jsonArray": [\n'

# Open File And Add To List
    def openFile(self, file, elem):
        with open(file, "r") as filin:
            ligne = filin.readline()
            stop = 0
            while ligne != "":
                if(self.supprUselessLigne(ligne)):
                    self.jsonArray.append(ligne)
                ligne = filin.readline()
                stop += 1
                if(stop == elem):
                    break

# Check if trump or biden in tweet
    def supprUselessLigne(self, val):
        patternBiden = r"@?(joe)?(\s)?biden | @?biden(\s)?(joe)?"
        patternTrump = r"@?(donald)?(\s)?trump | @?trump(\s)?(donald)?"
        if re.search(patternTrump, val, re.IGNORECASE | re.MULTILINE):
            return True
        if re.search(patternBiden, val, re.IGNORECASE | re.MULTILINE):
            return True
        return False


# Json Concatenante
    def concatenateJson(self):
        for elem in self.jsonArray:
            if(self.jsonArray[-1] == elem):
                self.jsonConcatenate = self.jsonConcatenate + elem
            else:
                self.jsonConcatenate = self.jsonConcatenate + elem + ','
        self.jsonConcatenate = self.jsonConcatenate + ']}'


# Write File jsonArrayList
    def writeFile(self):
        with open("AppTraitement/JsonFiles/JsonFile1.json", "w") as filout:
            for json in self.jsonConcatenate:
                filout.write(json)
