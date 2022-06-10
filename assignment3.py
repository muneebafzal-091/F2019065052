import requests
from bs4 import BeautifulSoup
url="https://go.drugbank.com/covid-19#drugs"
page=requests.get(url)
html=BeautifulSoup(page.content,"html.parser")
table=html.find_all('table')
Done=table[2].find_all('a')
Count=1
for i in Done:
  Count=Count+1
  print(i.text)
  if Count>10:
    break