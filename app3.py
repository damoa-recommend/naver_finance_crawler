# 프로그램매매동향
import requests as rq
from bs4 import BeautifulSoup

url = 'https://finance.naver.com'
path = '/sise/sise_program.nhn?sosok=01'
headers = {}

res = rq.get(url + path, headers=headers)
soup = BeautifulSoup(res.content, 'lxml')

iframe_by_time_url = url + soup.select('.box_type_m iframe')[0].get('src') + '&page=%d'
iframe_by_day_url = url + soup.select('.box_type_m2 iframe')[0].get('src') + '&page=%d'

def c(u):

  for page in range(1, 43):
    res = rq.get(u%(page))
    soup = BeautifulSoup(res.content, 'lxml')
    rows = soup.select('.type_1 tr')[2:]

    for row in rows:
      columns = row.select('td')
      if not len(columns) >= 9: continue

      print('날짜(시간): %s'%(columns[0].text))
      print('    차익거래-매수: %s, 차익거래-매도: %s, 차익거래-순매도: %s'%(columns[1].text, columns[2].text, columns[3].text))
      print('    비차익거래-매수: %s, 비차익거래-매도: %s, 비차익거래-순매도: %s'%(columns[4].text, columns[5].text, columns[6].text))
      print('    전체-매수: %s, 전체-매도: %s, 전체-순매도: %s'%(columns[7].text, columns[8].text, columns[9].text))

print('======= iframe_by_time_url ========')
c(iframe_by_time_url)

print('======= iframe_by_day_url ========')
c(iframe_by_day_url)