from bs4 import BeautifulSoup
import requests
import datetime
import re
now= datetime.datetime.now()
pattern = r'\([^)]*\)'
def lunchs():
    b=1
    di = {}
    while b <31:
        url = 'https://hyoyang.goeic.kr/meal/view.do?menuId=9562&year=%s&month=%s&day=%s' % (now.year, now.month, b)
        req = requests.get(url, verify=False)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        if soup.select('td')[0].get_text().strip() == '식단이 없습니다.':
            di[b] = '오늘 중식은 없습니다'
        else:
            a = soup.select('td')[2]
            # print(a)
            a = a.select('span')[0].get_text().strip()
            # print("dfs"+a)
            # a = str.replace("\"", "")
            z = re.sub(pattern=pattern, repl='', string=a)
            oa = z.split('ㆍ')
            del oa[0]
            di[b] = oa
        b=b+1
    print(di)
    return di
def tolunchs():
    b = 1
    di = {}
    while b < 31:
        url = 'https://hyoyang.goeic.kr/meal/view.do?menuId=9562&year=%s&month=%s&day=%s' % (now.year, now.month, b)
        req = requests.get(url, verify=False)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        try:
            if soup.select('td')[6].get_text().strip() == '식단이 없습니다.':
                di[b] = '오늘 석식은 없습니다'
            elif soup.select('td')[6] =='':
                'd'
            else:
                a = soup.select('td')[6]
                # print(a)
                a = a.select('span')[0].get_text().strip()
                # print("dfs" + a)
                # a = str.replace("\"", "")
                z = re.sub(pattern=pattern, repl='', string=a)
                oa = z.split('ㆍ')
                del oa[0]
                di[b] = oa
        except:
            pass
        b = b + 1
    return di
