import pandas as pd
from matplotlib import pyplot plt
data=pd.read_csv (r'sample.csv')
data.head()

df= pd.DataFrame(data)
Region=df["Region"].head(4)
sales=df["sales"].head(4)
fig=plt.figure(figsize=(10,7))
plt.bar(Region[0:10],Sales[0:10])
plt.Show()
plt.pie(Sales,Labels=Region)
plt.legend()
plt.show()