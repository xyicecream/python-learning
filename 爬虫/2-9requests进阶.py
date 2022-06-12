#1. 模拟用户登录 处理cookie
# 登录 -> 返回cookie
# 带着cookie去请求到书架url -> 书架上的内容
# 必须把上面的两个操作连起来
# 我们可以使用session进行请求，-> session是一连串的请求，在这个过程中的cookie不会丢失
import requests

# # 会话
# session = requests.session()
# data = {"loginName": "15950840896",
# "password": "tianhappy77"}

# #1.登录
# url = "https://passport.17k.com/ck/user/login"

# resp = session.post(url,data = data )
# #print(resp.text)

# # 2. 拿书架上的数据
# #刚才的session是有cookie的
# resp2 = session.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919")
# print(resp2.json())

# 2. 防盗链 抓取梨视频
# 拿到contID 
# 拿到videostatus返回的json. -> srcurl
# 对scrurl进行修整
# 拿到视频真正的下载路径进行下载
url = "https://www.pearvideo.com/video_1764805"
contID = url.split("_")[1]
videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contID}&mrd=0.2935074990858819"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
         # 防盗链：溯源，本次请求的上一级
         "Referer":url
}
resp = requests.get(videoStatusUrl,headers = headers)
dic = resp.json()
srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']
srcUrl = srcUrl.replace(systemTime,f"cont-{contID}")
#print(srcUrl)
# 下载视频
with open("a.mp4", mode = "wb") as f:
    f.write(requests.get(srcUrl).content)
f.close()