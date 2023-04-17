import requests
from bs4 import BeautifulSoup
import re
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
content = requests.get("https://acgsecrets.hk/bangumi/",headers=headers)
content.encoding = 'utf-8'
soup = BeautifulSoup(content.text,"html.parser")
allname = soup.find_all("div",attrs={"class":"entity_localized_name"})
allmakers = soup.find_all("div",attrs={"class":"anime_copyrightstring anime_summary"})
alltime = soup.find_all("div",attrs={"class":"anime_onair time_today"})
nowaminetime = soup.find_all("h1",attrs={"class":"with-top-margin"})
allhowmuch = soup.find_all("p",attrs={"class":"with-top-margin"})
for aminetime,howmuch in zip(nowaminetime ,allhowmuch):
    print(aminetime.string)
    print(howmuch.string)
for name, time ,maker, in zip(allname, alltime,allmakers,):
    print("amine_name:" + name.string)
    print("amine_maker:" + maker.string)
    print("anime_onair_time:" + time.string)
    print("----------------------------------------------------------------------------------------------------------")
while True:
    pass