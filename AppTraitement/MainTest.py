import json
from Python.GenerateImgResult import GenerateImgResult


with open("Result/Biden/Biden.json") as f:
    biden = json.load(f)



generate = GenerateImgResult(biden, "Biden/")



generate.execute()
