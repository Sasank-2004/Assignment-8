from matplotlib import pyplot as plt
import numpy as np
def f(x,pr):
    if x<0 : return 0
    elif x<1 : return pr["X=0"]
    elif x<2 : return pr["X=0"] + pr["X=1"]
    else : return pr["X=0"] + pr["X=1"] + pr["X=2"] 
x = np.linspace(-10,10,num=100)
S = ["HH","HT","TH","TT"]
X = {i : i.count('H') for i in S }
pr = {"X=0":1/4,"X=1":2/4,"X=2":1/4}
y = [f(i,pr) for i in x] 
plt.plot(x,y)
plt.title("CDF")
plt.xlabel("x")
plt.ylabel("Fx(x)")
plt.show()