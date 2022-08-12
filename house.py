import array
from chamber import Chamber
from request_and_scrap import return_soup

class ShareHouse:
    url : str = "";
    university : array = [];
    Chamber : array = []
    adress: str = "";
    houseName = "";
    medianPrice : int = 0;
    medianFee : int = 0;
    NumberOfBed : int = 0;
    longetide : float = 0;
    latitude : float = 0;
    Region : str = "";
    NbShower : int = 0;
    NbToilet : int = 0;
    NbBath : int = 0;
    AsLan : bool = False;
    NbKitchen : int = 0;
    Owner : str = "";

    def __init__(self, url, university, regionName):
        self.url = url;
        self.university = university;
        self.Region = regionName;
        soup = return_soup(self.url);
        self.houseName = soup.find('h1').text;
        rightDetailList = soup.find('table', class_='detailListArea').find_all('tr')
        self.adress = rightDetailList[0].find('div', class_='labelDesc').text
        self.medianPrice = self.get_median(rightDetailList[1].find('div', class_='month clearfix').text)
        self.medianFee =  self.get_median(rightDetailList[2].find('div', class_='labelDesc').text)
        self.NumberOfBed = int(''.join(x for x in rightDetailList[5].find('div', class_='labelDesc').text if x.isdigit()))
        self.get_coordinates(self.adress);
        self.get_public_space(soup.find('div', class_='facility').find_all('li'));
        self.create_every_chamber(return_soup("https://tokyosharehouse.com/" + soup.find('div', class_="room-link").find('a')['href']));
        print(self.Region, self.houseName, self.medianPrice, self.medianFee, self.NumberOfBed)

    def create_every_chambe(self, chambers_soup):
        return;


    def get_median(self, text):
        text = text.replace(',', '');
        text = text.replace('¥', '');
        text = text.replace('\\', '');
        text = text.replace(' ', '');
        text = text.replace('\n', '');
        text = text.replace('～', '~');
        text = text.replace('permonth', '');
        if "~" in text:
            two_number = text.split('~');
            return int((int(two_number[0]) + int(two_number[1])) / 2);
        else:
            if text == "-":
                return 0;
            return int(text);

    def get_coordinates(self, adress):
        import requests
        import json
        info = json.loads(requests.get("https://nominatim.openstreetmap.org/search?q=" + adress + "&format=json").text);
        print(adress, info)
        if len(info) > 0:
            self.longetide = info[0]['lon'];
            self.latitude = info[0]['lat'];
        elif adress == "":
            self.longetide = 0;
            self.latitude = 0;
        else:
            split = adress.split(',')[1:];
            adress = ','.join(split);
            return self.get_coordinates(adress);
        print(self.longetide, self.latitude)

    def get_public_space(self, facility):
        nbShower = ''.join(x for x in facility[7].find('div', class_="count") if x.isdigit());
        self.NbShower = int(nbShower) if nbShower != '' else 0;
        nbBath = ''.join(x for x in facility[8].find('div', class_="count") if x.isdigit());
        self.NbBath = int(nbBath) if nbBath != '' else 0;
        nbToilet = ''.join(x for x in facility[9].find('div', class_="count") if x.isdigit());
        self.NbToilet = int(nbToilet) if nbToilet != '' else 0;
        nbKitchen = ''.join(x for x in facility[10].find('div', class_="count") if x.isdigit());
        self.NbKitchen = int(nbKitchen) if nbKitchen != '' else 0;
        if facility[1].find('div', class_="icon kitchen-on") != None and self.NbKitchen == 0:
            self.NbKitchen = 1;
        self.AsLan = True if facility[4].find('div', class_="icon lan-on") != None else False;
        print(self.NbShower, self.NbBath, self.NbToilet, self.NbKitchen, self.AsLan)
            

