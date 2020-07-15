import json

myJson = ''' 
{
"Status" : "Ok",
"Source" : "This",
"Value" : "uid"
}

'''

a = json.loads(myJson)
print(a)

print(a["Source"])



jasonData = '{"A":"1","B":"2","C":"3"}'

js = json.loads(jasonData)
print(js)
print(js["B"])

with open("MyJson1.json","w") as f:
    json.dump(js,f)

















