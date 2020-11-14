from Python.ParsingJson import ParsingJson
# from Python.ParsingSpacy import ParsingSpacy
from Python.TraitementJsonFile import TraitementJsonFile
import time


start = time.time()
# Génération des JsonFile
traitementJsonFile = TraitementJsonFile()
traitementJsonFile.openFile("AppTraitement/JsonBigFile/us_election20_tweet_pr.json", 50000)
traitementJsonFile.writeFile()
end = time.time()
val = end - start
print("Time OpeWri : " + str(val))


# Memory error donc
# diviser fichier jsonBigFile en 10 ?
# effectuer traitement sur chaque fichier et garder les 200 best word ?
# fusionner les resultat ?


start = time.time()
# Instanciation Class ParsingJson
parsingJson = ParsingJson("AppTraitement/JsonFiles/JsonFile1.json")
parsingJson.getJsonToArray()
end = time.time()
val = end - start
print("Time loadJs : " + str(val))


start = time.time()
# Séparation Trump / Biden Tweet        -->         Traitement ? 2 filesJson sortie ?
parsingJson.findTrumpOrBiden()
trumpArray = parsingJson.getTrumpArray()
bidenArray = parsingJson.getBidenArray()
end = time.time()
val = end - start
print("Time SepToB : " + str(val))


start = time.time()
# Suppressions symbols
trumpWithoutSymbols = parsingJson.extractionSymbols(trumpArray)
bidenWithoutSymbols = parsingJson.extractionSymbols(bidenArray)
end = time.time()
val = end - start
print("Time Symbol : " + str(val))


start = time.time()
# Count occurence mots
trumpCountOccurence = parsingJson.countOccurenceWord(trumpWithoutSymbols)
bidenCountOccurence = parsingJson.countOccurenceWord(bidenWithoutSymbols)
end = time.time()
val = end - start
print("Time OccurW : " + str(val))


start = time.time()
# Trié les array par ordre décroissant
trumpSortedArray = parsingJson.arraySorted(trumpCountOccurence)
bidenSortedArray = parsingJson.arraySorted(bidenCountOccurence)
end = time.time()
val = end - start
print("Time Sorted : " + str(val))


start = time.time()
# Récupération des 25 premier elements
trumpBestElems = parsingJson.getFirstElemsArray(trumpSortedArray, 100)
bidenBestElems = parsingJson.getFirstElemsArray(bidenSortedArray, 500)
end = time.time()
val = end - start
print("Time First  : " + str(val))


start = time.time()
# Création file result
parsingJson.createResultFile("Trump", trumpBestElems)
parsingJson.createResultFile("Biden", bidenBestElems)
end = time.time()
val = end - start
print("Time Result : " + str(val))


# Test For InterfaceWeb

# # -------------------- Spacy -------------------- #
#
# start = time.time()
# # Instanciation Class ParsingSpacy
# parsingSpacy = ParsingSpacy()
# end = time.time()
# val = end - start
# print("Time SpaIns : " + str(val))
#
# start = time.time()
# # Extraction StopWord
# trumpWithoutStopWords = parsingSpacy.extractionStopWords(trumpWithoutSymbols)
# bidenWithoutStopWords = parsingSpacy.extractionStopWords(bidenWithoutSymbols)
# end = time.time()
# val = end - start
# print("Time StopWo : " + str(val))
#
# start = time.time()
# # Count occurence mots Spacy
# trumpCountOccurence = parsingJson.countOccurenceWord(trumpWithoutStopWords)
# bidenCountOccurence = parsingJson.countOccurenceWord(bidenWithoutStopWords)
# end = time.time()
# val = end - start
# print("Time OccuSp : " + str(val))
#
# # -------------------- Spacy -------------------- #
