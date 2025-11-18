import math
i1=0.2
i2=0.4
w1=0.3
w2=0.6
b=0.5

net=i1*w1+i2*w2+b

sigmoid_biploar=(1-math.exp(-net))/(1+math.exp(-net))

print(sigmoid_biploar)

sigmoid_unipolar=1/(1+math.exp(-net))

print(sigmoid_unipolar)