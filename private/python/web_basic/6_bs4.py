import requests
from bs4 import BeautifulSoup

url ="https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) #처음 발견되는 a
# print(soup.a.attrs)# a element의 속성
# print(soup.a["href"])# a element의 herf 속성 값

# print(soup.find(attrs = {"class":"Nbtn_upload"})) #특성을 통해 객채를 찾을 수 있다.
# rank1 = soup.find("li",attrs={"class":"rank01"})
# print(rank1.a.get_text())
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.get_text())
# print(rank1.parent)
# ranks = rank1.find_next_siblings("li")
# print(ranks)


webtoon = soup.find("a",text="외모지상주의")
print(webtoon)