def f(net):
    if net>=1:
        return 1
    else:
        return 0
w1=w2=w3=w4=w5=w6=w7=w8=i1=i2=2

h11=i1*w1+w3*i2
h12=i1*w2+i2*w4

h1=f(h11)
h2=f(h12)

c11=h1*w5+h2*w7
c12=h1*w6+h2*w8

c1=f(c11)
c2=f(c12)

print(c1)
print(c1)


