class Region:
    url = 'https://tokyosharehouse.com/eng/'
    region = []

    def __init__(self):
        import os.path
        if os.path.exists('region.json'):
            self.region = self.load_region()
        else:
            self.get_all_region()
            self.save_region()

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
        r = requests.get(self.url + "area/")
        soup = BeautifulSoup(r.text, 'html.parser')
        for area in soup.find_all('div', class_='ar'):
            if area.find('a') is None:
                continue;
            place = {'id':int(''.join(x for x in area.find('a')['href'] if x.isdigit())), 'link':area.find('a')['href'], 'name':area.find('a').text};
            if self.check_if_region_exist(place['id']):
                continue;
            self.region.append(place);
        self.region.sort(key=lambda x: x['id']);
    
    def  check_if_region_exist(self, region_id):
        for region in self.region:
            if region["id"] == region_id:
                return True;
        return False;

    def get_regions(self):
        return self.region;