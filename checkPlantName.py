
from bs4 import BeautifulSoup
import requests

def find_plant(genus,species):
    search_url = "http://www.theplantlist.org/tpl1.1/search?q="
    key1,key2 = genus,species
    search = search_url + key1 + "+" + key2

    content = requests.get(search).content
    soup = BeautifulSoup(content, "lxml")

    accepted = soup.find_all("td" , class_ = "name Accepted")
    result = [ i.text for i in accepted]
    if result ==[]:
        return False
    else:
        return True

