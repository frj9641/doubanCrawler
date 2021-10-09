import os
# 导入requests库
import random
import time

import requests
# 导入文件操作库
import codecs
from bs4 import BeautifulSoup

# 给请求指定一个请求头来模拟chrome浏览器
global headers
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0',
           'cookie': 'bid=G1z9gVzLXHs; ap_v=0,6.0; __utma=30149280.997487087.1633758875.1633758875.1633760958.2; __utmc=30149280;'
                     ' __utmz=30149280.1633758875.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); dbcl2="163850451:mA1bAeuSsp4"; '
                     'ck=GldF; __utmb=30149280.4.10.1633760958; push_noty_num=0; push_doumail_num=0; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1633761212%2C%22https%3A%2F%2Fmovie.douban.com%2Fsubject%2F26100958%2Fcomments%3Fpercent_type%3Dh%26start%3D40%26limit%3D20%26status%3DP%26sort%3Dnew_score%22%5D;'
                     ' _pk_id.100001.8cb4=a2a46eee1a70cbe4.1633761212.1.1633761229.1633761212.; _pk_ses.100001.8cb4=*; __utmt=1; __utmv=30149280.16385'}
server = 'https://movie.douban.com/subject/34605404/comments'
# 定义存储位置
global save_path
save_path = os.getcwd() + "\\Text\\" + 'jojo6.txt'
global page_max
# 好评
page_max = 20
global comments
comments = ''


# 获取短评内容
def get_comments(page):
    time.sleep(random.random() * 3)
    req = requests.get(url=page, headers=headers)
    html = req.content
    html_doc = str(html, 'utf-8')
    bf = BeautifulSoup(html_doc, 'html.parser')
    comment = bf.find_all(class_="short")
    for short in comment:
        print(short)
        global comments
        comments = comments + short.text + "\n\n\n"
# 写入文件
def write_txt(chapter, content, code):
    with codecs.open(chapter, 'a', encoding=code) as f:
        f.write(content)


# 主方法
def main():
    for i in range(0, page_max):
        try:
            print(i)
            page = server + '?start=' + str(i * 20) + '&limit=20&sort=new_score&status=F'
            get_comments(page)
            write_txt(save_path, comments, 'utf8')
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
