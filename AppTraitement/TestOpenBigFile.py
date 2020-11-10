import json     # json_decode
import re       # preg_match

class Test:
    bidenTweetArray = {}
    trumpTweetArray = {}

    # Constructor
    def __init__(self):
        self.bidenTweetArray = {}
        self.trumpTweetArray = {}

    # Open File And Add To List
    def execute(self, file):
        with open(file, "r") as filin:
            ligne = filin.readline()
            while ligne != "":
                self.supprUselessLigne()
                ligne = filin.readline()


# ------------------ Parsing ------------------
    # Suppression tweet without trump or biden
    def supprUselessLigne(self, val):
        patternBiden = r"@?(joe)?(\s)?biden | @?biden(\s)?(joe)?"
        patternTrump = r"@?(donald)?(\s)?trump | @?trump(\s)?(donald)?"

        if re.search(patternTrump, val, re.IGNORECASE | re.MULTILINE):
            return True
        if re.search(patternBiden, val, re.IGNORECASE | re.MULTILINE):
            return True
        return False


# ------------------ Getter / Setter ------------------
    # Return array with Trump message
    def getTrumpArray(self):
        return self.trumpTweetArray

    # Return array with Biden message
    def getBidenArray(self):
        return self.bidenTweetArray
