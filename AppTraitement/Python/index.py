
from ParsingJson import ParsingJson



# Initialisation Class ParsingJson
parsingJson = ParsingJson("Python/FileTest2.json")
parsingJson.getJsonToArray()
#print(parsingJson.jsonArray)


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
