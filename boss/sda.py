import requests
import parsel
import csv

url = "https://sou.zhaopin.com/?jl=551&p=1"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/109.0.0.0 '
                  'Safari/537.36 '
}
request = requests.get(url=url, headers=headers)
# 获取网页信息
# print(request)
selector = parsel.Selector(request.text)
print(selector)
