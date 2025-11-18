r1=int(input("enter r1 : "))
c1=int(input("enter c1 : "))
r2=int(input("enter r2 : "))
c2=int(input("enter c2 : "))

a=[]
for i in range(r1):
    row=[]
    for j in range(c1):
        a[i][j]=int(input(f"Enter A{i+1} {j+1}: "))
        row.append(a[i][j])
    a.append(row)


b=[]
for i in range(r2):
    row=[]
    for j in range(c2):
        b[i][j]=int(input(f"Enter B{i+1} {j+1}: "))
        row.append(b[i][j])
    b.append(row)


c=[]

for i in range(r1):
    row=[]
    for j in range(c2):
        temp=[]
        for k in range(c1):
            temp.append(min(a[i][k],b[k][j]))
        row.append(min(temp))
    c.append(row)

d=[]

for i in range(r1):
    row=[]
    for j in range(c2):
        temp=[]
        for k in range(c1):
            temp.append(min(a[i][k],b[k][j]))
        row.append(max(temp))
    d.append(row)