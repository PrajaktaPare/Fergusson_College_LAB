def caesar_encrypt(text, key):
    encrypted = ""
    for ch in text.upper():
        if ch.isalpha():
            encrypted += chr((ord(ch) - 65 + key) % 26 + 65)
        else:
            encrypted += ch
    return encrypted

def caesar_decrypt(cipher, key):
    decrypted = ""
    for ch in cipher.upper():
        if ch.isalpha():
            decrypted += chr((ord(ch) - 65 - key) % 26 + 65)
        else:
            decrypted += ch
    return decrypted


def modified_encrypt(text, keys):
    encrypted = ""
    for i, ch in enumerate(text.upper()):
        if ch.isalpha():
            shift = keys[i % len(keys)]
            encrypted += chr((ord(ch) - 65 + shift) % 26 + 65)
        else:
            encrypted += ch
    return encrypted

def modified_decrypt(cipher, keys):
    decrypted = ""
    for i, ch in enumerate(cipher.upper()):
        if ch.isalpha():
            shift = keys[i % len(keys)]
            decrypted += chr((ord(ch) - 65 - shift) % 26 + 65)
        else:
            decrypted += ch
    return decrypted


plainText = input("Enter the plain text: ")

print("\n1. Caesar Cipher")
print("2. Modified Caesar Cipher")
choice = int(input("Choose (1/2): "))

if choice == 1:
    key = int(input("Enter key (shift value): "))
    cipher = caesar_encrypt(plainText, key)
    print("Encrypted:", cipher)
    print("Decrypted:", caesar_decrypt(cipher, key))

elif choice == 2:
    keys = list(map(int, input("Enter keys (comma separated): ").split(",")))
    cipher = modified_encrypt(plainText, keys)
    print("Encrypted:", cipher)
    print("Decrypted:", modified_decrypt(cipher, keys))

else:
    print("Invalid choice!")
