from requests import get
import json
from celery import Celery

def extract_people_names(url):
    # Load JSON data
    res = get(url.strip())
    data = res.json()

    # Extract first_name and last_name from each person
    people_data = data.get('people', [])
    if people_data:
        first_name = people_data[0].get('first_name', '')
        last_name = people_data[0].get('last_name', '')
        name = first_name +last_name
    else:
        name = "N/A"
    return name


with open('link_file/compnay_details_urls.txt', 'r', encoding='utf-8') as file:
    urls = file.readlines()

company_data = {}
for url in urls:
    res = get(url.strip())
    data = res.json()
    company_data['organization'] = data.get('name')
    company_data['name'] = extract_people_names(url)
    print(company_data)

