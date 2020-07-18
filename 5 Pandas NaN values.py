import pandas as pd

df = pd.read_csv("weather_data.csv")
print(df)
print()
df = pd.read_csv("weather_data.csv",parse_dates=['day'])
print(df)
print()
print(type(df['day'][0]))

df.set_index('day')
print(df)
######     inplace=True>>> modifies original dataframe.
########  if inplace=True not given>>>> returns a new dataframe
df.set_index('day',inplace= True)
print(df)
print()
new_df = df.fillna(0)
print(new_df)
print()
######  0 doesn't mean anything in event column. so we need to specify by using a dictionary

new_df = df.fillna(
{
    'temperature': 0,
    'windspeed' : 0,
    'event' : 'No event'
})
print(new_df)
print()

print(df)
print()
new_df = df.fillna(method='ffill')
print(new_df)
print()
new_df = df.fillna(method='bfill')
print(new_df)
print()
new_df = df.fillna(method='bfill',axis='columns')
print(new_df)
print()
new_df = df.fillna(method='ffill',axis='columns')
print(new_df)
print()
new_df = df.fillna(method='ffill',limit=1)
print(new_df)
print()
new_df = df.interpolate()
print(new_df)
print()
new_df = df.interpolate(method='time')
print(new_df)
print()
new_df = df.dropna()
print(new_df)
print()
new_df = df.dropna(how='all')
print(new_df)
print()
############   how='all>> if all values in the row is NaN then drop that.¶
############   threshold parameter>> thresh=1>> acts same way, if at least one value in the row then keep the row
new_df = df.dropna(thresh=1)
print(new_df)
print()
dt = pd.date_range("01-01-2017","01-11-2017")
idx = pd.DatetimeIndex(dt)
df = df.reindex(idx)
print(df)


