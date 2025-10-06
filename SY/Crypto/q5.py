import cryptocode
import hashlib
import base64

while True:
    print("\n==== MENU ====")
    print("1. Encrypt/Decrypt text (cryptocode)")
    print("2. Hash text (MD5 & SHA256)")
    print("3. Base64 Encode/Decode")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        text = input("Enter text to encrypt: ")
        password = input("Enter password for encryption: ")
        encrypted = cryptocode.encrypt(text, password)
        decrypted = cryptocode.decrypt(encrypted, password)
        print("Encrypted text:", encrypted)
        print("Decrypted text:", decrypted)

    elif choice == '2':
        msg = input("Enter text to hash: ").encode()
        md5_hash = hashlib.md5(msg).hexdigest()
        sha256_hash = hashlib.sha256(msg).hexdigest()
        print("MD5 Hash:", md5_hash)
        print("SHA256 Hash:", sha256_hash)

    elif choice == '3':
        msg = input("Enter text for Base64 encoding: ").encode()
        encoded = base64.b64encode(msg).decode()
        decoded = base64.b64decode(encoded).decode()
        print("Base64 Encoded:", encoded)
        print("Base64 Decoded:", decoded)

    elif choice == '4':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please enter 1-4.")

# PS Z:\Crypto\Practicals> python last_menu.py
   
# ==== MENU ====
# 1. Encrypt/Decrypt text (cryptocode)
# 2. Hash text (MD5 & SHA256)
# 3. Base64 Encode/Decode
# 4. Exit
# Enter your choice (1-4): 1
# Enter text to encrypt: Vaibhavi
# Enter password for encryption: 3
# Encrypted text: wGFkIw5MRA0=*Ghw4eTnc/CVZeXmNqiY92A==*0mJrGqaCFXZM7VoSQRTlwQ==*clJh+m4w7/9iLrZZ2rN1mg==
# Decrypted text: Vaibhavi

# ==== MENU ====
# 1. Encrypt/Decrypt text (cryptocode)
# 2. Hash text (MD5 & SHA256)
# 3. Base64 Encode/Decode
# 4. Exit
# Enter your choice (1-4): 2
# Enter text to hash: Vaibhavi
# MD5 Hash: e5eeab8ab84bd408bef01e794be422a0
# SHA256 Hash: e4329990602e38aeb1621fe5311c6b3a8e1698a09ede9e2b7261d4347ac43834

# ==== MENU ====
# 1. Encrypt/Decrypt text (cryptocode)
# 2. Hash text (MD5 & SHA256)
# 3. Base64 Encode/Decode
# 4. Exit
# Enter your choice (1-4): 2
# Enter text to hash: Vaibhavi
# MD5 Hash: e5eeab8ab84bd408bef01e794be422a0
# SHA256 Hash: e4329990602e38aeb1621fe5311c6b3a8e1698a09ede9e2b7261d4347ac43834

# ==== MENU ====
# 1. Encrypt/Decrypt text (cryptocode)
# 2. Hash text (MD5 & SHA256)
# 3. Base64 Encode/Decode
# 4. Exit
# Enter your choice (1-4): 3
# Enter text for Base64 encoding: Vaibhavi 
# Base64 Encoded: VmFpYmhhdmk=
# Base64 Decoded: Vaibhavi

# ==== MENU ====
# 1. Encrypt/Decrypt text (cryptocode)
# 2. Hash text (MD5 & SHA256)
# 3. Base64 Encode/Decode
# 4. Exit
# Enter your choice (1-4): 3
# Enter text for Base64 encoding: Vaibhavi
# Base64 Encoded: VmFpYmhhdmk=
# Base64 Decoded: Vaibhavi

# ==== MENU ====
# 1. Encrypt/Decrypt text (cryptocode)
# 2. Hash text (MD5 & SHA256)
# 3. Base64 Encode/Decode
# 4. Exit
# Enter your choice (1-4): 4
# Exiting program...
# PS Z:\Crypto\Practicals> 
