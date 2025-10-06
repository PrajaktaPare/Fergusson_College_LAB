def columnar_encrypt(text, key):
    text = text.replace(" ", "")
    n = len(key)
    rows = (len(text) + n - 1) // n
    matrix = [text[i*n:(i+1)*n] for i in range(rows)]
    while len(matrix[-1]) < n:
        matrix[-1] += 'X'
    cipher = ''
    for idx in sorted(range(len(key)), key=lambda x: key[x]):
        for row in matrix:
            cipher += row[idx]
    return cipher

text = input("Enter text: ")
key = input("Enter key: ")
print("Columnar Encrypted:", columnar_encrypt(text, key))












# cols = int(input("Give the column count: "))

# keys = []
# for i in range(cols):
#     key = int(input("Enter the key: "))
#     keys.append(key)

# print(keys)

# plainText = input("Enter the plain text: ")
# print(len(plainText))

# while len(plainText) % cols != 0:
#     plainText += ' '

# rows = len(plainText) // cols

# matrix = []
# i = 0
# while i < len(plainText):
#     j = 0
#     tempRow = []
#     while j < cols and i < len(plainText):
#         tempRow.append(plainText[i])
#         j += 1
#         i += 1
#     matrix.append(tempRow)

# print("Matrix:")
# print(matrix)

# cipherText = ''

# key_order = sorted([(k, i) for i, k in enumerate(keys)])

# for k, index in key_order:
#     for row in matrix:
#         cipherText += row[index]

# print("Cipher Text:")
# print(cipherText)





# # PS Y:\Sem-3\Codes\Codes\Crypto> python .\columnar.py
# # Give the column count: 3
# # Enter the key: 2
# # Enter the key: 1
# # Enter the key: 3
# # [2, 1, 3]
# # Enter the plain text: ajinkya
# # 7
# # Matrix:
# # [['a', 'j', 'i'], ['n', 'k', 'y'], ['a', ' ', ' ']]
# # Cipher Text:
# # jk anaiy 
# # PS Y:\Sem-3\Codes\Codes\Crypto> 