
class Resource:
    def __init__(self, pk, title, entry_type, entry_type_id, partner,
                 scientific_domain, authors, co_creators, attachments_number,
                 highlight='', file_result=''):
        self.pk = pk
        self.title = title
        self.entry_type = entry_type
        self.entry_type_id = entry_type_id
        self.partner = partner
        self.scientific_domain = scientific_domain
        self.authors = []
        for i in range(len(authors)):
            author = [authors[i]['pk'], authors[i]['first_name'],
                      authors[i]['last_name']]
            self.authors.append(author)

        self.co_creators = []
        for i in range(len(co_creators)):
            co_creator = [co_creators[i]['pk'], co_creators[i]['full_name']]
            self.authors.append(co_creator)

        self.attachments_number = attachments_number
        self.highlight = highlight
        self.file_result = file_result

    def showResource(self):
        print(self.title)
        print(self.authors)
    

    