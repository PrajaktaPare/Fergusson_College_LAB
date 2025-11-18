m=[[0,0],[0,1],[1,0],[1,1]]
# y=[0,0,0,1] #AND
y=[0,1,1,1] #OR

w=[0,0]
b=0
lr=0.1
def f(net):
    if net>=1:
        return 1
    else:
        return 0
    
epoch=10
for i in range(epoch):
    for j in range(len(m)):
        net=(m[j][0]*w[0])+(m[j][1]*w[1])+b

        op=f(net)
        error=y[j]-op

        w[0]+=lr*m[j][0]*error
        w[1]+=lr*m[j][1]*error
        b+=lr*error
print(w)
print(b)