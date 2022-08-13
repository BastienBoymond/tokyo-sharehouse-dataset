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
        self.number = chamber_soup.find('div', class_='room-num').text;
        self.space = float(chamber_soup.find('span', class_='width').text.replace('Space: ', '').replace(' ㎡', ''));
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
        print(self.price, self.fee, self.number, self.space, self.sexeAvailable, self.asKey, self.asDesk, self.asChair, self.asBed, self.asClimatisation, self.asPrivateBasin, self.asTv, self.asStorage, self.asLan, self.asPrivateKitchen, self.asPrivateFridge, self.asPrivateShower, self.asPrivateToilet, self.asSunaccess, self.asSomethingMore, self.Remarks, self.Requirement, self.Availablity);

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