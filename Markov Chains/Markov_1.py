import numpy as np
import matplotlib.pyplot as plt
P=np.array([[.6,.1],[.5,.5]])
x=np.array([.1,.9])
##x=np.dot(x0,P)
##x2=np.dot(x1,P)

print('transistion matrix: \n',P)
print('transistion matrix squared: \n',P**2)
print('transistion matrix dot: \n',np.dot(P,P))

iterations=[]
sunny=[]
rain=[]


for i in range(50):
    if (i==0):
        print ('state ',i)
        print (x,'\n')
    else:
        x=np.dot(x,P)
        print ('state ',i,'\n')
        print (x,'\n')
        
    iterations.append(i)
    sunny.append(x[0])
    rain.append(x[1])

plt.plot(iterations,sunny)

plt.show()  


  

          
