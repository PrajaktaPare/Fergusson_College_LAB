plaintext=input("ENter plain text : ")
# keys=list(input("Enter keys : "))
key=3
ct=""


for i in plaintext:
    ct+=chr((((ord(i)-97)+key)%26)+97)
print(ct)
# j=0
# for i in plaintext:
#     ct+=chr((((ord(i)-97)+keys[j])%26)+97)
#     j=(j+1)%len(keys)

# print(ct)
