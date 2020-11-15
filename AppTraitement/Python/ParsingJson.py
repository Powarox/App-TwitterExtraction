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
    def getJsonToArray(self, i = 0):
        with open(self.jsonFile) as f:
            for value in json.load(f):
                self.jsonArray[i] = json.loads(value)
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
        arrayCountOccurence = {"word" : 1}
        for key, value in array.items():
            for word in self.traitementWord(value):
                if word in arrayCountOccurence:
                    arrayCountOccurence[word] += 1
                else:
                    arrayCountOccurence[word] = 1
        return arrayCountOccurence



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



# ------------------ Traitement File Sortie ------------------

    # Fichier json contenant les résultat
    def createResultFile(self, name, data):
        folder = 'AppTraitement/Result/' + name + '/'
        with open(folder + name + '.json', "w") as filout:
            filout.write(json.dumps(data))



# ------------------ Utilitaire ------------------

    def spacyStopWords(self):
        spacyStopWords = (
            "unless", "itself", "yet", "formerly", "against", "wherever", "at", "anyway", "get", "than", "cannot", "his", "either", "see", "hundred", "ours", "used", "hence", "six", "beyond", "its", "although", "while", "wherein", "really", "such", "these", "everything", "serious", "'s", "he", "over", "whereupon", "full", "between", "several", "afterwards", "always", "whether", "here", "very", "eleven", "four", "with", "anything", "still", "any", "alone", "even", "eight", "themselves", "everywhere", "thereby", "nine", "among", "only", "almost", "my", "ca", "amongst", "becoming", "around", "and", "hereby", "otherwise", "have", "moreover", "being", "next", "why", "therein", "front", "just", "or", "due", "together", "anyhow", "about", "under", "sometimes", "'m", "\u2019re", "herself", "where", "seems", "'ve", "part", "\u2019m", "already", "to", "all", "perhaps", "anywhere", "are", "must", "yourselves", "\u2018re", "further", "been", "many", "in", "none", "myself", "least", "along", "what", "via", "should", "last", "once", "beforehand", "two", "until", "doing", "an", "the", "himself", "nobody", "nor", "might", "n\u2019t", "am", "never", "n't", "someone", "herein", "few", "who", "up", "without", "sixty", "each", "most", "move", "sometime", "so", "will", "re", "however", "keep", "every", "their", "her", "nevertheless", "i", "therefore", "something", "your", "nothing", "yours", "throughout", "too", "into", "seemed", "go", "we", "then", "meanwhile", "thereupon", "\u2019ll", "\u2019ve", "no", "for", "same", "whence", "whereafter", "less", "whose", "'d", "before", "can", "forty", "hereafter", "some", "not", "onto", "also", "those", "ever", "from", "after", "empty", "call", "within", "former", "may", "somewhere", "one", "of", "towards", "beside", "namely", "regarding", "rt", "toward", "enough", "own", "another", "amount", "because", "often", "twelve", "whereby", "\u2019d", "give", "five", "\u2018s", "hereupon", "which", "across", "anyone", "whoever", "please", "n\u2018t", "other", "there", "made", "'ll", "besides", "them", "more", "could", "upon", "say", "much", "whither", "though", "do", "thence", "whenever", "us", "during", "mostly", "\u2018ll", "per", "name", "thus", "\u2018ve", "now", "quite", "back", "nowhere", "thereafter", "was", "seem", "him", "ourselves", "make", "how", "out", "bottom", "side", "latterly", "mine", "is", "hers", "\u2018d", "a", "again", "top", "noone", "whereas", "seeming", "would", "this", "below", "rather", "somehow", "take", "show", "whom", "since", "except", "ten", "become", "whatever", "whole", "done", "did", "using", "but", "various", "they", "becomes", "latter", "'re", "were", "twenty", "\u2019s", "our", "everyone", "if", "above", "neither", "it", "has", "when", "fifty", "off", "she", "thru", "yourself", "me", "first", "through", "three", "you", "put", "\u2018m", "that", "well", "behind", "by", "elsewhere", "indeed", "else", "does", "be", "down", "became", "on", "had", "both", "as", "fifteen", "third", "others", "rt", "de", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "l", "m", "n "," o "," p "," q ", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "", " ")
        return spacyStopWords

    def arrayBanWords(self):
        arrayBanWords = (
            "but", "or", "and", "therefore", "or", "neither", "because", "he", "him", "they", "she", "they", "we", "you", "your", "your", "my", "mine", "mine", "yours", "yours", "all", "yes", "no", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "l", "m", "n "," o "," p "," q ", "r", "s", "t", "u", "v", "w", "x", "y", "z", "the", "the", "the", "our", "then", "to", "none", "also", "other", "before", "with", "have", "good", "because", "this", "that", "these", "those", "each", "this", "like", "how", "in", "of", "of", "out", "from", "two", "should", "must", "therefore", "back", "right", "start", "she", "they", "in", "still", "test", "is", "and", "had", "done", "times", "do", "force", "up", "off", "here", "he", "they", "I just", "the", "the", "the", "their", "there", "my", "now", "but", "mine", "minus", "word", "same", "neither", "named", "our", "we", "new", "or", "where", "by", "because", "word", "not", "people", "may", "little", "part", "most", "for", "why", "when", "what", "which", "which", "which", "which", "which", "his", "without", "his", "only", "if", "his", "his", "are", "under", "be subject", "on", "your", "while", "so", "such", "your", "your", "all", "all", "too much", "very", "you", "value", "way", "see", "go", "seen", "that", "were", "state", "were", "been", "be", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "with", "at", "by", "in", "of", "in", "of", "a", "your", "best", "between", "entered", "from", "then", "not", "not", "from", "same", "or", "name", "only", "accepted", "having", "your", "your", "my", "mine", "mine", "yours", "that", "what", "who", "how", "little", "can", "worse", "then", "not", "each", "each", "each", "his", "his", "au", "aux", "se", "sur", "those", "this", "that", "also", "for", "small", "large", "medium", "large", "top", "bottom", "middle", "right", "left", "center", "said", "be", "their", "more", "less", "less", "es", "is", "are", "his", "will", "am", "have", "come", "http", "https", "", " ", "as", "it", "rt")
        return arrayBanWords




#
