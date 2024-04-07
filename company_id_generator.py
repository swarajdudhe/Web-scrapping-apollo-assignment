# from requests import get
# with open('Using_Flask/urls.txt','r') as file:
#     url_list = file.readlines()

# for url in url_list:
#     res = get(url.strip())
#     for company in res.json():
#         print(company.get('id'))

from requests import get

# Base URL for concatenation
base_url = "https://discovery-api.apollo.io/api/v1/discovery/modality/organizations/entity/"

with open('link_file/urls.txt','r') as file:
    url_list = file.readlines()

# List to store concatenated URLs
concatenated_urls = []

for url in url_list:
    res = get(url.strip())
    for company in res.json():
        company_id = company.get('id')
        concatenated_url = f"{base_url}{company_id}"
        concatenated_urls.append(concatenated_url)

# Write concatenated URLs to a text file
with open('link_file/compnay_details_urls.txt', 'w') as file:
    for url in concatenated_urls:
        file.write(f"{url}\n")
