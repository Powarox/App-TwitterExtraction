traitementJsonFile.openFile(Path("AppTraitement/JsonBigFile/us_election20_tweet_pr.json"), 100)
traitementJsonFile.writeFile()



# -------------------------------------------------------------------------

# Open File And Add To List
    def openFile(self, file, elem, stop = 0):
        with open(file, "r") as filin:
            ligne = filin.readline()
            while ligne != "" and stop != elem:
                if(self.supprUselessLigne(ligne)):
                    self.jsonArray.append(ligne)
                ligne = filin.readline()
                stop += 1


# Write File jsonArrayList
    def writeFile(self):
        with open(Path("AppTraitement/JsonFiles/JsonFile1.json"), "w") as filout:
            result = json.dumps(self.jsonArray)
            filout.write(result)



# -------------------- Spacy -------------------- #

start = time.time()
# Instanciation Class ParsingSpacy
parsingSpacy = ParsingSpacy()
end = time.time()
val = end - start
print("Time SpaIns : " + str(val))

start = time.time()
# Extraction StopWord
trumpWithoutStopWords = parsingSpacy.extractionStopWords(trumpWithoutSymbols)
bidenWithoutStopWords = parsingSpacy.extractionStopWords(bidenWithoutSymbols)
end = time.time()
val = end - start
print("Time StopWo : " + str(val))

start = time.time()
# Count occurence mots Spacy
trumpCountOccurence = parsingJson.countOccurenceWord(trumpWithoutStopWords)
bidenCountOccurence = parsingJson.countOccurenceWord(bidenWithoutStopWords)
end = time.time()
val = end - start
print("Time OccuSp : " + str(val))

# -------------------- Spacy -------------------- #



    def arrayBanWords(self):
        arrayBanWords = (
            "but", "or", "and", "therefore", "or", "neither", "because", "he", "him", "they", "she", "they", "we", "you", "your", "your", "my", "mine", "mine", "yours", "yours", "all", "yes", "no", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "l", "m", "n "," o "," p "," q ", "r", "s", "t", "u", "v", "w", "x", "y", "z", "the", "the", "the", "our", "then", "to", "none", "also", "other", "before", "with", "have", "good", "because", "this", "that", "these", "those", "each", "this", "like", "how", "in", "of", "of", "out", "from", "two", "should", "must", "therefore", "back", "right", "start", "she", "they", "in", "still", "test", "is", "and", "had", "done", "times", "do", "force", "up", "off", "here", "he", "they", "I just", "the", "the", "the", "their", "there", "my", "now", "but", "mine", "minus", "word", "same", "neither", "named", "our", "we", "new", "or", "where", "by", "because", "word", "not", "people", "may", "little", "part", "most", "for", "why", "when", "what", "which", "which", "which", "which", "which", "his", "without", "his", "only", "if", "his", "his", "are", "under", "be subject", "on", "your", "while", "so", "such", "your", "your", "all", "all", "too much", "very", "you", "value", "way", "see", "go", "seen", "that", "were", "state", "were", "been", "be", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "with", "at", "by", "in", "of", "in", "of", "a", "your", "best", "between", "entered", "from", "then", "not", "not", "from", "same", "or", "name", "only", "accepted", "having", "your", "your", "my", "mine", "mine", "yours", "that", "what", "who", "how", "little", "can", "worse", "then", "not", "each", "each", "each", "his", "his", "au", "aux", "se", "sur", "those", "this", "that", "also", "for", "small", "large", "medium", "large", "top", "bottom", "middle", "right", "left", "center", "said", "be", "their", "more", "less", "less", "es", "is", "are", "his", "will", "am", "have", "come", "http", "https", "", " ", "as", "it", "rt")
        return arrayBanWords
