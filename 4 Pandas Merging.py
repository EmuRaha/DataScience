# Merging
import pandas as pd





df1 = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns=['A','B','C'])
print(df1)
print()

df2 = pd.DataFrame([[13,5,345],[44,8,86],[67,2,97]], columns=['X','Y','Z'])
print(df2)
print()

df3 = pd.merge(df1,df2,right_on='Y',left_on='B')
print(df3)
print()

df4 = pd.merge(df2,df1,right_on='B',left_on='Y')
print(df4)


























