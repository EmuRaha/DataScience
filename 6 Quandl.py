
import quandl as qd



dataset = qd.get('CHRIS/ASX_WM2')

print(dataset)
print(dataset.head())
print()
print('Previous Settlement column is:')
print(dataset.head()['Previous Settlement'])
print()
print('First 20 colums of "Previous Settlement" is:')
print(dataset.head(20))
print()
print()
print('11th to 20th values of "Previous Settlement" column is:')
print(dataset['Previous Settlement'][11:21])
print()

dataset['Double_Previous Settlement'] = 2* dataset['Previous Settlement']

dataset = dataset[['Previous Settlement','Double_Previous Settlement']]
print()
print('First 20 colums of "Previous Settlement" is:')
print(dataset.head(20))


























