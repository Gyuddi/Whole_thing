import re
import requests
from bs4 import BeautifulSoup

def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
    "Accept-Language": "ko-KR,ko"}
    res = requests.get(url,headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_weather():
    url= "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)
    today_t = soup.find("span",attrs={"class":"todaytemp"}).get_text()
    today_imf = soup.find("p",attrs={"class":"cast_txt"}).get_text()
    minn = soup.find("span",attrs={"class":"min"}).get_text()
    maxi = soup.find("span",attrs={"class":"max"}).get_text()
    morning_rain_rate = soup.find("span",attrs={"class":"rain_rate wet"}).get_text()
    afternoon_rain_rate =  soup.find("span",attrs={"class":"rain_rate"}).get_text()
    dust = soup.find("dl",attrs = {"class":"indicator"})
    pm10 = dust.find_all("dd")[0].get_text()
    pm25 = dust.find_all("dd")[1].get_text()
    print("[오늘의 날씨]")
    print(today_imf)
    print("현재",today_t,"℃","(최저 {} / 최고 {})".format(minn,maxi))
    print("오전{} / 오후 강수확률 {}".format(morning_rain_rate,afternoon_rain_rate))
    print("미세먼지 {}".format(pm10))
    print("초미세먼지 {}".format(pm25))

def scrape_headline_news():
    print("[오늘의 뉴스]")
    url = "https://news.naver.com/"
    soup = create_soup(url)
    headline_titles = soup.find("ul",attrs={"class":"hdline_article_list"}).find_all("li",limit=3)
    for index,headline in enumerate(headline_titles):
        headline_title = headline.find("div",attrs={"class":"hdline_article_tit"}).get_text().strip()
        headline_link = headline.find("div",attrs={"class":"hdline_article_tit"}).find("a")["href"]
        print(index+1,headline_title)
        print("링크:",url+headline_link)

def scrape_kospi():
    print("오늘의 거래 TOP 종목")
    url = "https://finance.naver.com/main/main.nhn"
    soup = create_soup(url)
    top_kospi = soup.find("tbody",attrs={"id":"_topItems1"}).find_all("tr")
    for index,stock in enumerate(top_kospi):
        stock_name = stock.find("th").get_text()
        stock_per = stock.find_all("td")[2].get_text()
        print("종목 이름:",stock_name,"       등락률",stock_per.strip())

def scrape_english():
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    E_sentences = soup.find_all("div",attrs = {"id":re.compile("^conv_kor_t")})
    todayK = soup.find_all("b",attrs = {"class":"conv_txtTitle"})[0].get_text()
    todayE = soup.find_all("b",attrs = {"class":"conv_txtTitle"})[1].get_text()
    print("-"*100)
    print("오늘의 영어 지문 =",todayE)
    for sentence in E_sentences[int(len(E_sentences)/2):]:
        print(sentence.get_text().strip())
    print("-"*100)
    print("오늘의 한글 지문 =",todayK)
    for sentence in E_sentences[:int(len(E_sentences)/2)]:
        print(sentence.get_text().strip())


    















scrape_weather()
scrape_headline_news()
scrape_kospi()
scrape_english()