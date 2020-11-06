from Python.ParsingJson import ParsingJson
from Python.ParsingSpacy import ParsingSpacy
from Python.TraitementJsonFile import TraitementJsonFile


# Génération des JsonFile
# traitementJsonFile = TraitementJsonFile()
#
# traitementJsonFile.openFile("AppTraitement/JsonBigFile/us_election20_tweet_pr.json", 1000)
# traitementJsonFile.concatenateJson()
# traitementJsonFile.writeFile()



# Initialisation Class ParsingJson
parsingJson = ParsingJson("JsonFiles/JsonFile1.json")
parsingJson.getJsonToArray()

parsingSpacy = ParsingSpacy()


# Séparation Trump / Biden Tweet
parsingJson.findTrumpOrBiden()

trumpArray = parsingJson.getTrumpArray()
bidenArray = parsingJson.getBidenArray()



# Suppressions symbols
trumpWithoutSymbols = parsingJson.extractionSymbols(trumpArray)
bidenWithoutSymbols = parsingJson.extractionSymbols(bidenArray)



# Extraction StopWord
trumpWithoutStopWords = parsingSpacy.extractionStopWords(trumpWithoutSymbols)
bidenWithoutStopWords = parsingSpacy.extractionStopWords(bidenWithoutSymbols)



# Count occurence mots
trumpCountOccurence = parsingJson.countOccurenceWord(trumpWithoutStopWords)
bidenCountOccurence = parsingJson.countOccurenceWord(bidenWithoutStopWords)



# Trié les array par ordre décroissant
trumpSortedArray = parsingJson.arraySorted(trumpCountOccurence)
bidenSortedArray = parsingJson.arraySorted(bidenCountOccurence)



# Récupération des 25 premier elements
trumpBestElems = parsingJson.getFirstElemsArray(trumpSortedArray, 25)
bidenBestElems = parsingJson.getFirstElemsArray(bidenSortedArray, 25)



# Création file result
parsingJson.createResultFile("Trump", trumpBestElems)
parsingJson.createResultFile("Biden", bidenBestElems)



# Test For InterfaceWeb



# Affichage








#
