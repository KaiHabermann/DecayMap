import json

with open("data/PDGIdentifiers-2022v0.json","r") as f:
    data = json.load(f)

data_map = {d["pdgId"]:d for d in data}
print(data_map)