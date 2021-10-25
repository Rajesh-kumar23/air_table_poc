import requests
import json
from airtable import airtable


# Fetch AirTable data and convert in json formate with requests liberary
url = "https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"
headers = {
    'Authorization': 'Bearer {API_KEY}',
}
air_table_response = requests.request("GET", url, headers=headers)
airtable_json_data = json.loads(air_table_response.text)

print(type(airtable_json_data))

# Fetch AirTable data with airtable liberary in dictonary formate
at = airtable.Airtable('{BASE_ID}', '{API_KEY}')
airtable_json_data = at.get('{TABLE_NAME}')
# print(airtable_json_data)

# Serializing json 
json_object = json.dumps(airtable_json_data, indent = 4)

# Writing to sample.json
# with open("sample.json", "w") as outfile:
#     outfile.write(json_object)