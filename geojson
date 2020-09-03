import json,urllib.request,urllib.parse,urllib.error

address=input('Enter location: ')
api_key = 42    
params=dict()           
params['key']=api_key                            #Api Key
params['address']=address                       #Address

serviceurl = "http://py4e-data.dr-chuck.net/json?"  # Service URL

url=serviceurl+urllib.parse.urlencode(params)
d=urllib.request.urlopen(url)
data=d.read().decode()
res=json.loads(data)
print('Retrieving '+url)
print('Retrieved '+str(len(data)))
print(res['results'][0]['place_id'])

