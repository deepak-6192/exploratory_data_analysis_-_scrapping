import pandas as pd 
import numpy as np 
import requests
import matplotlib.pyplot as plt
import seaborn as sns 
from bs4 import BeautifulSoup

url = 'https://www.cricbuzz.com/cricket-stats/icc-rankings/men/batting'
agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
page = requests.get(url,headers=agent).text
soup = BeautifulSoup(page,'lxml')

player_name = []
player_country = []
player_rank = []
player_rating = []

for i in range(0,98):
    player_name.append(soup.find_all('a',class_= "text-hvr-underline text-bold cb-font-16")[i].text)
    player_country.append(soup.find_all('div',class_= "cb-font-12 text-gray")[i].text)
    player_rank.append(soup.find_all('div',class_= "cb-col cb-col-16 cb-rank-tbl cb-font-16")[i].text)
    player_rating.append(soup.find_all('div',class_= "cb-col cb-col-17 cb-rank-tbl pull-right")[i].text)

df =pd.DataFrame({"player_rank":player_rank,"player_name":player_name,"player_country":player_country,"player_rating":player_rating})

df.to_excel('testmatch_ranking.xlsx')
