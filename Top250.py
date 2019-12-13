# /usr/bin python3
# 爬取 豆瓣 top250电影
import requests
import re
from bs4 import BeautifulSoup

def get_text(url):
    # 使用代理
    # proxies = {
    #     "http": "127.0.0.1",
    #     "https": "127.0.0.1"
    # }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    # html_text = requests.get(url, headers=headers, proxies=proxies)
    html_text = requests.get(url, headers=headers)
    return html_text

def top(text): 

    global num

    soup = BeautifulSoup(text.text, 'html.parser')
    names = soup.find_all('div', class_='hd')
    scores = soup.find_all('span', class_='rating_num')
    movie_score = []
    movie_name = []
    # 得到电影评分
    for score in scores:
        movie_score.append(score.text)
    # 得到电影名称
    for name in names:
        movie_name.append(name.a.span.text)

    for i in range(0, 25):
        print(num, str(movie_name[i]) + '   评分:' + str(movie_score[i]))
        num += 1

if __name__ == '__main__':
    num = 1
    for each in range(0, 10):
        url = 'https://movie.douban.com/top250?start={0}&filter='.format(str(each * 25))
        top(get_text(url))
