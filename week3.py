import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
movies= pd.read_csv('movies.csv')

Year_array=np.array(movies["Year"])
rating_array=np.array(movies["Rating"])
plt.plot(Year_array, rating_array)

plt.title("Year_array")
plt.xlabel("Rating_array")
plt.ylabel("movies Used (movies)")

plt.show()



#days = [1,2,3,4,5,6,7]
#water_usage = [120,150,130,170,160,140,120]

#plt.plot(days, water_usage)

#plt.title("Daily Water Usage")
#plt.xlabel("Day")
#plt.ylabel("Water Used (Litres)")

#plt.show()