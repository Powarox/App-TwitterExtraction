import json     # json_decode
import re       # preg_match

class ParsingJson:
    jsonFile = ""
    jsonArray = {}
    bidenTweetArray = {}
    trumpTweetArray = {}

# Constructor
    def __init__(self, f):
        self.jsonFile = f
        self.jsonArray = {}
        self.bidenTweetArray = {}
        self.trumpTweetArray = {}



# ------------------ Traitement File Entrée ------------------
    # Récupère le json et le transforme en tableau
    def getJsonToArray(self):
        with open(self.jsonFile) as f:
            jsonString = json.load(f)
        for keyArray, valueArray in jsonString.items():
            i = 0
            for value in valueArray:
                self.jsonArray[i] = value
                i += 1



# ------------------ Séparation Trump / Biden ------------------

    # Find si tweet talk about T or B
    def findTrumpOrBiden(self):
        patternBiden = r"@?(joe)?(\s)?biden | @?biden(\s)?(joe)?"
        patternTrump = r"@?(donald)?(\s)?trump | @?trump(\s)?(donald)?"
        for key, value in self.jsonArray.items():
            if re.search(patternTrump, value['text'], re.IGNORECASE | re.MULTILINE):
                self.trumpTweetArray[key] = value
            if re.search(patternBiden, value['text'], re.IGNORECASE | re.MULTILINE):
                self.bidenTweetArray[key] = value

    # Return array with Trump message
    def getTrumpArray(self):
        return self.trumpTweetArray

    # Return array with Biden message
    def getBidenArray(self):
        return self.bidenTweetArray



# ------------------ Traitement File Sortie ------------------

    # Fichier json contenant les résultat
    def createResultFile(self, name, data):
        with open('Result/' + name + '.json', "w") as filout:
            dataJson = json.dumps(data)
            filout.write(dataJson)

    # Transform file json pour la rendre correct
    def encodeJsonFile(self):
        x = 0

    # Récupération de chaque json independament
    def jsonIndepElem(self):
        x = 0



# ------------------ Extraction Mots Important ------------------

    # Preparation pattern
    def regexpBanWord(self, result = {}, i = 0, j = 0):
        array = self.arrayBanWord()
        for value in array:
            result[i] = r"\s(" + value + ")\s"
            i += 1
            j = i
        result[j] = r"(rt)\s"
        return result

    # Extract important word
    def extractionImportantWord(self, banWord, array):
        arrayWithoutBanWord = {}
        pattern = r"@|&|'|\"|\||\(|\)|<|>|#|\.|\,|\/|\?|\!|\;|\:|\\"
        for key, value in array.items():
            arrayTransition = re.sub(pattern, "", value['text'])

            arrayWithoutBanWord[key] = arrayTransition

            # arrayWithoutBanWord[key] = re.sub(banWord, "", arrayTransition, re.MULTILINE | re.IGNORECASE)
        return arrayWithoutBanWord

    # Array Ban Word
    def arrayBanWord(self):
        banWord = [
            "but", "or", "and", "therefore", "or", "neither", "because",
            "I", "he", "him", "they", "she", "they", "we", "you",
            "your", "your", "my", "mine", "mine", "yours", "yours",
            "all", "yes", "no",
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "l", "m", "n "," o "," p "," q ",
            "r", "s", "t", "u", "v", "w", "x", "y", "z",
            "the", "the", "the", "our",
            "then", "to", "none", "also", "other", "before", "with", "have", "good", "because", "this",
            "that", "these", "those", "each", "this", "like", "how", "in", "of", "of",
            "out", "from", "two", "should", "must", "therefore", "back", "right", "start", "she",
            "they", "in", "still", "test", "is", "and", "had", "done", "times", "do",
            "force", "up", "off", "here", "he", "they", "I just", "the", "the", "the", "their", "there",
            "my", "now", "but", "mine", "minus", "word", "same", "neither", "named",
            "our", "we", "new", "or", "where", "by", "because", "word", "not", "people",
            "may", "little", "part", "most", "for", "why", "when", "what", "which", "which",
            "which", "which", "which", "his", "without", "his", "only", "if", "his", "his",
            "are", "under", "be subject", "on", "your", "while", "so", "such", "your", "your",
            "all", "all", "too much", "very", "you", "value", "way", "see", "go",
            "seen", "that", "were", "state", "were", "been", "be",
            "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
            "with", "at", "by", "in", "of", "in", "of", "a", "your", "best", "between",
            "entered", "from", "then", "not", "not", "from", "same",
            "or", "name", "only", "accepted", "having",
            "your", "your", "my", "mine", "mine", "yours",
            "that", "what", "who", "how", "little", "can", "worse", "then", "not",
            "each", "each", "each",
            "his", "his", "au", "aux", "se", "sur", "those", "this", "that",
            "also", "for", "small", "large", "medium", "large", "top", "bottom", "middle", "right",
            "left", "center", "said", "be", "their", "more", "less", "less",
            "es", "is", "are", "his", "will", "am", "have", "come",
            "http", "https", "", " "
        ]
        return banWord


# ------------------ Count Occurence Word ------------------

    # Explode String to Char Array
    def traitementWord(self, string):
        lowerString = string.lower()
        arrayWord = lowerString.split(' ')
        return arrayWord

    # Count number of occurence word
    def countOccurenceWord(self, array):
        arrayCountOccurence = {"word" : 1}
        for key, value in array.items():
            arrayWord = self.traitementWord(value)
            for word in arrayWord:
                if word in arrayCountOccurence:
                    arrayCountOccurence[word] += 1
                else:
                    arrayCountOccurence[word] = 1
        return arrayCountOccurence



# ------------------ Count Occurence Word ------------------

    def arraySorted(self, array):
        arraySorted = {}
        for key, value in sorted(array.items(), key = lambda x: x[1], reverse = True):
            arraySorted[key] = value
        return arraySorted



# ------------------ Count Occurence Word ------------------

    def getFirstElemsArray(self, array, stopValue):
        arrayFirstElem = {}
        stop = 0
        for key, value in array.items():
            arrayFirstElem[key] = value
            stop +=1
            if stop == stopValue:
                break
        return arrayFirstElem



# ------------------ Autre ------------------

    # Suppression des prépositions et des mots pas important
    def traitementRegExp(self):
        x = 0







#
