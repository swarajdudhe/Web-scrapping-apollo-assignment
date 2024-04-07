from requests import get

pages = {}

letters = 'abcde'
for letter in letters:
    base_url = f'https://discovery-api.apollo.io/api/v1/discovery/modality/organizations/page_letters/{letter}/pages'
    res = get(base_url)
    data = res.json()

    pages[letter] = data.get('page_count')
    print(f'{letter} is scrapped')

print(pages)