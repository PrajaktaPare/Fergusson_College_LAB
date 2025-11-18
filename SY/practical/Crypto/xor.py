pt="abcd"

zero=[chr(ord(ch)^0) for ch in pt]
one=[chr(ord(ch)^1) for ch in pt]

print(zero)
print(one)