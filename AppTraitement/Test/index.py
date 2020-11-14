import json
from GenerateImgResult import GenerateImgResult


with open("Biden500.json") as f:
    biden = json.load(f)




generate = GenerateImgResult(biden, "Biden/")



generate.execute()
