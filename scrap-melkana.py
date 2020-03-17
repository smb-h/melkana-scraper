import requests
from bs4 import BeautifulSoup
import json
import lxml


base_url = "https://www.melkana.com/"
# url = "https://www.melkana.com/v3/home/load-more"
url = "https://www.melkana.com/v3/home/load-more?filters%5Bsort%5D%5Btitle%5D=%D8%AC%D8%AF%DB%8C%D8%AF%D8%AA%D8%B1%DB%8C%D9%86+%D9%87%D8%A7&filters%5Bsort%5D%5Bmodel%5D=approve_time&filters%5Bsort%5D%5Border%5D=desc&filters%5Bdeal_type%5D=0&filters%5Bdeal_type_mobile%5D=0&filters%5Bhas_tour%5D=2&filters%5Bestate_type%5D=2&filters%5Bestate_document%5D=2&filters%5Bprice_analyse%5D=0&filters%5Bfeatures%5D%5B0%5D%5Bid%5D=1&filters%5Bfeatures%5D%5B0%5D%5Bname%5D=%D9%BE%D8%A7%D8%B1%DA%A9%DB%8C%D9%86%DA%AF&filters%5Bfeatures%5D%5B0%5D%5Btitle%5D=parking&filters%5Bfeatures%5D%5B0%5D%5Bstatus%5D=false&filters%5Bfeatures%5D%5B1%5D%5Bid%5D=2&filters%5Bfeatures%5D%5B1%5D%5Bname%5D=%D8%A7%D9%86%D8%A8%D8%A7%D8%B1%DB%8C&filters%5Bfeatures%5D%5B1%5D%5Btitle%5D=warehouse&filters%5Bfeatures%5D%5B1%5D%5Bstatus%5D=false&filters%5Bfeatures%5D%5B2%5D%5Bid%5D=3&filters%5Bfeatures%5D%5B2%5D%5Bname%5D=%D8%A2%D8%B3%D8%A7%D9%86%D8%B3%D9%88%D8%B1&filters%5Bfeatures%5D%5B2%5D%5Btitle%5D=elevator&filters%5Bfeatures%5D%5B2%5D%5Bstatus%5D=false&filters%5Bfeatures%5D%5B3%5D%5Bid%5D=4&filters%5Bfeatures%5D%5B3%5D%5Bname%5D=%D8%A8%D8%A7%D9%84%DA%A9%D9%86&filters%5Bfeatures%5D%5B3%5D%5Btitle%5D=balcony&filters%5Bfeatures%5D%5B3%5D%5Bstatus%5D=false&filters%5Bcenter%5D%5Blat%5D=35.73744828648759&filters%5Bcenter%5D%5Blng%5D=51.39876293182373&filters%5Bzoom%5D=12&filters%5Bfoundation%5D%5Bmin%5D=&filters%5Bfoundation%5D%5Bmax%5D=&filters%5Bfoundation%5D%5BminRange%5D=&filters%5Bfoundation%5D%5BmaxRange%5D=&filters%5Bprice_rent%5D%5Bmin%5D=&filters%5Bprice_rent%5D%5Bmax%5D=&filters%5Bprice_rent%5D%5BminRange%5D=&filters%5Bprice_rent%5D%5BmaxRange%5D=&filters%5Brahn%5D%5Bmin%5D=&filters%5Brahn%5D%5Bmax%5D=&filters%5Brahn%5D%5BminRange%5D=&filters%5Brahn%5D%5BmaxRange%5D=&filters%5Bprice%5D%5Bmin%5D=&filters%5Bprice%5D%5Bmax%5D=&filters%5Bprice%5D%5BminRange%5D=&filters%5Bprice%5D%5BmaxRange%5D=&filters%5Bestate_age%5D%5Bmin%5D=0&filters%5Bestate_age%5D%5Bmax%5D=40&filters%5Bestate_age%5D%5BminRange%5D=0&filters%5Bestate_age%5D%5BmaxRange%5D=40&filters%5Brooms%5D%5Bmin%5D=3&filters%5Brooms%5D%5Bmax%5D=3&filters%5Brooms%5D%5BminRange%5D=0&filters%5Brooms%5D%5BmaxRange%5D=5&filters%5Bestate_floor%5D%5Bmin%5D=-1&filters%5Bestate_floor%5D%5Bmax%5D=20&filters%5Bestate_floor%5D%5BminRange%5D=-1&filters%5Bestate_floor%5D%5BmaxRange%5D=20&filters%5Bbuilding_floors%5D%5Bmin%5D=1&filters%5Bbuilding_floors%5D%5Bmax%5D=20&filters%5Bbuilding_floors%5D%5BminRange%5D=1&filters%5Bbuilding_floors%5D%5BmaxRange%5D=20&filters%5Bfloor_units%5D%5Bmin%5D=1&filters%5Bfloor_units%5D%5Bmax%5D=10&filters%5Bfloor_units%5D%5BminRange%5D=1&filters%5Bfloor_units%5D%5BmaxRange%5D=10&filters%5BleftBottom%5D%5Blat%5D=35.713904233681035&filters%5BleftBottom%5D%5Blng%5D=51.22959136962891&filters%5BrightTop%5D%5Blat%5D=35.760721836547624&filters%5BrightTop%5D%5Blng%5D=51.568107604980476&filters%5Bpolygon%5D=&filters%5BeasyFilters%5D=&page="

# payload = "{filters[sort][title]: 'جدیدترین ها', filters[sort][model]: 'approve_time', filters[sort][order]: 'desc', filters[deal_type]: '0', filters[deal_type_mobile]: '0', filters[has_tour]: '2', filters[estate_type]: '2', filters[estate_document]: '2', filters[price_analyse]: '0', filters[features][0][id]: '1', filters[features][0][name]: 'پارکینگ', filters[features][0][title]: 'parking', filters[features][0][status]: 'false', filters[features][1][id]: '2', filters[features][1][name]: 'انباری', filters[features][1][title]: 'warehouse', filters[features][1][status]: 'false', filters[features][2][id]: '3', filters[features][2][name]: 'آسانسور', filters[features][2][title]: 'elevator', filters[features][2][status]: 'false', filters[features][3][id]: '4', filters[features][3][name]: 'بالکن', filters[features][3][title]: 'balcony', filters[features][3][status]: 'false', filters[center][lat]: '35.73744828648759', filters[center][lng]: '51.39876293182373', filters[zoom]: '12', filters[foundation][min]: '', filters[foundation][max]: '', filters[foundation][minRange]: '', filters[foundation][maxRange]: '', filters[price_rent][min]: '', filters[price_rent][max]: '', filters[price_rent][minRange]: '', filters[price_rent][maxRange]: '', filters[rahn][min]: '', filters[rahn][max]: '', filters[rahn][minRange]: '', filters[rahn][maxRange]: '', filters[price][min]: '', filters[price][max]: '', filters[price][minRange]: '', filters[price][maxRange]: '', filters[estate_age][min]: '0', filters[estate_age][max]: '40', filters[estate_age][minRange]: '0', filters[estate_age][maxRange]: '40', filters[rooms][min]: '3', filters[rooms][max]: '3', filters[rooms][minRange]: '0', filters[rooms][maxRange]: '5', filters[estate_floor][min]: '-1', filters[estate_floor][max]: '20', filters[estate_floor][minRange]: '-1', filters[estate_floor][maxRange]: '20', filters[building_floors][min]: '1', filters[building_floors][max]: '20', filters[building_floors][minRange]: '1', filters[building_floors][maxRange]: '20', filters[floor_units][min]: '1', filters[floor_units][max]: '10', filters[floor_units][minRange]: '1', filters[floor_units][maxRange]: '10', filters[leftBottom][lat]: '35.713904233681035', filters[leftBottom][lng]: '51.22959136962891', filters[rightTop][lat]: '35.760721836547624', filters[rightTop][lng]: '51.568107604980476', filters[polygon]: '', filters[easyFilters]: '', page: '2'}"
headers = {
	'Accept': '*/*',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Referer': 'https://www.melkana.com/',
}

rs = []
saved_data = []

# Crawl
for i in range(100):
	response = requests.request("POST", url + str(i), headers=headers)
	content = response.json()
	for home in content.get("estate_list", False):
	    if home.get("code", False):
	        if home.get("code", False) not in saved_data:
	            saved_data.append(home.get("code", False))
	            rs.append({
					"floorArea": str(home.get("foundation", False)),
					"sector": str(home.get("some_address", False)),
					"url": "https://www.melkana.com/estate/" + str(home.get("code", False)),
					})


# Result
for home in rs:
    print(home)


