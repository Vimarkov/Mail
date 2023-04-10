import burp_requests
import pandas as pd
import random
import threading
import time

def getProxy():
    df = pd.read_csv('proxies.txt', sep=':')
    proxy = df.loc[random.randint(0, len(df) - 1)]
    proxies = { 'http' : f'http://{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}',
                'https' : f'http://{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}' } 
    #print(f'proxy used = {proxies}')
    return proxies

def check_mail(yc, yses, yp, yj, mail, proxy):
    proxy = getProxy()
    mail = mail.strip("\n")
    scrap = burp_requests.scrap_mail(yc, yses, yp, yj, mail, proxy) 


if __name__ == '__main__':
    with open("mail.txt", "r") as f:
        mails = f.readlines()

    proxy = getProxy()
    yc, yses = burp_requests.get_cookies(proxy)
    yp = burp_requests.get_yp(yc, yses, proxy)
    #compte = burp_requests.connect(yc, yses, yp, mail)
    yj = burp_requests.get_yj(yc, yses, proxy)
    threads = []
    for mail in mails:
        t = threading.Thread(target=check_mail, args=(yc, yses, yp, yj, mail, proxy))
        threads.append(t)
        t.start()