import requests
from bs4 import BeautifulSoup
import re
import random

def get_cookies(proxy): 
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Dnt': '1',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Te': 'trailers',
    'Connection': 'close'
    }

    response = requests.get('https://yopmail.com/', headers=headers, proxies=proxy, allow_redirects=False)
    cookies = response.cookies
    print(response)
    print(response.headers) 
    print(response.text)
    yc = cookies["yc"]
    yses = cookies['yses']

    return yc, yses


def get_yp(yc, yses, proxy):
    url = 'https://yopmail.com/fr/'
    headers = {
    'Host': 'yopmail.com',
    'Cookie': 'yc='+ yc +'; yses='+ yses +';  _r=0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Dnt': '1',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Te': 'trailers',
    'Connection': 'close'
}
    response = requests.get(url, headers=headers, proxies=proxy)
    soup = BeautifulSoup(response.text, 'html.parser')
    value = soup.find('input', {'id': 'yp'}).get('value')

    return value

def get_yj(yc, yses, proxy):
    url = 'https://yopmail.com/ver/7.4/webmail.js'
    headers = {
    'Host': 'yopmail.com',
    'Cookie': 'yc='+ yc +'; yses='+ yses +'; ycons=oBiJUZhRqTghDYupF+tsf7HgukUCQz66EAUi4b98IEg',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': '*/*',
    'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Dnt': '1',
    'Referer': 'https://yopmail.com/fr/',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-origin',
    'Te': 'trailers',
    'Connection': 'close'
    }

    response = requests.get(url, headers=headers, proxies=proxy)
    match = re.search(r'&yj=(.*?)&v=', response.text)
    if match:
        code = match.group(1)
    return code

def connect(yc, yses, yp, mail, proxy):
    url = 'https://yopmail.com/fr/'
    headers = {
    'Host': 'yopmail.com',
    'Cookie': 'yc='+ yc +'; yses='+ yses +'; ytime=10:41',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://yopmail.com',
    'Dnt': '1',
    'Referer': 'https://yopmail.com/fr/',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Te': 'trailers',
    'Connection': 'close'
    }
    data = {'yp': yp, 'login': mail}

    response = requests.post(url, headers=headers, data=data, proxies=proxy)
    cookies = response.cookies
    compte = cookies["compte"]

    return compte

def scrap_mail(yc, yses, yp, yj, mail, proxy):
    url = 'https://yopmail.com/fr/inbox?login='+ mail +'&p=1&d=&ctrl=&yp='+ yp +'&yj='+ yj +'&v=7.4&r_c=&id='

    headers = {
    'Host': 'yopmail.com',
    'Cookie': 'yc='+ yc +'; yses='+ yses +'; ycons=/VJN9mIAXfnfXx9w84Bz7QMnDpsVLdbplmdl2xx4IMPx6eVPWAD2O/ofXY+HoJjO; ytime=10:42; compte='+ mail +'; ywm=' + mail,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Dnt': '1',
    'Referer': 'https://yopmail.com/fr/wm',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'iframe',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Te': 'trailers',
    'Connection': 'close'
        }

    response = requests.get(url, headers=headers, proxies=proxy)

    if len(response.text) <= 1000:
        print(mail + "@yopmail.com : No new mail!")
    else:
        print(mail + "@yopmail.com : NEW MAIL !")
    #print(response.text)
    
    return(len(response.text))