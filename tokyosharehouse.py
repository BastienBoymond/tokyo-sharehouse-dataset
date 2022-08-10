from region import Region
from house import ShareHouse
from request_and_scrap import return_soup

class TokyoShareHouse:
    url = 'https://tokyosharehouse.com/eng/area'
    allregions = []
    allUniversity = []
    allHouses = []

    def __init__(self, university):
        self.allUniversity = university;
        region = Region();
        self.allregions = region.get_regions();
        for region in self.allregions:
            self.getAllHouses(region);
    
    def getAllHouses(self, region):
        url = self.url + '/search/' + str(region['id']);
        i = 1
        print(region["name"] + " " + str(region["nb_pages"]) + ' pages');
        while i <= region["nb_pages"]:
            soup = return_soup(url + '/page:' + str(i))
            htmlcontent = soup.find_all('div', class_='lineupRight')
            for html in htmlcontent:
                newHouse = ShareHouse("https://tokyosharehouse.com/" + html.find('a')['href'], self.allUniversity, region['name']);
                self.allHouses.append(newHouse);
                print(html.find('a')['href']);
            print(i);
            i += 1;
