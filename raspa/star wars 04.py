import requests
import json

url = 'http://swapi.co/api/starships/'
for d in range(1, 5):
  d = '' if d == 1 else '?page='+str(d)
  res = requests.get(url+str(d))
  res = json.loads(res.content.decode('utf-8'))
  for ship in res['results']:
    print (ship['name'])
  
