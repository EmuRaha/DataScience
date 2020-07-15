import  pandas as pd

# data = pd.read_csv('MyFile.csv')

# print(data)
# print()
# print(data['Cousins'])
# print()
# print(data['Cousins'][0])

##################        NEW        ###################

df = pd.read_csv('weather.csv')
print(df)
print()
print()
print('Dates when rained:')
print(df['Date'][df['Event']=='Rain'])

########################################################################
################# Dataframe using dictionary ######################

weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature': [32,35,28,24,32,31],
    'windspeed': [6,7,2,7,4,2],
    'event': ['Rain', 'Sunny', 'Snow','Snow','Rain', 'Sunny']
}

df1 = pd.DataFrame(weather_data)
print(df1)





























