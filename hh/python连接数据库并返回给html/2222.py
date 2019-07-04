# coding=utf-8
import requests
import json
import re


# 请求搜索列表数据
search = input('音乐名:')  # 控制台输入搜索关键词
pagesize = "10"  # 请求数目
url = 'https://songsearch.kugou.com/song_search_v2?callback=jQuery11240251602301830425_1548735800928&keyword=%s&page=1&pagesize=%s&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1548735800930' % (search, pagesize)
res = requests.get(url)  # 进行get请求

# 需要注意一点，返回的数据并不是真正的json格式，前后有那个多余字符串需要用正则表达式去掉,只要大括号{}包着的内容
# json.loads就是将json数据转为python字典的函数
res = json.loads(re.match(".*?({.*}).*", res.text, re.S).group(1))

list = res['data']['lists']  # 这个就是歌曲列表
print(list)

#建立List存放歌曲列表信息，将这个歌曲列表输出，别的程序就可以直接调用
musicList = []

#for循环遍历列表得到每首单曲的信息
for item in list:
    #将列表每项的item['FileHash'],item['AlnbumID']拼接请求url2
    url2 = 'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback=jQuery191010559973368921649_1548736071852&hash=%s&album_id=%s&_=1548736071853' % (
    item['FileHash'], item['AlbumID'])
    res2 = requests.get(url2)
#     res2 = json.loads(re.match(".*?({.*}).*", res2.text).group(1))['data']#同样需要用正则处理一下才为json格式,再转为字典
#
#     #打印一下
#     print (res2['song_name']+' - '+res2['author_name'])
#     print (res2['play_url'])
#     print ('')

    #将单曲信息存在一个字典里
    dict = {
        'author': res2['author_name'],
        'title': res2['song_name'],
        'id': int(res2['album_id']),
        'type': 'kugou',
        'pic': res2['img'],
        'url': res2['play_url'],
        'lrc': res2['lyrics']
    }

    #将字典添加到歌曲列表
    musicList.append(dict)