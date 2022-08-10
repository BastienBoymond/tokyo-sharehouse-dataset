import array
from chamber import Chamber
from request_and_scrap import return_soup

class ShareHouse:
    url : str = "";
    university : array = [];
    Chamber : array = []
    priceAverage : int = 0;
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
        print(rightDetailList[0])

        


