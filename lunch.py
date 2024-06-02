from bs4 import BeautifulSoup
import requests
import datetime
import re
now= datetime.datetime.now()
pattern = r'\([^)]*\)'
di = {}
def lunchs():
    url = 'https://hyoyang.goeic.kr/meal/calendar.do?menuId=9562&year=%s&month=%s' % (now.year, now.month)
    req = requests.get(url, verify=False)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    for a in soup.select('div[class=dayBox]'):
        # a.get_text().strip()
        # cleanr = re.compile('<.*?>')
        # cleantext = re.sub(cleanr, '', str(a))
        ass = a.select('div[class=lunch] a')
        if not ass:
            dayt = a.select('div[class=dayBox] span')
            dayt = str(dayt).replace('[<span>','')
            dayt = str(dayt).replace('</span>]','')
            # print(str(dayt))
            di[dayt] = 'its empty'
            # print()
        else:
            oa = str(ass).split('ㆍ')
            del oa[0]
            k = oa[-1].split('"')
            del k[1]
            oa[-1] = k[0]
            print(oa)
            dayt = a.select('div[class=dayBox] span')
            dayt = str(dayt).replace('[<span>','')
            dayt = str(dayt).replace('</span>]','')
            # print(str(dayt))
            di[dayt] = oa
    print(di)
return di
