import pandas as pd
import numpy as np
import plotly as pl
import cufflinks as cf
import plotly.offline as po

po.init_notebook_mode(connected=True)

cf.go_offline()


df = pd.DataFrame(np.random.rand(100,5), columns = ["a","b","c","d","e"])
df2 = pd.DataFrame({"x":["a","b","c","d","e"], "y": [1,2,3,4,5], "z": [6,7,8,4,3]})

#PLOTTING POINT PLOTS
df.iplot(kind="scatter")
df.iplot(kind="scatter", x='a', y='b', mode='markers')
df.scatter_matrix()

#PLOTTING SURFACE PLOTS
df3 = pd.DataFrame({"x":[3,6,12,5,8], "y": [1,2,3,4,5], "z": [6,7,8,4,3]})

df3.iplot(kind="surface")
cf.datagen.sinwave(10,.25).iplot(kind = "surface", theme = "solar", colorscale="brbg", margin=(0,0,0,0))

#PLOTTING FIGURE PLOTS INTERACTIVE
df[["a","b"]].iplot(kind = "spread")

