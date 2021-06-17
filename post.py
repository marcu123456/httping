import requests
import main

def postSend(url):
    r = requests.post(url=url, allow_redirects=False, data=main.dataGen(20))
    if r.status_code == "404":
        print("URL not found")
    else:
        print("URL found")
