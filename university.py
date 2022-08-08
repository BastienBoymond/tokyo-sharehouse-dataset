def getAllUniversity():
    import os.path
    if (os.path.exists("university.txt")):
        file = open("university.txt", "r");
        university = file.read().split(",");
        file.close();
        return university;
    else :
        import requests
        from bs4 import BeautifulSoup
        r = requests.get("https://www.4icu.org/jp/tokyo/a-z/");
        soup = BeautifulSoup(r.text, 'html.parser');
        university = [];
        for uni in soup.find('tbody').find_all('tr'):
            university.append(uni.find('a').text);
        file = open("university.txt", "w");
        file.write(",".join(university));
        file.close();
        return university;
