import json     # json_decode
import re       # preg_match
from pathlib import Path

class ParsingJson:
    jsonFile = ""
    jsonArray = {}
    globalTrumpCountOccu = {}
    globalBidenCountOccu = {}


# Constructor
    def __init__(self):
        self.jsonFile = {}
        self.jsonArray = {}
        self.globalTrumpCountOccu = {}
        self.globalBidenCountOccu = {}


# Getter / Setter
    def setJsonFile(self, file):
        self.jsonFile = file

    def getGlobalTrumpCountOccu(self):
        return self.globalTrumpCountOccu

    def getGlobalBidenCountOccu(self):
        return self.globalBidenCountOccu



# ------------------ Traitement File Entrée ------------------
    # Récupère le json et le transforme en tableau
    def transformJsonToArray(self, i = 0):
        with open(self.jsonFile) as f:
            for value in json.load(f):
                self.jsonArray[i] = json.loads(value)
                i += 1



# ------------------ Séparation Trump / Biden ------------------

    # Find si tweet talk about T or B
    def findTrumpOrBiden(self, trumpTweetArray = {}, bidenTweetArray = {}):
        patternBiden = r"@?(joe)?(\s)?biden | @?biden(\s)?(joe)?"
        patternTrump = r"@?(donald)?(\s)?trump | @?trump(\s)?(donald)?"
        for key, value in self.jsonArray.items():
            if re.search(patternTrump, value['text'], re.IGNORECASE | re.MULTILINE):
                trumpTweetArray[key] = value
            if re.search(patternBiden, value['text'], re.IGNORECASE | re.MULTILINE):
                bidenTweetArray[key] = value
        return trumpTweetArray, bidenTweetArray


# ------------------ Suppression Symbols ------------------

    # Extract important word
    def extractionSymbols(self, array):
        arrayWithoutSymbols = {}
        pattern = r"@|&|'|\"|\||\(|\)|<|>|#|\.|\,|\/|\?|\!|\;|\:|\\|\n||-|_|[1234567890]*|(\s[abcdefghijklmnopqrstuvwxyz]\s)"
        for key, value in array.items():
            arrayWithoutSymbols[key] = re.sub(pattern, "", value['text'])
        return arrayWithoutSymbols



# ------------------ Count Occurence Word ------------------

    # Explode String to Char Array
    def traitementWord(self, string):
        return string.lower().split(' ')

    # Count number of occurence word
    def countOccurenceWord(self, array):
        arrayCountOccurence = {}
        for key, value in array.items():
            for word in self.traitementWord(value):
                if word in arrayCountOccurence:
                    arrayCountOccurence[word] += 1
                else:
                    arrayCountOccurence[word] = 1
        return arrayCountOccurence

    # Global count number of occurence word
    def globalCountOccuWord(self, name, array):
        for key, value in array.items():
            if name == "Trump":
                if key in self.globalTrumpCountOccu:
                    self.globalTrumpCountOccu[key] = self.globalTrumpCountOccu[key] + value
                else:
                    self.globalTrumpCountOccu[key] = value
            else:
                if key in self.globalBidenCountOccu:
                    self.globalBidenCountOccu[key] = self.globalBidenCountOccu[key] + value
                else:
                    self.globalBidenCountOccu[key] = value



# ------------------ Array Sorted ------------------

    def arraySorted(self, array):
        arraySorted = {}
        for key, value in sorted(array.items(), key = lambda x: x[1], reverse = True):
            arraySorted[key] = value
        return arraySorted



# ------------------ First Elems Array ------------------

    def getFirstElemsArray(self, array, stopValue, stop = 0):
        arrayFirstElem = {}
        for key, value in array.items():
            if not key in self.spacyStopWords():
                arrayFirstElem[key] = value
                stop +=1
                if stop == stopValue:
                    break
        return arrayFirstElem



# ------------------ Traitement Tmp Result Files ------------------

    # Création Fichier json contenant les résultat
    def createTmpResultFile(self, name, data, numberFile):
        path = Path('AppTraitement/Tmp/' + name + '/Result' + str(numberFile) + '.json')
        with open(path, "w") as filout:
            filout.write(json.dumps(data))



# ------------------ Traitement File Sortie ------------------

    # Création Fichier json contenant les résultat
    def createFinalResultFile(self, name, data):
        path = Path('AppTraitement/Result/' + name + '/AResult.json')
        with open(path, "w") as filout:
            filout.write(json.dumps(data))



# ------------------ Utilitaire ------------------

    def spacyStopWords(self):
        spacyStopWords = (
            "unless", "itself", "yet", "formerly", "against", "wherever", "at", "anyway", "get", "than", "cannot", "his", "either", "see", "hundred", "ours", "used", "hence", "six", "beyond", "its", "although", "while", "wherein", "really", "such", "these", "everything", "serious", "'s", "he", "over", "whereupon", "full", "between", "several", "afterwards", "always", "whether", "here", "very", "eleven", "four", "with", "anything", "still", "any", "alone", "even", "eight", "themselves", "everywhere", "thereby", "nine", "among", "only", "almost", "my", "ca", "amongst", "becoming", "around", "and", "hereby", "otherwise", "have", "moreover", "being", "next", "why", "therein", "front", "just", "or", "due", "together", "anyhow", "about", "under", "sometimes", "'m", "\u2019re", "herself", "where", "seems", "'ve", "part", "\u2019m", "already", "to", "all", "perhaps", "anywhere", "are", "must", "yourselves", "\u2018re", "further", "been", "many", "in", "none", "myself", "least", "along", "what", "via", "should", "last", "once", "beforehand", "two", "until", "doing", "an", "the", "himself", "nobody", "nor", "might", "n\u2019t", "am", "never", "n't", "someone", "herein", "few", "who", "up", "without", "sixty", "each", "most", "move", "sometime", "so", "will", "re", "however", "keep", "every", "their", "her", "nevertheless", "i", "therefore", "something", "your", "nothing", "yours", "throughout", "too", "into", "seemed", "go", "we", "then", "meanwhile", "thereupon", "\u2019ll", "\u2019ve", "no", "for", "same", "whence", "whereafter", "less", "whose", "'d", "before", "can", "forty", "hereafter", "some", "not", "onto", "also", "those", "ever", "from", "after", "empty", "call", "within", "former", "may", "somewhere", "one", "of", "towards", "beside", "namely", "regarding", "rt", "toward", "enough", "own", "another", "amount", "because", "often", "twelve", "whereby", "\u2019d", "give", "five", "\u2018s", "hereupon", "which", "across", "anyone", "whoever", "please", "n\u2018t", "other", "there", "made", "'ll", "besides", "them", "more", "could", "upon", "say", "much", "whither", "though", "do", "thence", "whenever", "us", "during", "mostly", "\u2018ll", "per", "name", "thus", "\u2018ve", "now", "quite", "back", "nowhere", "thereafter", "was", "seem", "him", "ourselves", "make", "how", "out", "bottom", "side", "latterly", "mine", "is", "hers", "\u2018d", "a", "again", "top", "noone", "whereas", "seeming", "would", "this", "below", "rather", "somehow", "take", "show", "whom", "since", "except", "ten", "become", "whatever", "whole", "done", "did", "using", "but", "various", "they", "becomes", "latter", "'re", "were", "twenty", "\u2019s", "our", "everyone", "if", "above", "neither", "it", "has", "when", "fifty", "off", "she", "thru", "yourself", "me", "first", "through", "three", "you", "put", "\u2018m", "that", "well", "behind", "by", "elsewhere", "indeed", "else", "does", "be", "down", "became", "on", "had", "both", "as", "fifteen", "third", "others", "rt", "de", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "l", "m", "n "," o "," p "," q ", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "", " ")
        return spacyStopWords
