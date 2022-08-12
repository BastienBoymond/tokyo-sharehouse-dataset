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
        while i <= region["nb_pages"]:
            soup = return_soup(url + '/page:' + str(i))
            htmlcontent = soup.find_all('div', class_='lineupRight')
            for html in htmlcontent:
                if html.find('div', class_='contact-button-area').find('a').text == 'Available' or html.find('div', class_='contact-button-area').find('a').text == 'Available Soon':
                    newHouse = ShareHouse(int(''.join(x for x in  html.find('a')['href'] if x.isdigit())),"https://tokyosharehouse.com/" + html.find('a')['href'], self.allUniversity, region['name']);
                    self.allHouses.append(newHouse);
            i += 1;
