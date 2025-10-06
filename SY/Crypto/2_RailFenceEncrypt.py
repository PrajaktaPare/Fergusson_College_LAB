def encryptText(normalText, key):
    s = normalText
    k = key
    d = {i: "" for i in range(k)}
    
    i = 0
    while i < len(s):
        for j in range(k):
            if i < len(s):
                d[j] += s[i]
                i += 1

        for j in range(k-2, 0, -1):
            if i < len(s):
                d[j] += s[i]
                i += 1
    print(d)
    return ''.join(d.values())

s = input("Enter Plain text : ")
k = int(input("Enter Key : "))
encrypted_text = encryptText(s, k)
print(encrypted_text)
