# -*- coding : utf-8 -*-
# @File : main.py
# @Author : Leonard
# @Time : 2022/01/10 15:25:14


# 第三方库导入
import requests
import re
import csv

# 头部文件
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
    AppleWebKit/537.36 (KHTML, like Gecko)\
    Chrome/97.0.4692.71 Safari/537.36"}

# 获取十页网页信息
for i in range(10):
    url = "https://movie.douban.com/top250?start="+str(i*25)+"&filter="

    html_response = requests.get(url, headers=header)

    html_content = html_response.text

    # 解析数据
    obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                     r'</span>.*?<p class="">.*?<br>(?P<year>.*?)'
                     r'&nbsp.*?<span class="rating_num" property="v:average">(?P<score>.*?)'
                     r'</span>.*?<span class="inq">(?P<item>.*?)</span>', re.S)
    result = obj.finditer(html_content)

    file = open("data.csv", mode='a', encoding="UTF-8")
    writer = csv.writer(file)

    for it in result:
        # print(it.group("name"))
        # print(it.group("year").strip())
        # print(it.group("score"))
        # print(it.group("item"))
        dict = it.groupdict()
        dict["year"] = dict["year"].strip()
        writer.writerow(dict.values())

    file.close()

print("豆瓣电影TOP250信息获取完成!")
