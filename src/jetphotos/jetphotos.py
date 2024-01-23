import os
import random
import requests
from bs4 import BeautifulSoup
import ctypes

def get_full_image(url):
    html2 = requests.get(url).text
    html2_data = BeautifulSoup(html2,"html.parser")
    value = html2_data.find("img", class_="large-photo__img").get("srcset")
    return value

def get_picture_links(url,lenlimit=99999):
    html = requests.get(url).text

    html_data = BeautifulSoup(html, "html.parser")
    l = []
    Dlist = html_data.find_all("a", class_="result__photoLink")
    i = 1
    for item in Dlist:
        if i>lenlimit:
            break
        val = "https://www.jetphotos.com"+item.get("href")
        value = val
        l.append(value)
        i+=1
    return l

def get_picture(url,sort="newest"):
    return get_pictures(url,sort=sort,count=1)[0]

def get_pictures(url, sort = "newest", count = 1):
    if sort=="newest":
        llim=count
    else:
        llim=10000000

    l=get_picture_links(url,lenlimit=llim)
    r = []
    for i in range (0,count):
        if len(l) == 0:
            break
        else:
            if sort == "random":
                val = random.choice(l)
                r.append(get_full_image(val))
                l.remove(val)
            elif sort == "newest":
                val = l[0]
                r.append(get_full_image(val))
                l.remove(val)
            elif sort == "oldest":
                val = l[len(l)-1]
                r.append(get_full_image(val))
                l.remove(val)
    return r

def download_image(link,path):
    response = requests.get(link)
    with open(path, "wb") as file:
        file.write(response.content)


print(get_full_image("https://www.jetphotos.com/photo/11202798"))