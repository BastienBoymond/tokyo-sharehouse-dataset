def return_soup(url):
    import requests
    from bs4 import BeautifulSoup
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup
    else :
        return None
