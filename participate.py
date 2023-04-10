import requests
import threading
import time
import pandas as pd
import random

def register1(mail, proxy):
    url = 'https://www.fnacspectacles.com/campaign/jeux-olympiques-paris-2024?tx_rcageventimform_eventimformular%5Baction%5D=checkparticipation&tx_rcageventimform_eventimformular%5Bcontroller%5D=Form&type=8985416574&cHash=c07555b30df5c27bab93b78555ce234c'

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': '*/*',
    'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://www.fnacspectacles.com',
    'Referer': 'https://www.fnacspectacles.com/campaign/jeux-olympiques-paris-2024',
    }

    data = {
    'email': mail,
    'answer': 'undefined',
    'form': "tx_rcageventimform_eventimformular%255Bform%255D%255B__identity%255D%3D1085%26tx_rcageventimform_eventimformular%255B__referrer%255D%255B%2540extension%255D%3DRcagEventimform%26tx_rcageventimform_eventimformular%255B__referrer%255D%255B%2540controller%255D%3DForm%26tx_rcageventimform_eventimformular%255B__referrer%255D%255B%2540action%255D%3Dshowform%26tx_rcageventimform_eventimformular%255B__referrer%255D%255Barguments%255D%3DYTowOnt929b4362cb62f5fb059f7ca7fa8e616be89c8c1c5%26tx_rcageventimform_eventimformular%255B__referrer%255D%255B%2540request%255D%3D%257B%2522%2540extension%2522%253A%2522RcagEventimform%2522%252C%2522%2540controller%2522%253A%2522Form%2522%252C%2522%2540action%2522%253A%2522showform%2522%257D209737f172882f22b7c2f7a1c4f5234ed8c334cc%26tx_rcageventimform_eventimformular%255B__trustedProperties%255D%3D%257B%2522participation%2522%253A1%252C%2522javascript%2522%253A1%252C%2522form%2522%253A%257B%2522email%2522%253A1%252C%2522__identity%2522%253A1%257D%257Dd7b34854af1631c15a1bd5993abbb6e5aacc583b%26tx_rcageventimform_eventimformular%255Bparticipation%255D%3D0%26tx_rcageventimform_eventimformular%255Bjavascript%255D%3Dtrue%26tx_rcageventimform_eventimformular%255Bform%255D%255Bemail%255D%3Dazelrmkjamzelkrj%2540gmail.com%26tx_rcageventimform_eventimformular%255Bform%255D%255Bformfields%255D%255Bfield10832%255D%255Bconditionsgenerales%255D%3DJ%25E2%2580%2599accepte%2520les%2520conditions%2520du%2520jeu%2520concours.%26tx_rcageventimform_eventimformular%255Bform%255D%255Bformfields%255D%255Bfield10835%255D%255Bnewsletter%255D%3DJe%2520souhaite%2520recevoir%2520les%2520informations%2520li%25C3%25A9es%2520aux%2520futurs%2520jeux%2520concours%2520Paris%25202024%2520et%2520aux%2520actualit%25C3%25A9s%2520li%25C3%25A9es%2520%25C3%25A0%2520nos%2520%25C3%25A9v%25C3%25A9nements%2520culturels."
    }

    response = requests.post(url, headers=headers, data=data)

    print(response.text) 

def register2(mail, proxy):
    url = 'https://www.fnacspectacles.com/campaign/jeux-olympiques-paris-2024/campaign/jeux-olympiques-paris-2024?tx_rcageventimform_eventimformular%5Baction%5D=preparedata&tx_rcageventimform_eventimformular%5Bcontroller%5D=Form&cHash=f854c21bc4736f3da19f180d3fd1baf4'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'multipart/form-data; boundary=---------------------------425541188442653252263092477815',
    'Origin': 'https://www.fnacspectacles.com',
    'Dnt': '1',
    'Referer': 'https://www.fnacspectacles.com/campaign/jeux-olympiques-paris-2024',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Te': 'trailers'
    }

    data = {
    'tx_rcageventimform_eventimformular[form][__identity]': '1085',
    'tx_rcageventimform_eventimformular[action]': 'preparedata',
    'tx_rcageventimform_eventimformular[controller]': 'Form',
    'cHash': 'f854c21bc4736f3da19f180d3fd1baf4',
    'tx_rcageventimform_eventimformular[__referrer][@extension]': 'RcagEventimform',
    'tx_rcageventimform_eventimformular[__referrer][@controller]': 'Form',
    'tx_rcageventimform_eventimformular[__referrer][@action]': 'showform',
    'tx_rcageventimform_eventimformular[__referrer][arguments]': 'YTowOnt929b4362cb62f5fb059f7ca7fa8e616be89c8c1c5',
    'tx_rcageventimform_eventimformular[__referrer][@request]': '{"@extension":"RcagEventimform","@controller":"Form","@action":"showform"}209737f172882f22b7c2f7a1c4f5234ed8c334cc',
    'tx_rcageventimform_eventimformular[__trustedProperties]': '{"participation":1,"javascript":1,"form":{"email":1,"__identity":1}}d7b34854af1631c15a1bd5993abbb6e5aacc583b',
    'tx_rcageventimform_eventimformular[participation]': '0',
    'tx_rcageventimform_eventimformular[javascript]': 'true',
    'tx_rcageventimform_eventimformular[form][email]': mail,
    'tx_rcageventimform_eventimformular[form][formfields][field10832][conditionsgenerales]': 'J\'accepte les conditions du jeu concours.',
    'tx_rcageventimform_eventimformular[form][formfields][field10835][newsletter]': 'Je souhaite recevoir les informations liÃ©es aux futurs jeux concours Paris 2024 et aux actualitÃ©s liÃ©es Ã  nos Ã©vÃ©nements culturels.'
    }

    response = requests.post(url, headers=headers, data=data, proxies=proxy, allow_redirects=False)
    print(response)
    print(response.headers)
    print(response.text)


def send(mail, proxy):
    print(1)
    register1(mail, proxy)
    time.sleep(1) 
    print(2)
    register2(mail, proxy)


def getProxy():
    df = pd.read_csv('proxies.txt', sep=':')
    proxy = df.loc[random.randint(0, len(df) - 1)]
    proxies = { 'http' : f'http://{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}',
                'https' : f'http://{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}' } 
    #print(f'proxy used = {proxies}')
    return proxies


if __name__ == '__main__':
    with open("fnac_mail.txt", "r") as f:
        mails = f.readlines()
    threads = []
    for mail in mails:
        proxy = getProxy()
        print(mail)
        t = threading.Thread(target=send, args=(mail, proxy))
        threads.append(t)
        t.start()
        time.sleep(3) 