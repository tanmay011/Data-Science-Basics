import pandas as pd
import seaborn as sns
import numpy as np


df1 = sns.load_dataset("tips")
df2 = pd.read_csv("188.iris.csv")

x1 = np.random.rand(100,5)
x2 = np.random.rand(10,5)
df3 = pd.DataFrame(x1, columns = ["a","b","c","d","e"])
df4 = pd.DataFrame(x2, columns = ["a","b","c","d","e"])

df3.plot.scatter(x ="a", y = "b") #PLOTTING POINT PLOT
df4.plot.scatter(x ="a", y = "b")

df4.plot.line() #PLOPTTING LINE PLOT
df3["a"].plot.kde()
df3.plot.kde()
df1["tip"].plot.line()

df4.plot.hist()    #PLOTTING DISTRIBUTION GRAPH
df2.plot.bar()
df4.plot.area()
df4.plot.box(color="g")
df3.plot.hexbin(x="a",y="b",gridsize=10)
