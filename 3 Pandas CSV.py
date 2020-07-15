import pandas as pd
import numpy as np

prices=[[16,27,33],[42,95,96],[23,35,58],[50,18,39],[32,67,98],[24,67,22],[23,35,58],[50,18,39]]

df = pd.DataFrame(prices)
print(df)
print(df.shape)
print()
print(df.iloc[1:4,0:2])     #slicing
print()
dataframe = pd.DataFrame(prices,columns=['jan','feb','march'])
print(dataframe)
print(dataframe.iloc[1:4,0:2])
pd.DataFrame(dataframe).to_csv("OutPut.csv")

dataframe.to_csv('Output.csv')










