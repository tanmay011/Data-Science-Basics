import seaborn as sns
import numpy as np
import pandas as pd

tips = sns.load_dataset("tips")
print(tips)

tips.head() #FIRST FIVE RECORDS ARE DISPLAYED

#POINT PLOT IN SEABORN PLOTS ONLY ON ONE PARAMETER EG- TOTAL_BILL
sns.kdeplot(tips["total_bill"])

sns.distplot(tips["total_bill"], kde =False)

#DISTRIBUTION PLOTS ARE PLOTS WHICH ARE PLOTTED ON 2 PARAMETER THEY CAN BE DIRECTLY PLOTTED 
#OR EVEN JOINTLY PLOTTED
sns.jointplot(x= "total_bill", y= "tip", data= tips)

#PAIR PLOT IS A GRAPH TO ANALYSE WHOLE DATA 
sns.pairplot(tips)

#CATEGORIAL PLOTS ARE GRAPH WHICH PLOT A NUMERICAL VALUE VS STRING AND VICE VERSA
sns.pointplot(x="day", y="total_bill", data=tips)

sns.swarmplot(x="smoker", y="tip", data=tips, hue="sex")

sns.barplot(x="day", y="tip", data=tips)

sns.boxplot(x="day", y="tip", data=tips, hue="sex")

#MATRIX PLOT ARE USED TO MAKE HEAT MAPS FIRST THE FILE IS NEEDED TO BE CONVERTED IN MATRIX THEN OPERATIONS ARE PERFORMED ON IT
tips2 = tips.pivot_table(index='day', columns = "tip", values = "total_bill")
sns.heatmap(tips2, annot = True)
sns.heatmap(tips2, lw = 1, annot = True)

#STYLING OF GRAPH CAN BE DONE VIA WRITING MATPLOTLIB INLINE BELOW IMPORT LIBRARY
# sns.set_style() is used to style the graph eg. in grid, paper,notebook view etc.


