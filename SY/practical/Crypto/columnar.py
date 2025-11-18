text="prajaktapare"
key=[1,2,3]

enc={}
for i in key:
    enc[i]=""

j=0
for ch in text:
    enc[key[j]]+=ch
    j=(j+1)%(len(key))


encstr="" 

for i in key:
    encstr+=enc[i]
    
print(encstr)