import array
from tkinter import N
from tkinter.messagebox import NO

class Chamber:
    price : int = 0;
    fee : int = 0;
    numberChamber : str = "";
    space : int = 0;
    sexeAvailable : str = "";
    asKey : bool = False;
    asDesk : bool = False;
    asChair : bool = False;
    asBed : bool = False;
    asClimatisation : bool = False;
    asPrivateBasin : bool = False;
    asTv : bool = False;
    asStorage: bool = False;
    asLan : bool = False;
    asPrivateKitchen : bool = False;
    asPrivateFridge : bool = False;
    asPrivateShower : bool = False;
    asPrivateToilet : bool = False;
    asSunaccess : bool = False;
    asSomethingMore: bool = False;
    Remarks : str = "";
    Requirement : str = "";
    Availablity : str = "";

    def __init__(self, chamber_soup):
        self.price = self.clean_price(chamber_soup.find('div', class_='value').text);
        self.fee = self.clean_price(chamber_soup.find('div', class_='price-row fee-area').find('div', class_='value').text);
        self.numberChamber = chamber_soup.find('div', class_='room-num').text.replace(',', '')
        self.get_space(chamber_soup);
        self.get_sexe(chamber_soup);
        self.asKey = chamber_soup.find('div', class_='icon key-on') != None;
        self.asDesk = chamber_soup.find('div', class_='icon desk-on') != None;
        self.asChair = chamber_soup.find('div', class_='icon chair-on') != None;
        self.asBed = chamber_soup.find('div', class_='icon bed-on') != None;
        self.asClimatisation = chamber_soup.find('div', class_='icon air_conditioner-on') != None;
        self.asPrivateBasin = chamber_soup.find('div', class_='icon basin-on') != None;
        self.asTv = chamber_soup.find('div', class_='icon tv-on') != None;
        self.asStorage = chamber_soup.find('div', class_='icon storage-on') != None;
        self.asLan = chamber_soup.find('div', class_='icon lan-on') != None;
        self.asPrivateKitchen = chamber_soup.find('div', class_='icon kitchen-on') != None;
        self.asPrivateFridge = chamber_soup.find('div', class_='icon refrigerator-on') != None;
        self.asPrivateShower = chamber_soup.find('div', class_='icon shower-on') != None;
        self.asPrivateToilet = chamber_soup.find('div', class_='icon toilet-on') != None;
        self.asSunaccess = chamber_soup.find('div', class_='icon sunshine-on') != None;
        self.asSomethingMore = chamber_soup.find('div', class_='icon other-on') != None;
        self.Remarks = chamber_soup.find('span', class_='remarks').text.replace('Remarks: ', '');
        self.Requirement = chamber_soup.find('span', class_='condition').text.replace('Requirement: ', '');
        self.Availablity = chamber_soup.find('div', class_='room-status-button-area').find('div')['class'][0].replace('btn', '').replace('_eng', '');

    def get_space(self, soup):
        place = soup.find('span', class_='width').text.replace('Space: ', '').replace(' ㎡', '').replace(' ', '');
        if place == "":
            self.space = 0;
        else:
            if "feet" in place:
                place = float(place.replace('feet', '')) / 3.28084;
            self.space = float(place);

    def get_sexe(self, soup):
        male = soup.find("div", class_="gender-icon male-1");
        female = soup.find("div", class_="gender-icon female-1");
        if (male != None and female != None):
            self.sexeAvailable = "Both"
        elif (male != None and female == None):
            self.sexeAvailable = "Male"
        elif (male == None and female != None):
            self.sexeAvailable = "Female"
        else:
            self.sexeAvailable = "None"

    def clean_price(self, str):
        if str == "-":
            return 0;
        return int(str.replace(',', '').replace('¥', '').replace('\\', '').replace(' ', '').replace('\n', '').replace('￥', ''));

    def writeToFile(self, csvFile, onlyAvailable, house):
        if (onlyAvailable == True and self.Availablity == "Available") or onlyAvailable == False:
            csvFile.write(str(self.numberChamber) + ',' + str(self.price) + ',' + str(self.fee) + ',' + str(self.space) + ',' + str(self.sexeAvailable) + ',' + str(self.Availablity) + ',' + str(self.asKey) + ',' + str(self.asDesk) + ',' + str(self.asChair) + ',' + str(self.asBed) + ',' + str(self.asClimatisation) + ',' + str(self.asPrivateBasin) + ',' + str(self.asTv) + ',' + str(self.asStorage) + ',' + str(self.asLan) + ',' + str(self.asPrivateKitchen) + ',' + str(self.asPrivateFridge) + ',' + str(self.asPrivateShower) + ',' + str(self.asPrivateToilet) + ',' + str(self.asSunaccess) + ',' + str(self.asSomethingMore) + ',' + str(house.id) + ',' + str(house.url) + ',' + str(house.Region) + ',' + str(house.houseName) + ',' + str(house.adress) + ',' + str(house.longetide) + ',' + str(house.latitude) + ',' + str(house.medianPrice) + ',' + str(house.medianFee) + ',' + str(house.NumberOfBed) + ',' + str(house.NbShower) + ',' + str(house.NbToilet) + ',' + str(house.NbBath) + ',' + str(house.NbKitchen) + ',')
            for university in house.university:
                csvFile.write(str(university['distance']) + ',')
            csvFile.write(str(house.Owner) + '\n')
