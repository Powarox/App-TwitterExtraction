from pathlib import Path
from Python.ParsingJson import ParsingJson
from Python.TraitementJsonFile import TraitementJsonFile
from Python.GenerateImgResult import GenerateImgResult



# Génération des JsonFile
traitementJsonFile = TraitementJsonFile()
countFiles = traitementJsonFile.openFractionFiles(
    Path("../AppTraitement/JsonBigFile/us_election20_tweet_pr.json"), 1000000)


# Instanciation Class ParsingJson
parsingJson = ParsingJson()


# Loop Traitement on number file
for count in range(countFiles):
    # Init Class ParsingJson
    parsingJson.setJsonFile(Path("../AppTraitement/JsonFiles/JsonFile" + str(count) +".json"))

    # Transform Json to Array
    parsingJson.transformJsonToArray()

    # Séparation Trump / Biden Tweet
    trumpArray, bidenArray = parsingJson.findTrumpOrBiden()

    # Suppression var
    parsingJson.clearVar()

    # Suppressions symbols
    trumpArray = parsingJson.extractionSymbols(trumpArray)
    bidenArray = parsingJson.extractionSymbols(bidenArray)

    # Count occurence mots
    trumpArray = parsingJson.countOccurenceWord(trumpArray)
    bidenArray = parsingJson.countOccurenceWord(bidenArray)

    # Fusion with globalCountOccu
    parsingJson.globalCountOccuWord("Trump", trumpArray)
    parsingJson.globalCountOccuWord("Biden", bidenArray)



# Récupération des array avec tous les mots et leurs occurences
globalTrumpCountOccu = parsingJson.getGlobalTrumpCountOccu()
globalBidenCountOccu = parsingJson.getGlobalBidenCountOccu()

# Trié les array par ordre décroissant
globalTrumpSortedArray = parsingJson.arraySorted(globalTrumpCountOccu)
globalBidenSortedArray = parsingJson.arraySorted(globalBidenCountOccu)

# Récupération des premier elements
globalTrumpBestElems = parsingJson.getFirstElemsArray(globalTrumpSortedArray, 1000)
globalBidenBestElems = parsingJson.getFirstElemsArray(globalBidenSortedArray, 1000)

# Création file result
parsingJson.createFinalResultFile("Trump", globalTrumpBestElems)
parsingJson.createFinalResultFile("Biden", globalBidenBestElems)

# Création des Img grâce aux stats
generateTrump = GenerateImgResult(trumpBestElems, "Trump/")
generateBiden = GenerateImgResult(bidenBestElems, "Biden/")
generateTrump.execute()
generateBiden.execute()
