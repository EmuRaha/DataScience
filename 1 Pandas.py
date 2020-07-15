import  pandas as pd

prices=[[16,27,33],[42,96],[23,35,58],[50,18,39],[32,67,98],[24,67,22],[23,58],[50,18,39]]

dataframe = pd.DataFrame(prices)
print(dataframe)
print()
dataframe.fillna(0,inplace=True)    ############# FILLNA################
print(dataframe)
print()
headers_dataframe = pd.DataFrame(prices,columns=['jan','feb','march'])
print(headers_dataframe)

print(headers_dataframe['jan'][3])
print(headers_dataframe.head()) #prints 1st 5 rows
print(headers_dataframe.tail()) #prints last 5 rows
print(headers_dataframe.head(3))
print(headers_dataframe.tail(3))
print()
print('Average values of January:',headers_dataframe['jan'].mean())

df = pd.DataFrame(prices,columns=['jan','feb','march'])
print()
print('Januray values when Feb values are 67 are:')
print(df['jan'][df['feb']==67])



######## CODEBASICS Pandas tutorials(look up for more)


































