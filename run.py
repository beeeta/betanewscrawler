"""
first crawler title and url then parse keywords and desc
"""
import requests
import random
from pyquery import PyQuery as pq
import re
import datetime


from .web.dao import getSession,CsdnGeek

USER_AGENTS = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
               'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0',
               'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0',
               ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) '
                'Chrome/19.0.1084.46 Safari/536.5'),
               ('Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46'
                'Safari/536.5'), )

URLS=["http://geek.csdn.net/hot"]
VERIFY_SSL_CERTIFICATE = False;

def _getBeforeNSecondsTime(secs):
    timecount = datetime.datetime.timestamp(datetime.datetime.now()) - secs
    timeobj = datetime.datetime.fromtimestamp(timecount)
    return timeobj.strftime("%Y-%m-%d %H:%M")


"""
get timestamp from time string
"""
def _parseTime(timeString):
    rec = re.compile(r'(\d+)小时前')
    res = rec.match(timeString)
    if res:
        hour = res.group(1)
        return _getBeforeNSecondsTime(float(hour)*60*60)
    else:
        rec = re.compile(r'(\d+)分钟前')
        res = rec.match(timeString)
        if res:
            min = res.group(1)
            return _getBeforeNSecondsTime(float(min) * 60)
        else:
            rec = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}')
            res = rec.match(timeString)
            if res:
                return timeString


def _get_url(urls):
    for url in urls:
        page = requests.get(url,headers={"User-Agent":random.choice(USER_AGENTS)},verify=VERIFY_SSL_CERTIFICATE).text
        page = pq(page)
        dd = page("#geek_list dd") # span.tracking-ad a.title
        dd.each(_colItems)

def _colItems(i,ele):
    # print(ele)
    ele = pq(ele)
    atag = ele('span.tracking-ad a.title')
    url = atag.attr('href')
    title = atag.text()
    createTime = _parseTime(ele('ul li').eq(1).text())
    geek = CsdnGeek(refurl=url,title=title,createTime=createTime)
    session = getSession()
    session.add(geek)
    session.commit()
    print('url: %s ctx: %s timeraw: %s' % (url,title,createTime))

if __name__ == '__main__':
    _get_url(URLS)