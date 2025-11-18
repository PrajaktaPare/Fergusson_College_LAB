pt = "arbc"
key = "dced"

encStr = ""

for i in range(len(pt)):
    encStr += chr(((ord(pt[i]) - 97) + (ord(key[i]) - 97)) % 26 + 97)

print(encStr)