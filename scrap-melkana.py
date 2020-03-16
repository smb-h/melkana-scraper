import requests
from bs4 import BeautifulSoup
import json
import lxml


url = "https://api.kilid.com/api/listing/search/portal/v2.0?page=1&sort=kilid,DESC"

# payload = "{\"locations\":[{\"type\":\"city\",\"locationId\":\"2301021576\"}],\"subType\":\"buy\",\"type\":\"listing\",\"page\":\"4\",\"sort\":\"kilid,DESC\"}"
payload = '{"locations":[{"type":"city","locationId":"2301021576"}],"subType":"buy","type":"listing","page":"1","sort":"kilid,DESC"}'
headers = {
  'Content-Type': 'application/json',
  'origin': 'https://kilid.com',
  'referer': 'https://kilid.com/buy/tehran?locations=c_2301021576&subType=buy&type=listing&sort=kilid,DESC',
}

rs = []
saved_data = []

# Crawl
for i in range(100):
    # response = requests.request("POST", url, headers=headers, data = payload.format(i))
    response = requests.request("POST", "https://api.kilid.com/api/listing/search/portal/v2.0?page=" + str(i) + "&sort=kilid,DESC", headers=headers, data = '{"locations":[{"type":"city","locationId":"2301021576"}],"subType":"buy","type":"listing","page":"' + str(i) + '","sort":"kilid,DESC"}')
    # print(response.text.encode('utf8'))
    # content = response.content
    # content = response.json
    # content = response.text
    content = response.json().get("content", False)
    # print(content)
    for home in content:
        if home.get("id", False):
            if home.get("id", False) not in saved_data:
                saved_data.append(home.get("id", False))
                rs.append({
                    "floorArea": str(home.get("floorArea", False)),
                    "sector": str(home.get("location", False).get("sector", False).get("name", False)),
                    "url": "https://kilid.com/buy/detail/" + str(home.get("id", False)),
                    })


# Result
for home in rs:
    print(home)


