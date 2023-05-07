import requests
import pandas as pd
from requests.utils import requote_uri

api_key = "mwVGnhDAq6v0k0nupQXETJx9oZLyErl3"

search_terms = ['image']

results_count = 0
patent_info_list = []

for search_term in search_terms:
    print(search_term)
    start = 0
    rows = 5
    has_more_results = True

    while has_more_results:
        test_urls = requote_uri(f'https://developer.uspto.gov/ibd-api/v1/application/publications?abstractText={search_term}&assigneeEntityName=Apple&start={start}&rows={rows}&largeTextSearchFlag=N&api_key={api_key}')
        print(test_urls)
        response = requests.get(test_urls, verify=False)
        json_data = response.json()

        if not json_data['results']:
            has_more_results = False
            break

        for data in json_data['results']:
            results_count += 1
            patent_dict = {}
            patent_dict['patent_number'] = data['patentApplicationNumber']
            patent_dict['application_#'] = data['patentApplicationNumber']
            patent_dict['invention_title'] = data['inventionTitle']
            patent_dict['category'] = data['inventionSubjectMatterCategory']
            patent_dict['filing_date'] = data['filingDate']
            patent_dict['grant_date'] = data['publicationDate']
            patent_dict['assignee'] = data['assigneeEntityName']
            patent_dict['assignee_location'] = data['assigneePostalAddressText']
            patent_dict['inventors'] = data['inventorNameArrayText']
            patent_dict['file_url'] = data['filelocationURI']
            patent_dict['archive_url'] = data['archiveURI']
            abstract_string = ''.join(data['abstractText'])
            patent_dict['abstract'] = abstract_string
            patent_dict['search_term'] = search_term
            patent_dict['descriptionText'] = data['descriptionText']
            patent_dict['claim_text'] = data['claimText']
            patent_dict['description_text'] = data['descriptionText']
            patent_info_list.append(patent_dict)
            print(patent_dict)

        start += rows

df = pd.DataFrame(patent_info_list)
df.to_csv('patent_api_demo_apple_image.csv')
