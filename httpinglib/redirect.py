import requests
import main

def postRedirect(url):
    r = requests.post(url=url, allow_redirects=True, data=main.dataGen(20))
    if r.status_code == "404":
        print("URL not found")
        exit(0)       
    else:
        if r.url != url:
            print("Redirected")
