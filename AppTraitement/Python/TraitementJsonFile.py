import json
import re
from pathlib import Path

class TraitementJsonFile:
    jsonArray = []

# Constructor
    def __init__(self):
        self.jsonArray = []


# Open File And Add To List
    def openFractionFiles(self, file, elem, stop = 0, countFiles = 0):
        with open(file, "r") as filin:
            ligne = filin.readline()
            while ligne != "":
                if(self.supprUselessLigne(ligne)):
                    if stop == elem:
                        self.writeFractionFiles(countFiles)
                        self.jsonArray.clear()
                        countFiles += 1
                        stop = 0
                    else:
                        self.jsonArray.append(ligne)
                        stop += 1
                ligne = filin.readline()
                if(countFiles == 3):
                    break
        return countFiles


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
    def writeFractionFiles(self, countFiles):
        with open(Path("AppTraitement/JsonFiles/JsonFile" + str(countFiles) + ".json"), "w") as filout:
            result = json.dumps(self.jsonArray)
            filout.write(result)
