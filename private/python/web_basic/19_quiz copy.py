# [출력 결과]
# [출력 결과]
# =========== 매물 1 ===========
# 거래 : 매매
# 면적 : 84/59 (공급/전용)
# 가격 : 165,000 (만원)
# 동 : 214동
# 층 : 고/23
# =========== 매물 2 ===========
#    ...

import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&DA=UME&t__nil_searchbox=suggest&sug=&sugo=15&sq=%EC%86%A1%ED%8C%8C+%ED%97%AC&o=1&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

aparts = soup.find("table",attrs = {"class":"tbl"}).find("tbody").find_all("tr")

for index,apart in enumerate(aparts):
    deal = apart.find_all("td")[0].get_text()
    area = apart.find_all("td")[1].get_text()
    price = apart.find_all("td")[2].get_text()
    dong = apart.find_all("td")[3].get_text()
    floor = apart.find_all("td")[4].get_text()
    print("="*20,"매물",index+1,"="*20)
    print(deal,area,price,dong,floor)

