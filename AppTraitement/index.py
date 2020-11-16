from pathlib import Path
from Python.ParsingJson import ParsingJson
# from Python.ParsingSpacy import ParsingSpacy
from Python.TraitementJsonFile import TraitementJsonFile
# from Python.GenerateImgResult import GenerateImgResult


# Génération des JsonFile
traitementJsonFile = TraitementJsonFile()
countFiles = traitementJsonFile.openFractionFiles(
    Path("AppTraitement/JsonBigFile/us_election20_tweet_pr.json"), 10000)


# Instanciation Class ParsingJson
parsingJson = ParsingJson()


for count in range(countFiles):
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

    # Trié les array par ordre décroissant
    trumpSortedArray = parsingJson.arraySorted(trumpCountOccu)
    bidenSortedArray = parsingJson.arraySorted(bidenCountOccu)

    # Récupération des premier elements
    trumpBestElems = parsingJson.getFirstElemsArray(trumpSortedArray, 50)
    bidenBestElems = parsingJson.getFirstElemsArray(bidenSortedArray, 50)

    # Tmp Result Files
    parsingJson.createTmpResultFile("Trump", trumpBestElems, count)
    parsingJson.createTmpResultFile("Biden", bidenBestElems, count)

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

    trumpSortedArray.clear()
    bidenSortedArray.clear()

    trumpBestElems.clear()
    bidenBestElems.clear()




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
