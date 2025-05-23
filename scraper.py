from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import os

def create_dir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print("Error")

#def create_file(path):

def get_all_urls(main_url):
    # 1. Fetch the pages HTML
    resp = requests.get(main_url)
    #      – Sends an HTTP GET request to the given URL.  
    #      – Returns a Response object containing status code, headers, and content.  

    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
    else:
       print("Error")
       exit()

    # 3. Select only the chapter links
    anchors = soup.select("div#Chapters_List ul ul li a")
    #    • soup.select(css_selector)  
    #      – Finds all elements matching the CSS selector you provide.  
    #      – Here, "div#Chapters_List ul ul li a" drills down into the nested <ul>s to grab each <a>.  

    # 4. Normalize URLs (make them absolute)
    urls = []  # 1. Start with an empty list
    for a in anchors:  # 2. Loop over each <a> tag
        raw_href = a["href"]                # 3. Extract the href attribute
        full_url = urljoin(main_url, raw_href)  # 4. Make it absolute
        print(raw_href,"->", full_url)
        urls.append(full_url)               # 5. Add it to the list
    
    return urls

def download_images(img_urls, folder):
    create_dir(folder)
    
