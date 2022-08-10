import array

class Chamber: 
    price : int = 0;
    fee : int = 0;
    number : int = 0;
    space : int = 0;
    sexeAvailable : array[str] = []
    asKey : bool = False;
    asDesk : bool = False;
    asChair : bool = False;
    asBed : bool = False;
    asClimatisation : bool = False;
    asPrivatetap : bool = False;
    asTv : bool = False;
    asWifi : bool = False;
    asPrivateKitchen : bool = False;
    asPrivateFridge : bool = False;
    asPrivateShower : bool = False;
    asPrivateToilet : bool = False;
    asSunaccess : bool = False;
    asSomethingMore: bool = False;
    Remarks : str = "";
    Requirement : str = "";
    isAvailable : bool = False;
