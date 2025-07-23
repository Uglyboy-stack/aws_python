myDict = {}
myDict["one"] = "1"
myDict["two"] = "2"
myDict[3] = "three"
myDict["four"] = "4.4"

print(myDict[3])

for key, value in myDict.items():
    print(key, value)
    
    name = "Alice"
    ans = "Alice"
    print(name.__eq__(ans))  # This will print True if both are equal
    
