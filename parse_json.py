import json

file = open("resume_json/13582.json", "r")

json_object = json.loads(file.read())
print(json_object)
