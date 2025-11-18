m=[[0.4,0.3,0.2],[0.9,0.8,0.1],[0.6,0.7,0.5]]

l=0.4
r,c=3,3
lm=[]
for i in range(r):
    row=[] 
    for j in range(c):
        if m[i][j]>=l:
            row.append(1)
        else:
            row.append(0)
    lm.append(row)
print(lm)