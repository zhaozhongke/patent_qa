from re import search
import numpy as np
import pandas as pd
import requests
import json
# import urllib.parse
from requests.utils import requote_uri


proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'https://127.0.0.1:7890'
}
cert_path = 'cacert.pem'

base_url = ""
# test_url= "https://developer.uspto.gov/ibd-api/v1/application/publications?searchText=nose%20cover&start=0&rows=100&largeTextSearchFlag=N&api_key=mwVGnhDAq6v0k0nupQXETJx9oZLyErl3"
# test_url= "https://developer.uspto.gov/ibd-api/v1/application/publications?searchText=remote%20diagnostic%20approaches&start=0&rows=100&largeTextSearchFlag=N&api_key=mwVGnhDAq6v0k0nupQXETJx9oZLyErl3"

api_key = "mwVGnhDAq6v0k0nupQXETJx9oZLyErl3"

# response=requests.get(test_url)
# json_data = response.json()

# search_terms = ['memory cache', 'system cache', 'CLPC', '' ]
# search_terms = ['variable refresh rate', 'closed loop performance', 'video image stabilization' ,'image fusion','long-exposure image fusion']
search_terms = ['image fusion']
# search_terms = ['image noise reduction']

# search_terms = ['image noise reduction']


# test_url= f'https://developer.uspto.gov/ibd-api/v1/application/publications?searchText={search_term}&start=0&rows=100&largeTextSearchFlag=N&api_key={api_key}'
results_count=0

import ssl

url = 'https://developer.uspto.gov'
ssl_context = ssl.create_default_context(cafile=cert_path)

for search_term in search_terms:
    print(search_term)

    # print(urllib.parse.quote("http://www.sample.com/"))
    test_urls=requote_uri(f'https://developer.uspto.gov/ibd-api/v1/application/publications?abstractText={search_term}&assigneeEntityName=Apple&start=0&rows=100&largeTextSearchFlag=N&api_key={api_key}')

    # test_url= urllib.parse.quote(f'https://developer.uspto.gov/ibd-api/v1/application/publications?searchText={search_term}&start=0&rows=100&largeTextSearchFlag=N&api_key={api_key}')
       
    print(test_urls)

    # response=requests.get(test_urls,stream=True,  proxies= {'https':'127.0.0.1:7890'}) 
    response=requests.get(test_urls,  verify=False) 
    json_data = response.json()
    
    
    patent_info_list = []
    for data in json_data['results']:
        if data is None:
            print('--------------------------------------------------------------')
            print('The search term: {search_term} did not produce any results')
            print('--------------------------------------------------------------')
        else:
            results_count=+1
            patent_dict={}
            # print(f'this is the json response data: {data}')
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
            # convert abstract from list to string
            for abstract_list in data['abstractText']:
                abstract_string = ''.join(abstract_list)
                print(f'abstract string: {abstract_string}')
            patent_dict['abstract'] = abstract_string
            patent_dict['search_term']=search_term
            patent_dict['descriptionText'] = data['descriptionText']

            
            claims = data['claimText']
            patent_dict['claim_text'] = claims
            patent_dict['description_text'] = data['descriptionText']
        patent_info_list.append(patent_dict)

        

    # print(f'this is the patent info {results_count} list: {patent_info_list}')

df=pd.DataFrame(patent_info_list)
# print(df)
df.to_csv('patent_api_demo_.csv')




# print(data['results'][0]['publicationDocumentIdentifier'])