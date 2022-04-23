#使用json格式讀取
import json
with open("config.json",mode="r") as file:
    data=json.load(file)
print("name",data["name"])
print("version",data["version"])