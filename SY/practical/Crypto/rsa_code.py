import rsa as rsa_code

pt="XYZ"
pb,pk=rsa_code.newkeys(2048)
ct=rsa_code.encrypt(pt.encode(),pb)
dc=rsa_code.decrypt(ct,pk).decode()

print(pt)
print(ct)
print(dc)