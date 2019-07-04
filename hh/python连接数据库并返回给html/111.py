import urllib.request
import re
import json
search = input('音乐名:')  # 控制台输入搜索关键词
pagesize = "10"  # 请求数目
url = 'https://songsearch.kugou.com/song_search_v2?callback=jQuery11240251602301830425_1548735800928&keyword=%s&page=1&pagesize=%s&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1548735800930' % (search, pagesize)
# res = urllib.request.Request.get_full_url(url) # 进行get请求

response=urllib.request.urlopen(url,timeout=10)
html=response.read()  # 获取到页面的源代码
p=html.decode('utf-8')
print(p)
# res = re.findall('\"FileName\":\"([^\"]+)', p, re.I | re.M)
# res = json.loads(re.match(".*?({.*}).*", p ,re.S).group(1))
# musiclist=res['data']['lists']# 这个就是歌曲列表
# for i in musiclist:
#     print(i["FileHash"])
# for item in musiclist:
#     #将列表每项的item['FileHash'],item['AlnbumID']拼接请求url2
#     url2 = 'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback=jQuery191010559973368921649_1548736071852&hash=%s&album_id=%s&_=1548736071853' % (
#     item['FileHash'], item['AlbumID'])
#     res2 = urllib.request.get(url2)
#     res2 = json.loads(re.match(".*?({.*}).*", res2.text).group(1))['data']  # 同样需要用正则处理一下才为json格式,再转为字典
# # print(mp)
#  #将单曲信息存在一个字典里
#     dict = {
#         'author': res2['author_name'],
#         'title': res2['song_name'],
#         'id': int(res2['album_id']),
#         'type': 'kugou',
#         'pic': res2['img'],
#         'url': res2['play_url'],
#         'lrc': res2['lyrics']
#     }
#
#     #将字典添加到歌曲列表
#     musicList.append(dict)
# print(type(p))
# print(type(res))
# print(len(res))