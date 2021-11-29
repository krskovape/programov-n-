import requests

URL = "https://mapa.pid.cz/getData.php"

r = requests.get(URL)
#print(r.status_code)
#print(r.encoding)
#print(r.text[:100])
#print(r.json())
data = r.json()

#print(type(data))
#print(data.keys())
#print(type(data['trips'].keys()))
#print(data['trips']['389/2'])

vehicles = data['trips'].values()
#print(vehicles)

#kolik vozidel je na každé lince
linky = {}
for val in vehicles:
    if val["route"] in linky:
        linky[val["route"]] += 1
    else:
        linky[val["route"]] = 1

print(linky)