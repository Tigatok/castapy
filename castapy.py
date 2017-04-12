from bs4 import BeautifulSoup
import urllib2
import pandas as pd
from shutil import copyfile
wiki = "https://classifieds.castanet.net/search/?rent_ptype=88&rent_location=&re_neighborhood4=&re_neighborhood56=&re_neighborhood58=&other_city=457&minprice=1000&maxprice=3000&numbeds=4-0&numbaths=2-0&pet_friendly=&submit="
page = urllib2.urlopen(wiki)
soup = BeautifulSoup(page, 'lxml')
prods = soup.find_all('a', class_='prod_container')
A=[]
B=[]
for row in prods:
  cells = row.findAll('div', class_='descr')
  descrs = row.findAll('h2')
  prices = row.findAll('div', class_='price')
  A.append(descrs[0].find(text=True))
  B.append(prices[0].find(text=True))
df=pd.DataFrame(A,columns=['Descs'])
df['Price']=B
copyfile('new.txt', 'old.txt')
with open("new.txt", "w+") as f:
  df.to_string(f)
