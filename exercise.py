import json
import requests

countries_response = requests.get("https://raw.githubusercontent.com/everypolitician/everypolitician-data/master/countries.json")

countries = countries_response.json()

# print(countries[0].keys())
# dict_keys(['name', 'country', 'code', 'slug', 'legislatures'])

# print(countries[0]['legislatures'][0].keys())
# dict_keys(['name', 'slug', 'sources_directory', 'popolo', 'popolo_url', 'names', 'lastmod', 'person_count', 'sha', 'legislative_periods', 'statement_count', 'type'])


# pick a country
def get_country(country_name):
    for country in countries:
        if country['name'] == country_name:
            return country

aus = get_country('Australia')

# Select country legislature
aus_leg = aus['legislatures'][0]
aus_url = aus_leg['popolo_url']
aus_res = requests.get(aus_url)
aus_body = aus_res.json()

# Extract the name of one politician from that JSON response and save it in a variable.
person = aus_body['persons'][0]
# dict_keys(['birth_date', 'contact_details', 'family_name', 'gender', 'given_name', 'id', 'identifiers', 'links', 'name', 'sort_name'])

person_name = person['name']
print(person_name)
# De-Anne Kelly