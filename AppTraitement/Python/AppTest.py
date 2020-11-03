import json

# Open File And Add To List
with open("Python\FileTest.json", "r") as filin:
    ligne = filin.readline()
    arrayList = []
    while ligne != "":
        arrayList.append(ligne)
        ligne = filin.readline()



# Json Encode File & Concatenante
#jsonArrayList = json.dumps(ArrayList, sort_keys=True, indent=4)
jsonConcatenate = '{"jsonArray": [\n'

for elem in arrayList:
    jsonConcatenate = jsonConcatenate + elem + ','

jsonConcatenate = jsonConcatenate + ']}'


# Write File jsonArrayList
with open("Python/FileTest2.json", "w") as filout:
    for json in jsonConcatenate:
        filout.write(json)







#
