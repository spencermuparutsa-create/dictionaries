capitals = {"UK":"London","Ireland":"Dublin"}
print(capitals)
capitals ["Canada"] = "Ottawa"
print(capitals)
print(capitals["UK"])
x = list(capitals.keys())
print(x)
v = list(capitals.values())
print(v)
if "Canada" in capitals:
    print("yes")
else:
    print("no")