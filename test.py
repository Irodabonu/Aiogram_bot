import logging
import requests
from pprint import pprint as prints
import json
# name = 'Weasley'
# url = f"https://api.potterdb.com/v1/characters?sort={name}"
# r = requests.get(url)
# jsonm = r.json()
#
# prints(jsonm['data'][2]['attributes']['image'])
# prints(jsonm['data'][7]['attributes']['image'])
# prints(jsonm['data'][8]['attributes']['image'])
# prints(jsonm['data'][9]['attributes']['image'])
name = [308, 401, 406, 506, 103, 200]
url = f"https://status.pizza/{name[4]}"
r = requests.get(url)
prints(r)
print(r.status_code)  # Output: 200
with open('image.png', 'wb') as f:
    f.write(r.content)



