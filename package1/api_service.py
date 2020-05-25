import requests
import json
import time
import resource
from requests.exceptions import HTTPError


class Manager:
    def test(self):
        return "It actually test"

def get_author(entries, apiKey):
    try:
        response = requests.get('https://api.e-science.pl/api/azon/authors/entries/' + str(entries) + '/', headers={
            'X-Api-Key': apiKey
        })
        response.raise_for_status()
        json_data = response.json()
        results = json_data['results']
        resource_list = []

        for item in results:
            pk = item.get("pk")
            title = item.get("title")
            entry_type = item.get("entry_type")
            entry_type_id = item.get("entry_type_id")
            partner = item.get("partner")
            scientific_domain = item.get("scientific_domain")
            authors = item.get("authors")
            co_creators  = item.get("co_creators")
            attachments_number  = item.get("attachments_number")
            res = resource.Resource(pk, title, entry_type, entry_type_id, partner, scientific_domain,
             authors, co_creators, attachments_number)

            resource_list.append(res)
        return resource_list
    except HTTPError as http_err:
        print('HTTP error')
    
