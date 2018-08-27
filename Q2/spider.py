# -*- coding: UTF-8 -*-
import requests
import json
import datetime

# 获取开始时间与结束时间
now_datetime_structs = datetime.datetime.now()
end_date = now_datetime_structs.strftime('%Y-%m-%d')
begin_datetime_structs = now_datetime_structs + datetime.timedelta(days=-365*2)
begin_date =begin_datetime_structs.strftime('%Y-%m-%d')

# 公共header头
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie':'UniqueID=aBrqeaQ65bN9ZMqa1535104903680; Sites=_21; 21_vq=1; _ga=GA1.3.1228963736.1535104904; _gid=GA1.3.835856889.1535104904',
    'Host': 'www.cwl.gov.cn',
    'Referer': 'http://www.cwl.gov.cn/kjxx/ssq/kjgg/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'
}

# 获取总页数
count_url = 'http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=ssq&issueCount=&issueStart=&issueEnd=&dayStart='+begin_date+'&dayEnd='+end_date+'&pageNo='
r = requests.get(url=count_url, headers=headers, timeout=3)
data_dict = json.loads(r.text)
page_count = data_dict['pageCount']

# 获取数据
result = []
for i in range(0,page_count):
    page_no = i+1
    url = 'http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=ssq&issueCount=&issueStart=&issueEnd=&dayStart='+begin_date+'&dayEnd='+end_date+'&pageNo=' + str(page_no)
    r = requests.get(url=url, headers=headers, timeout=3)
    data_dict = json.loads(r.text)
    result.append(data_dict['result'])

# 写入文件
f = open('D:\data.txt','a',encoding='utf-8')
f.write(json.dumps(result))

print('success')
