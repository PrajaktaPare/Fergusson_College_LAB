n=int(input("enter size of a: "))
m=int(input("enter size of b: "))
a=[]
b=[]
for i in range(n):
    val=float(input(f"enter {i+1}: "))
    a.append(val)

for i in range(m):
    val=float(input(f"enter {i+1}: "))
    b.append(val)

aunionb=[max(i,j) for i, j in zip(a,b)]

print(aunionb)

comp=[1-i for i in aunionb]


compa=[1-i for i in a]
compb=[1-i for i in b]

ca_intersection_cb=[min(i,j) for i,j in zip(compa,compb)]

print("Demorgans law : ",comp==ca_intersection_cb)