import json

data = {
    124032: ("Bob", 23),
    436885: ("George", 15),
    987578: ("Alice", 31),
    457671: ("Bill", 54),
    321875: ("Polly", 8)
}

with open("01.json", "w") as file:
    json.dump(data, file)
