####################
# My_First_Img_Scrapper
#####################

from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image

import requests
import os

#making search loopable

def StartSearch():
    #create a new directory based of searches
    search = input("Search for: ")
    parms = {"q": search}
    #make a dir with the name of search
    dir_name = search.replace(" ", "_").lower()

    #need to add os lib to make a dir
        #first check if the dir exists already
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
    #req based of the search
    r = requests.get("http://www.bing.com/images/search", params= parms)

    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.findAll("a", {"class": "thumb"})

    for item in links:
        try:
            img_obj = requests.get(item.attrs["href"])
            #parsing the attrs of href split at the end
            print("Getting", item.attrs["href"])
            title = item.attrs["href"].split("/")[-1]
        except:
            print("Could not get image")
        try:
            img = Image.open(BytesIO(img_obj.content))
            img.save("./" + dir_name + "/" + title, img.format)
        except:
            print("Could Not Save Image")
    StartSearch()

StartSearch()