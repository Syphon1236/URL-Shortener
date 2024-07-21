
# Made By Alexey Strilets




#requests

import requests

def shortenlink(full_link, link_name):
    API_Key = '9e6bfcf8c10ae147ebf4f9e7fbb3d658ce920'
    Base_URL = 'https://cutt.ly/api/api.php'

    payload = {'key': API_Key, 'short': full_link, 'name':link_name}
    request = requests.get(Base_URL, params=payload)
    data = request.json()

    print('')

    try:
        title = data['url']['title']
        short_link = data['url']['shortLink']
        print('Title', title)
        print('URL', short_link)
    except:
        status = data['url']['status']
        print('Error Status:', status)

shortenlink('https://www.google.com/search?q=sasiski&sca_esv=3672c068e7112759&sca_upv=1&rlz=1C1RXQR_enCA1082CA1082&udm=2&biw=1280&bih=601&sxsrf=ADLYWILuWjKLmxVxOG6w33enF8BxpDy81Q%3A1721520149937&ei=FVCcZvT6OMi3ptQP2diZuAw&ved=0ahUKEwi02Yqo6raHAxXIm4kEHVlsBscQ4dUDCBA&uact=5&oq=sasiski&gs_lp=Egxnd3Mtd2l6LXNlcnAiB3Nhc2lza2kyBRAAGIAESOUHUK0CWJwGcAF4AJABAJgBQ6ABtAGqAQEzuAEDyAEA-AEBmAIDoAK4AcICBBAjGCfCAgcQABiABBgYwgIJEAAYgAQYGBgKmAMAiAYBkgcBM6AHzQY&sclient=gws-wiz-serp#vhid=G7adr4RfvWy-KM&vssid=mosaic', 'mixjamlodinisa')