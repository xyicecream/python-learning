
import requests
url = "https://movie.douban.com/j/chart/top_list"
#重新封装参数
param = {
    "type": 11,
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20}
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}
resp = requests.get(url= url,params=param,headers=header)
print(resp.json())
