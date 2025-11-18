text="prajaktapare"
key=2

enc={}
for i in range(key):
    enc[i]=""

j=0
sign="+"
for ch in text:
    enc[j]+=ch
    if sign=="+":
        if j==key-1:
            j=j-1
            sign="-"
        else :
            j=j+1
    else:
        if j==0:
            j=j+1
            sign="+"
        else:
            j=j-1
encstr=""
for i in range(key):
    encstr+=enc[i]
print(encstr)