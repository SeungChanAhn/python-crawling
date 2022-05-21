from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
import re
import csv

start = 1
result_df = pd.DataFrame()
# 키워드 입력
keyword = input('검색하고싶은 키워드 >> ')
encoded_keyword = urllib.parse.quote(keyword)

# 날짜 입력
start_date = input('시작 날짜 >> ')
end_date = input('끝나는 날짜 >> ')

# 데이터 얻기
while True:
    try:
        url = 'https://search.naver.com/search.naver?&where=news&query='+encoded_keyword+'&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=3&ds='+start_date+'&de='+end_date+'&docid=&nso=so:r,a:all&mynews=0&cluster_rank=91&start={}&refresh_start=0'.format(start)
        headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15',
          'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        news_title = [title['title'] for title in soup.find_all('a', attrs={'class':'news_tit'})] # 기사 제목
        
        news_url = [ url['href'] for url in soup.find_all('a', attrs={'class':'news_tit'}) ] # 기사 url
        
        dates = [ date.get_text() for date in soup.find_all('span', attrs={'class':'info'})] # 기사 작성일
        news_date = []
        for date in dates:
            if re.search(r'\d+.\d+.\d+.', date) != None: # 기사 작성일 정제
                news_date.append(date)
        
        df = pd.DataFrame({'기사작성일':news_date,'기사제목':news_title,'기사주소':news_url})
        result_df = pd.concat([result_df, df], ignore_index=True)
        start += 10

# 오류발생시 몇 페이지까지 크롤링했는지 page 확인하기.
    except:  
        print(start)
        break

# csv파일로 저장하기.
result_df.to_csv("/Users/chan/Desktop/test2.csv", header=True, index=True)