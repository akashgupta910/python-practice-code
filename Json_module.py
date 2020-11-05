import json

data = ' { "name": "Akash", "age": 30, "city": "gaya"  } '

parsed = json.loads(data)

# print(parsed["name"])
# print(type(parsed))


dict = {
    "name": "dictionary",
    "cars": ["BMW", "Mercedes", "Audi", "Ferrari"],
    "Devices": ("Apple MacBook Air", "iPhone X"),
    "isbad": False
}

# We use json.dumps to make it compatible to Javascript

jcomp = json.dumps(dict)
print(jcomp)


# Short Notes:-
#
# json.loads = Parsed the data
# json.dumps = make compatible to Javascript.
