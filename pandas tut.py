import numpy as np
import pandas as pd

A = [1,2,3,4]
B = [2,3,4,5]
C = [6,7,8,9]
D = [0,1,2,3]
E = [4,5,6,7]

df = pd.DataFrame([A,B,C,D,E],["a","b","c","d","e"],["w","x","y","z"]) #CREATING TABLES
print(df)

print("😍") #FOR EMOJIS PRESS WINDOWS+FULLSTOP(.)

df["p"] = df["y"] + df["z"] #ADDING A NEW COLUMN WHICH IS SUM OF COLUMN Y AND Z
print(df)

df.drop("e",inplace=True) #DELETING A ROW WITH DROP E ROW IS DELEATED, INPLACE TRUE IS USED TO DELETE ROW PARMANENTLY
print(df)

df.drop("p",axis=1,inplace=True) #DELETING A COLUMN PARMENTLY WITH DROP AXIS =1 IS FOR Y AXIS OF TABLE AND INPLACE TURE IS TO DELETE PARMANTLY
print(df)

df.loc["a"] #used for accessing row
print(df.loc)

df[df>3] #shows values greater than 3

df[df["w"]>3][["w","z"]] #conditional accessing

k = {"item":["apple","apple","orange","orange","guns","guns"], "days":["mon","tue","wed","thu","fri","sat"], "sales": [200,100,300,80,5,10]}
print(k)

df = pd.DataFrame(k)
print(df)

x = df.groupby("item") #GROUPBY METHOD HAS FOLLOWING THINGS
print(x.mean())
print(x.sum())
print(x.max())
print(x.min())
print(x.describe())
print(x.describe().transpose())


#x.join(k)# used to join two dataframes

 #CONCAT IS USED TO JOIN 2 OR MORE DATAFRAMES WITH DIFFERENT INDEXING JUST SPECIFY AXIS 1 OR 0


x1 = {"a":[1,1,1,1,1],"b":[1,1,1,1,1],"c":[1,1,1,1,1],"d":[1,1,1,1,1],"e":[1,1,1,1,1]}
x2 = {"e":[2,2,2,2,2],"f":[2,2,2,2,2],"g":[2,2,2,2,2],"h":[2,2,2,2,2],"i":[2,2,2,2,2]}
x3 = {"a":[3,3,3,3,3],"b":[3,3,3,3,3],"c":[3,3,3,3,3],"d":[3,3,3,3,3],"e":[3,3,3,3,3]}

df1 = pd.DataFrame(x1, index = [1,2,3,4,5])
df2 = pd.DataFrame(x2, index = [1,2,3,4,5])
df3 = pd.DataFrame(x3, index = [5,6,7,8,9])

print(df1)
print(df2)
print(df3)

print(pd.concat([df1,df2],axis = 1))
print(pd.concat([df1,df2]))
print(pd.concat([df1,df2,df3],axis = 1))
print(pd.concat([df1,df2,df3],axis = 0))
print(pd.concat([df1,df3]))

print(pd.merge(df1,df2, how = "right"))

