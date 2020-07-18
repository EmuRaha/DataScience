import  pandas as pd

# data = pd.read_csv('MyFile.csv')

# print(data)
# print()
# print(data['Cousins'])
# print()
# print(data['Cousins'][0])

##################  CSV file   ###################

df = pd.read_csv('weather.csv')
print(df)
print()
print()
print('Dates when rained:')
print(df['Date'][df['Event']=='Rain'])

########################################################################


################# Dataframe using dictionary ######################
###########____Dictionary_____###################

weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature': [32,35,28,24,32,31],
    'windspeed': [6,7,2,7,4,2],
    'event': ['Rain', 'Sunny', 'Snow','Snow','Rain', 'Sunny']
}

df1 = pd.DataFrame(weather_data)
print(df1)

weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'windspeed': [6,7,2],
    'event': ['Rain', 'Sunny', 'Snow']
}
df2 = pd.DataFrame(weather_data)
print(df2)


############## Excel file ###############

df = pd.read_excel('weather.xlsx')
print(df)

############## Tuple's List(each tuple is a row)################

weather_data = [
    ('1/1/2017',32,6,'Rain'),
    ('1/2/2017',35,7,'Sunny'),
    ('1/3/2017',28,2,'Snow')
]
df = pd.DataFrame(data=weather_data, columns=['day','temperature','windspeed','event'])
print(df)

################# Dictionary's List#########################

weather_data = [
    {'day': '1/1/2017', 'temperature': 32, 'windspeed': 6, 'event': 'Rain'},
    {'day': '1/2/2017', 'temperature': 35, 'windspeed': 7, 'event': 'Sunny'},
    {'day': '1/3/2017', 'temperature': 28, 'windspeed': 2, 'event': 'Snow'},

]
df = pd.DataFrame(data=weather_data)
print("Dictionary's list method:")

print(df)























