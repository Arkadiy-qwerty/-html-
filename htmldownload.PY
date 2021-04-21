import requests
from bs4 import BeautifulSoup


name = input()
URL = input()
HEADERS = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36', 'accept' : '*/*'}

res = requests.get(URL, headers = HEADERS)

f = open(name, "w+", encoding = 'utf-8')

print(f.write(res.text)) 
