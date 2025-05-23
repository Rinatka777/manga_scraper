from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import os

def create_dir(path):# create a path for a file 
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print("Error")

def get_all_urls(main_url):
    #Fetch the pages HTML
    resp = requests.get(main_url)
    #if ok, soup with html parser
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
    else:
       print("Error")
       exit()

    #pick only ul ul li a 
    anchors = soup.select("div#Chapters_List ul ul li a")

    #Normalize URLs (make them absolute)
    urls = []
    for a in anchors:
        raw_href = a["href"]
        full_url = urljoin(main_url, raw_href)
        print(raw_href,"->", full_url)
        urls.append(full_url)
    
    return urls

def download_images(img_urls, folder):
    create_dir(folder)

