import requests
import main

def postRedirect(url):
    r = requests.post(url=url, allow_redirects=True, data=main.dataGen(20))
    if r.url != url:
        print("Redirected")

