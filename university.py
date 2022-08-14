from tempfile import tempdir


def getAllUniversity():
    import os.path
    import json
    if (os.path.exists("university.json")):
        print("Load university.json");
        with open('university.json', 'r') as f:
            return json.load(f)
    else :
        import requests
        from bs4 import BeautifulSoup
        r = requests.get("https://www.4icu.org/jp/tokyo/a-z/");
        soup = BeautifulSoup(r.text, 'html.parser');
        temp = [];
        university = [];
        for uni in soup.find('tbody').find_all('tr'):
            temp.append(uni.find('a').text);
        for uni in temp:
            univ = getUniCoord(uni)
            if univ != "":
                university.append(univ);
        with open('university.json', 'w') as f:
            json.dump(university, f)
        return university;

def getUniCoord(adress):
    import requests
    import json
    long = 0;
    lat = 0;
    info = json.loads(requests.get("https://nominatim.openstreetmap.org/search?q=" + adress + ",Tokyo" + "&format=json").text);
    if len(info) > 0:
        long = info[0]['lon'];
        lat = info[0]['lat'];
    elif adress == "":
        long = 0;
        lat = 0;
    else:
        return "";
    return {"adress": adress, "long": float(long), "lat":float(lat)};