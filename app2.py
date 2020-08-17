# 기관매매
import requests as rq
from bs4 import BeautifulSoup

sosoks = ['01', '02']    # 01: 코스피, 02: 코스닥
types = ['buy', 'sell']  # buy: 매수, sell: 매도

sosok_map = {
  '01': '코스피',
  '02': '코스닥'
}

URL = "https://finance.naver.com/sise/sise_deal_rank_iframe.nhn?sosok=%s&investor_gubun=1000&type=%s"
headers = {}

for sosok in sosoks:

  for t in types:
    res = rq.get(URL%(sosok, t), headers=headers)
    soup = BeautifulSoup(res.content, 'lxml')

    rows = soup.select('.box_type_ms tr')
    print('===== %s-%s ====='%(sosok_map[sosok], t))
    for row in rows:
      columns = row.select('td')
      if len(columns) == 4:
        print('종목명: %s, 수량: %s, 금액: %s, 당일거래량: %s'%(columns[0].text, columns[1].text, columns[2].text, columns[3].text))
