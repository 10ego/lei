import requests

class LEI():
    def __init__(self):
        self.session = requests.session()
        
    def search_lei(self, company, country="CA"): #country is a 2 character country code. e.g. Canada = "CA"
        url = "https://api.gleif.org/api/v1/lei-records?filter%5Bentity.addresses.country%5D={}&filter%5Bfulltext%5D={}&page%5Bnumber%5D=1&page%5Bsize%5D=15".format(country.upper(), company)
        r = self.session.get(url)
        if r.status_code == 200:
            return r.status_code, r.json()
        else:
            return r.status_code, r.content
            
    def get_parent(self, lei):
        url = "https://api.gleif.org/api/v1/lei-records/{}/ultimate-parent".format(lei)
        r = self.session.get(url)
        if r.status_code == 200:
            return r.status_code, r.json()
        else:
            return r.status_code, r.content
        
    def get_children(self, lei, page=None):
        if page <= 1:
            url = "https://api.gleif.org/api/v1/lei-records/{}/ultimate-children".format(lei)
        else:
            url = "https://api.gleif.org/api/v1/lei-records/{}/ultimate-children?page[number]={}".format(lei, page)
        r = self.session.get(url)
        if r.status_code==200:
            return r.status_code, r.json()
        else:
            return r.status_code, r.content
        
    def get_children_recursive(self, lei):
        status, meta = self.get_children(self.session, lei)
        if status == 200:
            meta = meta['meta']
        pages = meta['pagination']['lastPage']
        children = []
        for i in range(pages):
            c_status, child = get_children(self.session, lei)
            if c_status == 200:
                for ids in child['data']
                    children.append(ids['id'])
            else:
                print(i, c_status)
        return children
    
