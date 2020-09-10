import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0,10,20)
y = x * x
z = x+y
#PLOTTING GRAPH WITH X AXIS Y AXIS AND TITLE
print(plt.plot(x,y))
print(plt.xlabel("x axis"))
print(plt.ylabel("y axis"))
print(plt.title("demo graph"))
#PLOTTING SUB GRAPHS AND TIGHT LAYOUT IS FOR DISTANCE IN GRAPHS
print(plt.subplot(3,2,1))
print(plt.plot(x,y))
print(plt.subplot(3,2,2))
print(plt.plot(x,z))
print(plt.subplot(3,2,3))
print(plt.plot(y,z))
print(plt.subplot(3,2,4))
print(plt.plot(x,x))
print(plt.subplot(3,2,5))
print(plt.plot(y,x))
plt.tight_layout()


#PLOTTING SUB PLOTS USING OBJECT ORIENTED APPROCH
fig, axes = plt.subplots(1,4)

axes[0].plot(x,y) #this will only work when there there is only one row in more than one row it will not work because of indexing problem
axes[1].plot(y,x)    
axes[3].plot(y,x) 
print(plt.xlabel("x axis"))
print(plt.ylabel("y axis"))
 
plt.tight_layout()   

#For more than one row we use the tuple for specifying the position of which graph to plot
fig, axes1 = plt.subplots(2,2)

axes1[(1,1)].plot(x,y)

axes1[(0,1)].plot(y,x)
plt.tight_layout()


#STYLIMG OF GRAPH
fig = plt.figure()
axes = fig.add_axes([0,0,1,1])
axes.plot(x,y)



