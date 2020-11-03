import json

# Open File And Add To List
with open("JsonBigFile/us_election20_tweet_pr.json", "r") as filin:
    ligne = filin.readline()
    arrayList = []
    stop = 0
    while ligne != "":
        arrayList.append(ligne)
        ligne = filin.readline()
        stop += 1
        if(stop == 1000):
            break


# Json Concatenante
jsonConcatenate = '{"jsonArray": [\n'
for elem in arrayList:
    if(arrayList[-1] == elem):
        jsonConcatenate = jsonConcatenate + elem
    else:
        jsonConcatenate = jsonConcatenate + elem + ','
jsonConcatenate = jsonConcatenate + ']}'


# Write File jsonArrayList
with open("Python/FileTest2.json", "w") as filout:
    for json in jsonConcatenate:
        filout.write(json)
