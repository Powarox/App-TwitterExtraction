from pathlib import Path
from Python.ParsingJson import ParsingJson
from Python.TraitementJsonFile import TraitementJsonFile
# from Python.GenerateImgResult import GenerateImgResult
import time

start = time.time()
# Génération des JsonFile
traitementJsonFile = TraitementJsonFile()
countFiles = traitementJsonFile.openFractionFiles(
    Path("AppTraitement/JsonBigFile/us_election20_tweet_pr.json"), 33000)
end = time.time()
val = end - start
print("Time OpenWrit : " + str(val))



# Instanciation Class ParsingJson
parsingJson = ParsingJson()

# Loop Traitement on number file
for count in range(countFiles):
    start = time.time()

    # Init Class ParsingJson
    parsingJson.setJsonFile(Path("AppTraitement/JsonFiles/JsonFile" + str(count) +".json"))

    # Transform Json to Array
    parsingJson.transformJsonToArray()

    # Séparation Trump / Biden Tweet
    trumpArray, bidenArray = parsingJson.findTrumpOrBiden()

    # Suppressions symbols
    trumpWithoutSymbols = parsingJson.extractionSymbols(trumpArray)
    bidenWithoutSymbols = parsingJson.extractionSymbols(bidenArray)

    # Count occurence mots
    trumpCountOccu = parsingJson.countOccurenceWord(trumpWithoutSymbols)
    bidenCountOccu = parsingJson.countOccurenceWord(bidenWithoutSymbols)

    # Fusion with globalCountOccu
    parsingJson.globalCountOccuWord("Trump", trumpCountOccu)
    parsingJson.globalCountOccuWord("Biden", bidenCountOccu)

    # CLear Local Var
    trumpArray.clear()
    bidenArray.clear()

    trumpWithoutSymbols.clear()
    bidenWithoutSymbols.clear()

    trumpCountOccu.clear()
    bidenCountOccu.clear()

    end = time.time()
    val = end - start
    print("Time BouclFor : " + str(val))



# Récupération des array avec tous les mots et leurs occurences
globalTrumpCountOccu = parsingJson.getGlobalTrumpCountOccu()
globalBidenCountOccu = parsingJson.getGlobalBidenCountOccu()

# Trié les array par ordre décroissant
globalTrumpSortedArray = parsingJson.arraySorted(globalTrumpCountOccu)
globalBidenSortedArray = parsingJson.arraySorted(globalBidenCountOccu)

# Récupération des premier elements
globalTrumpBestElems = parsingJson.getFirstElemsArray(globalTrumpSortedArray, 50)
globalBidenBestElems = parsingJson.getFirstElemsArray(globalBidenSortedArray, 50)

# Création file result
parsingJson.createFinalResultFile("Trump", globalTrumpBestElems)
parsingJson.createFinalResultFile("Biden", globalBidenBestElems)



# # Création des Img grâce aux stats
# generateTrump = GenerateImgResult(trumpBestElems, "Trump/")
# generateBiden = GenerateImgResult(bidenBestElems, "Biden/")
#
# generateTrump.execute()
# generateBiden.execute()
