import requests
import argparse
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = 'https://dashboard.cpolar.com'
LOGIN_URL = urljoin(BASE_URL, '/login')
STATUS_URL = urljoin(BASE_URL, '/status')

# USERNAME = 'mixinju123@163.com'
# PASSWORD = '7758521MXJ'
USERNAME = '2597035903@qq.com'
PASSWORD = '11111111'
# csrf_token = '1538662349.68##b5aa35f374452a6198004dab20d88b13583c7c2c'

parser = argparse.ArgumentParser(description='ssh remote hostname')
parser.add_argument("-r", action="store_true", help="choose cpolar hostname")
args = parser.parse_args()

session = requests.Session()

response_login =  session.post(LOGIN_URL, data={
	'login': USERNAME,
	'password': PASSWORD,
	# 'scrf_token': csrf_token
})

response_status = session.get(STATUS_URL)
# print(resp)  #结果：<Response [200]>
resp_text = response_status.text
# print(resp_text)
text = BeautifulSoup(resp_text, 'html.parser')

tunnels = []
tables = text.select("tr")
for td in tables:
	if(td.text.find("310") != -1):
		lines = td.text.splitlines()
		tunnel = "Host lab"
		if (lines[1] == "ntu310-1"):
			tunnel += "1\n"
		else:
			tunnel += "2\n"
		tunnel += "  HostName " + lines[2].split(':')[1][2:] + "\n"
		tunnel += "  User lei\n"
		tunnel += "  Port " + lines[2].split(':')[2] + "\n"
		if args.r:
			tunnels.append(tunnel)

if args.r == False:
	tunnel = "Host lab1\n"
	tunnel += "  HostName 10.80.15.186\n"
	tunnel += "  User lei\n"
	tunnel += "  Port 7758\n"
	tunnels.append(tunnel)

	tunnel = "host lab2\n"
	tunnel += "  hostname 10.80.15.186\n"
	tunnel += "  user lei\n"
	tunnel += "  port 7759\n"
	tunnels.append(tunnel)

# tunnel = "host lab2\n"
# tunnel += "  HostName 192.168.31.171\n"
# tunnel += "  User lei\n"
# tunnel += "  Port 22\n"
# tunnels.append(tunnel)

# tunnel = "Host lab2\n"
# tunnel += "  HostName 192.168.31.171\n"
# tunnel += "  User lei\n"
# tunnel += "  Port 22\n"
# tunnels.append(tunnel)
# print(tunnels)	
# print(len(tables))
# print(tables)

# res = tunnels
# for table in tables:
# 	for tr in table.find_all("tr"):
# 		for td in tr.find_all("td"):
# 			print(td.get_text())

# print(resp.text) #拿到页面源代码
response_status.close()  #关掉resp

with open('C:\\Users\\lei\\.ssh\\config', 'w') as f:
    for tunnel in tunnels:
        print(tunnel, file=f)


# import requests

# cookies = session.cookies
# print('Cookies: ', cookies)
# print('cookies\' type', type(cookies))

# response_status = session.get(STATUS_URL, cookies=cookies)
# print('Response Status: ', response_status.status_code)
# print('Response URL: ', response_status.url)


# url = 'https://dashboard.cpolar.com/status'
# headers = {
# 	'authority':'dashboard.cpolar.com',
# 	'method':'GET',
# 	'path':'/status',
# 	'scheme':'https',
# 	'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
# 	'accept-encoding':'gzip, deflate, br',
# 	'accept-language':'zh-CN,zh;q=0.9',
# 	'cookie':'_ga=GA1.2.1087364690.1664327971; session=fcf121d1-18d1-4590-988d-7f37654c1c21; _gid=GA1.2.1194350729.1664618732; Hm_lvt_0838dad5461d14f63bdf207a43a54c29=1664327971,1664618614,1664618773,1664619770; _gat_gtag_UA_128397857_1=1; Hm_lpvt_0838dad5461d14f63bdf207a43a54c29=1664676662',
# 	'pragma':'no-cache',
# 	'referer':'https://dashboard.cpolar.com/get-started',
# 	'sec-ch-ua':'"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
# 	'sec-ch-ua-mobile':'?0',
# 	'sec-ch-ua-platform':'Windows',
# 	'sec-fetch-dest':'document',
# 	'sec-fetch-mode':'navigate',
# 	'sec-fetch-site':'same-origin',
# 	'sec-fetch-user':'?1',
# 	'upgrade-insecure-requests':'1',
# 	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
# }