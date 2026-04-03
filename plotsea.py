import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Day":[1,2,3,4,5],
    "Water":[120,150,130,170,160]
}

df = pd.DataFrame(data)

#sns.lineplot(x="Day", y="Water", data=df)
plt.bar('Day', 'Water', data=df)
#plt.hist([120,150,130,170,160,140])
plt.title("Water Usage Distribution")
plt.show()