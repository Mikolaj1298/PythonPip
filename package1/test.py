import api_service


res = api_service.get_page(3,"xhADh8FO4czFdIeHo8UIsbegTWeTPQSLeUUGVh6E", 2)

for item in res:
    item.showResource()