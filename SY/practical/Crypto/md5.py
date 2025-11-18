import hashlib

text="abcd"

enc=hashlib.sha256(text.encode()).hexdigest()

# enc=hashlib.md5(text.encode()).hexdigest()

print(enc)