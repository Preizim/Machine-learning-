#numpy useage

import numpy as np

arr = np.array([1,2,3,4,5])

print(arr)
print(arr * 2)
print(arr*arr)

matrix = np.array([[1,2,3],
                   [4,5,6]])

print(matrix)
print(matrix.shape)

matrics=np.array([[1,2,3,4,5], 
                                      [4,5,6,7,6]])

print(matrics)
print(matrics.shape)


#panda arranges your array

import pandas as pd

data = {
    "Name": ["John","Mary","David"],
    "Age": [20,21,19],
    "Score": [85,90,88],
    "Class": ['Jss 1', 'Jss 2', 'Jss 3']
}

df = pd.DataFrame(data)

print(df)



import pandas as pd

df = pd.read_csv("pra1.csv")
print(df)

print(df[["Name", 'Score']])


import pandas as pd

df = pd.read_csv("pra.csv")

print(df.isnull().sum())

df = df.fillna(df["Age"].mean())

print(df)

