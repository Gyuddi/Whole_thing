import requests
from bs4 import BeautifulSoup

url = "https://search.shopping.naver.com/search/all?query=%EC%84%B8%EC%9D%B4%EC%BD%94+%EC%8B%9C%EA%B3%84&bt=1&frm=NVSCVUI"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

#cartoons =soup.find_all("td", attrs = {"class":"title"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title)
# print("https://comic.naver.com"+link)
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com"+cartoon.a["href"]
#     print(title, link)

#평점구하기
totla_price= 0
prices = soup.find_all("span", attrs={"class":"price_num__2WUXn"})
for price in prices:
    rate = price.get_text()
    print(rate)
    rate = rate.replace(",","")
    totla_price += float(rate[:-1])
print("전체점수:",totla_price)
print("평균점수:",totla_price/len(prices))