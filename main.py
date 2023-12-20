import requests

proxies = None #uncomment the lines below if you have proxies and delete this line.

"""
proxies = {
  "https": "",
  "http": ""
}
only if you have proxies!
"""

webh = "webhook goes here"

while True:
    url = 'https://api.discord.gx.games/v1/direct-fulfillment'
    headers = {
        'authority': 'api.discord.gx.games',
        'accept': '*/*',
        'accept-language': 'en-US, en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://www.opera.com',
        'referer': 'https://www.opera.com/',
        'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0'
    }

    data = {
        'partnerUserId': 'bc385c68-be5f-43c2-9713-cb2051fef65b'
    }
    response = requests.post(url, headers=headers, json=data, proxies=proxies)

    byte = response.json()["token"]
    data = {
        "content": f"https://discord.com/billing/partner-promotions/1180231712274387115/{byte}"
    }
    requests.post(webh, data=data)
    print(f"https://discord.com/billing/partner-promotions/1180231712274387115/{byte}")
#made by spottedpanther
