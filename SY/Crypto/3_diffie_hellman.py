n = int(input("Enter a prime number (n): "))
g = int(input("Enter a primitive root (g): "))

x = int(input("Alice's private key (x): "))
A = pow(g, x, n)   # A = g^x mod n

y = int(input("Bob's private key (y): "))
B = pow(g, y, n)  

print("\nPublicly exchanged values:")
print("Alice sends A =", A)
print("Bob sends B =", B)

KA = pow(B, x, n)  # A's computes key
KB = pow(A, y, n)

print("\nShared Secret Keys:")
print("A's computed key:", KA)
print("B's computed key:  ", KB)

if KA == KB:
    print("\nKey exchange successful! Shared Key =", KA)
else:
    print("\nKey exchange failed!")
