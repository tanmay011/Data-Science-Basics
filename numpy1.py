import numpy as np

x = ([[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]])
print(x)

y = np.array(x)

print(y)

''' METHODS OF NUMPY '''
print(np.zeros((3,3)) + 5)#FOR ZEERO MATRIX ADDITION,SUB,MUL,DIV CAN BE PERFORMED ON THEM

print(np.ones((3,3)))#FOR ONES MATRIX
 
print(np.eye(4))#FOR IDENTITY MATRIX

print(np.arange(50).reshape(5,10))#CREATE ARRAY AND RESHAPE IN MATRIX

print(np.linspace(0,100,5))#CREATE A ARRAY WITH LINEAR SPACING 



v = np.arange(10)

w = np.arange(11,20)

print(np.sin(v))

print(np.cos(w))

print(np.log(v))

j = np.arange(12).reshape(3,4)
print(j)

i = np.arange(10,22).reshape(3,4)
print(i)

print(j + i)


