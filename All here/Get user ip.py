import requests
api_url = 'https://api.ipify.org?format=json'
res = requests.get(api_url)

if res.status_code == 200:
   data = res.json()
   ip = data.get('ip')
   print('Your ip address is',ip)