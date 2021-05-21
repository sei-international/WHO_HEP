from googlesearch import search
import pandas as pd
import requests
import yaml
import urllib.parse as urlparse

def is_absolute(url):
    return bool(urlparse.urlparse(url).netloc)

def download_file(download_url, filename):
    url = download_url
    filename = filename + '.pdf'
    try:
        if is_absolute(url):
            r = requests.get(url, stream=True, verify=False)
            open(filename, 'wb').write(r.content)
    except:
        return 0

stream = open('Country_Domains', 'r')    # 'document.yaml' contains a single YAML document.
Country_Domains = yaml.safe_load(stream)

for c,l in Country_Domains.items():
    u = "Energy regulation PDF cooking heating " + " " +  c + " " + l
    i = 0
    for j in search(u, tld="com", num=10, stop=10, pause=2):
        if 'search' not in j and ('download' in j or 'pdf' in j):
            i = i + 1
            download_file(j, c + str(i))

