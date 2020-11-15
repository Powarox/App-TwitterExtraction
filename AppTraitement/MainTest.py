import json
from Python.GenerateImgResult import GenerateImgResult


with open("Result/Biden/Biden.json") as f:
    biden = json.load(f)


# Création des Img grâce aux stats
generateBiden = GenerateImgResult(biden, "Biden/")
generateTrump = GenerateImgResult(biden, "Trump/")
generateBiden.execute()
generateTrump.execute()
