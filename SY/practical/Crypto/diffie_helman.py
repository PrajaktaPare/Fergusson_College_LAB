#assymetric
def power(a,b,p):
    if b==1:
        return a
    else:
        return pow(a,b)%p

P=23 #prime
G=9 #coprime number

#user A
a=3
x=power(G,a,P) 

#user B
b=4
y=power(G,b,P)

ka=power(y,a,P)
kb=power(x,b,P)

print(ka)
print(kb)