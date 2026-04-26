import copy

def generate_data():
    return [
        {"id": 1, "data": {"files": ["a.txt", "b.txt"], "usage": 500}},
        {"id": 2, "data": {"files": ["c.txt"], "usage": 300}}
    ]

def replicate_data(original):
    assigned = original
    shallow = list(original)
    deep = copy.deepcopy(original)
    return assigned, shallow, deep

def modify_data(data):
    for user in data:
        user["data"]["files"].append("new_file.txt")
        user["data"]["usage"] += 100
        if len(user["data"]["files"]) > 1:
            user["data"]["files"].pop(0)

def check_integrity(original, shallow, deep):
    leakage = 0
    safe = 0
    overlap = set()

    for i in range(len(original)):
        o = set(original[i]["data"]["files"])
        s = set(shallow[i]["data"]["files"])
        d = set(deep[i]["data"]["files"])

        if o == s:
            leakage += 1

        if o != d:
            safe += 1

        overlap.update(o & d)

    return (leakage, safe, len(overlap))


original = generate_data()

print("BEFORE")
print(original)

assigned, shallow, deep = replicate_data(original)

modify_data(shallow)
modify_data(deep)

print("\nAFTER")
print("Original:", original)
print("Shallow:", shallow)
print("Deep:", deep)

print("\nREPORT")
print(check_integrity(original, shallow, deep))