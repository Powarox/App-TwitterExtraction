from ParsingJson import ParsingJson
from TraitementJsonFile import TraitementJsonFile


# Génération des JsonFile
traitementJsonFile = TraitementJsonFile()

traitementJsonFile.openFile("AppTraitement/JsonBigFile/us_election20_tweet_pr.json", 1000)
traitementJsonFile.concatenateJson()
traitementJsonFile.writeFile()



# Initialisation Class ParsingJson
parsingJson = ParsingJson("AppTraitement/JsonFiles/JsonFile1.json")
parsingJson.getJsonToArray()



# Séparation Trump / Biden Tweet
parsingJson.findTrumpOrBiden()

trumpArray = parsingJson.getTrumpArray()
bidenArray = parsingJson.getBidenArray()



# Suppressions mots inutile
banWord = parsingJson.regexpBanWord()

trumpImportantWords = parsingJson.extractionImportantWord(banWord, trumpArray)
bidenImportantWords = parsingJson.extractionImportantWord(banWord, bidenArray)



# Count occurence mots
trumpCountOccurence = parsingJson.countOccurenceWord(trumpImportantWords)
bidenCountOccurence = parsingJson.countOccurenceWord(bidenImportantWords)



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
