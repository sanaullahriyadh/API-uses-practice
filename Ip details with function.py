import requests

def res_data(url):
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
    return data


ip_find_url = 'https://api.ipify.org?format=json'
# res = requests.get(api_find_url)
# if res.status_code == 200:
#     data = res.json()
data = res_data(ip_find_url)
ip = data.get('ip')

ip_location_url = f'https://ipapi.co/{ip}/json/'
# r = requests.get(ip_location_url)
# if r.status_code == 200:
#     ip_details = r.json()

ip_details = res_data(ip_location_url)
city = ip_details.get('city')
region = ip_details.get('region')
country_name = ip_details.get('country_name')

sentence = f'This ip({ip}) is located is {city}, {region}, {country_name}'
print(sentence)