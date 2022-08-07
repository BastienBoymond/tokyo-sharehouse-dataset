from pydoc import pager
from region import Region

class TokyoShareHouse:
    url = 'https://tokyosharehouse.com/eng/area'
    allregions = []


    def __init__(self):
        region = Region();
        self.allregions = region.get_regions();
        for region in self.allregions:
            self.getAllHouses(region);
    
    def getAllHouses(self, region):
        url = self.url + '/search/' + str(region['id']);
        print(region["name"] + " " + str(region["nb_pages"]) + ' pages');
