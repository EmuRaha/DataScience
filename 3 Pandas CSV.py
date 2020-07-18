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
print()
###############################################
###############################################

df = pd.read_csv("stock_data.csv")
print(df)
print()

df = pd.read_csv("stock_data.csv", skiprows=1)
print(df)
print()

df = pd.read_csv("stock_data.csv",header=1)
print(df)
print()
##### In case of missing header ########

df = pd.read_csv("stock_data.csv", header=None, names = ["ticker","eps","revenue","price","people"])
print(df)
print()

df = pd.read_csv("stock_data.csv", nrows=3)
print(df)
print()

df = pd.read_csv("stock_data.csv", na_values=['not available','n.a.'])
print(df)
print()

df.to_csv("new1.csv")
df.to_csv("new.csv", index=False)
print()

df = pd.read_excel("stock_data.xlsx","Sheet1")
print(df)
print()

############# converter ##################


def convert_people_cell(cell):
    if cell == "n.a.":
        return 'Sam Walton'
    return cell


def convert_price_cell(cell):
    if cell == "n.a.":
        return 50
    return cell


df = pd.read_excel("stock_data.xlsx", "Sheet1", converters={
    'people': convert_people_cell,
    'price': convert_price_cell
})
print(df)

print()

df.to_excel("new.xlsx", sheet_name="stocks", index=False, startrow=2, startcol=1)
print(df)
print()



##################  DataFrames in different sheets  #######################


df_stocks = pd.DataFrame({
    'tickers': ['GOOGL', 'WMT', 'MSFT'],
    'price': [845, 65, 64 ],
    'pe': [30.37, 14.26, 30.97],
    'eps': [27.82, 4.61, 2.12]
})

df_weather =  pd.DataFrame({
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'event': ['Rain', 'Sunny', 'Snow']
})

with pd.ExcelWriter("Stock_Weather.xlsx") as writer :
    df_stocks.to_excel(writer,sheet_name='Stocks')
    df_weather.to_excel(writer,sheet_name='Weather')































