import array
from chamber import Chamber
from request_and_scrap import return_soup

class ShareHouse:
    url : str = "";
    university : array = [];
    Chamber : array = []
    medianPrice : int = 0;
    FeeAverage : int = 0;
    NumberOfBed : int = 0;
    adress: str = "";
    longetide : float = 0;
    latitude : float = 0;
    Region : str = "";
    NbShower : int = 0;
    NbToilet : int = 0;
    NbBath : int = 0;
    AsLan : bool = False;
    Washing: str = "";
    NbKitchen : int = 0;
    Owner : str = "";

    def __init__(self, url, university, regionName):
        self.url = url;
        self.university = university;
        self.Region = regionName;
        soup = return_soup(self.url);
        rightDetailList = soup.find('table', class_='detailListArea').find_all('tr')
        self.adress = rightDetailList[0].find('div', class_='labelDesc').text
        print(rightDetailList[1].find('div', class_='month clearfix').text);
        self.medianPrice = self.get_median_price(rightDetailList[1].find('div', class_='month clearfix').text)
        print(self.medianPrice);

    def get_median_price(self, text):
        text = text.replace(',', '');
        text = text.replace('\\', '');
        text = text.replace(' ', '');
        text = text.replace('permonth', '');
        if "~" in text:
            two_number = text.split('~');
            print(two_number);
            return int((int(two_number[0]) + int(two_number[1])) / 2);
        else:
            return int(text);


        


