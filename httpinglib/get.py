import requests
import main

def getSend(url):
    r = requests.get(url=url, allow_redirects=False)
    if r.status_code == "404":
        print("URL not found")
    else:
        print("URL found")
