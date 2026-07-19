import json

data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "Django", "JavaScript"]
}

print_json = json.dumps(data, indent=4)
print(print_json)


"""{
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "skills": [
        "Python",
        "Django",
        "JavaScript"
    ]
}"""