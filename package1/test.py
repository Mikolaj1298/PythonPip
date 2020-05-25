import api_service


res = api_service.get_author(3,"xhADh8FO4czFdIeHo8UIsbegTWeTPQSLeUUGVh6E")

for item in res:
    item.showResource()