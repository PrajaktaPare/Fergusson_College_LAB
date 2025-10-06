def generate_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()

    for ch in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in used:
            matrix.append(ch)
            used.add(ch)

    return [matrix[i:i+5] for i in range(0, 25, 5)]

def format_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    pairs, i = [], 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else "X"
        if a == b:
            pairs.append(a + "X")
            i += 1
        else:
            pairs.append(a + b)
            i += 2
    return pairs

def find_pos(matrix, ch):
    for i, row in enumerate(matrix):
        if ch in row:
            return i, row.index(ch)

def playfair_encrypt(plainText, key):
    matrix = generate_matrix(key)
    pairs = format_text(plainText)
    cipher = ""

    for a, b in pairs:
        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)

        if r1 == r2: 
            cipher += matrix[r1][(c1+1) % 5]
            cipher += matrix[r2][(c2+1) % 5]
        elif c1 == c2:  
            cipher += matrix[(r1+1) % 5][c1]
            cipher += matrix[(r2+1) % 5][c2]
        else:  
            cipher += matrix[r1][c2]
            cipher += matrix[r2][c1]

    return cipher

plainText = input("Enter the plain text: ")
key = input("Enter the key: ")

cipher = playfair_encrypt(plainText, key)
print("Encrypted:", cipher)
