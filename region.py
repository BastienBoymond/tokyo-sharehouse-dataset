class Region:
    url = 'https://tokyosharehouse.com/eng/area/'
    region = []

    def __init__(self):
        import os.path
        if os.path.exists('region.json'):
            print("Load region.json");
            self.region = self.load_region()
        else:
            print("region.json not found, creating it");
            self.get_all_region()
            self.save_region()
            print("region.json created");

    def save_region(self):
        import json
        print(self.region);
        with open('region.json', 'w') as f:
            json.dump(self.region, f)

    def load_region(self):
        import json
        with open('region.json', 'r') as f:
            return json.load(f)
    
    def get_all_region(self):
        import requests
        from bs4 import BeautifulSoup
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, 'html.parser')
        for area in soup.find_all('div', class_='ar'):
            if area.find('a') is None:
                continue;
            if self.check_if_region_exist(int(''.join(x for x in area.find('a')['href'] if x.isdigit()))):
                continue;
            place = {'id':int(''.join(x for x in area.find('a')['href'] if x.isdigit())), 'link':area.find('a')['href'], 'name':area.find('a').text, 'nb_pages':self.get_nb_page(int(''.join(x for x in area.find('a')['href'] if x.isdigit())))};
            print("Place: " + place['name'] + " was finish to Scrap");
            self.region.append(place);
        self.region.sort(key=lambda x: x['id']);
    
    def  check_if_region_exist(self, region_id):
        for region in self.region:
            if region["id"] == region_id:
                return True;
        return False;

    def get_nb_page(self, region_id):
        url = self.url + 'search/' + str(region_id);
        import requests
        page  = 1;
        for i in range(1, 100):
            r = requests.get(url + '/page:' + str(i));
            if r.status_code != 200:
                break;
            page = i;
        return page;

    def get_regions(self):
        return self.region;
