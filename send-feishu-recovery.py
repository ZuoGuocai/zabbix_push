#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author: zuoguocai@126.com
# Description:  Send Alarm Messages via FeiShu,
#               Need set sign in Robot Page

import json
import hashlib
import base64
import hmac
import time
import os 
import sys
import ast
import urllib3






userkey = sys.argv[1]
subject = sys.argv[2]
data = sys.argv[3]
# 把字符串转为字典
message  = ast.literal_eval(data)

HOSTNAME = ': '.join((' 告警主机',message["HOSTNAME"]))
HOSTIP = ': '.join(('告警地址',message["HOSTIP"]))
ITEMNAME = ': '.join(('监控项目',message["ITEMNAME"]))
ITEMLASTVALUE = ': '.join(('监控取值',message["ITEMLASTVALUE"]))
TRIGGERSEVERITY = ': '.join(('告警等级',message["TRIGGERSEVERITY"]))
TRIGGERSTATUS = ': '.join(('当前状态',message["TRIGGERSTATUS"]))
TRIGGERNAME = ': '.join(('告警信息',message["TRIGGERNAME"]))
EVENTTIME = ': '.join(('告警时间',message["EVENTTIME"]))
EVENTAGE = ': '.join(('持续时间',message["EVENTAGE"]))
EVENTID = ': '.join(('事件ID',message["EVENTID"]))


sendtext = '\n '.join((HOSTNAME,HOSTIP,ITEMNAME,ITEMLASTVALUE,TRIGGERSEVERITY,TRIGGERSTATUS,TRIGGERNAME,EVENTTIME,EVENTAGE,EVENTID))










secret = "dVEBsss"
timestamp = time.time()

def gen_sign(timestamp, secret):
  # 拼接timestamp和secret
  string_to_sign = '{}\n{}'.format(timestamp, secret)
  hmac_code = hmac.new(string_to_sign.encode("utf-8"), digestmod=hashlib.sha256).digest()
  
  # 对结果进行base64处理
  sign = base64.b64encode(hmac_code).decode('utf-8')
  
  return sign








#sign = gen_sign(timestamp,secret)
url = "https://open.feishu.cn/open-apis/bot/v2/hook/" + userkey
header ={"Content-Type": "application/json"}
            
data = {
    "timestamp": timestamp,
    "msg_type": "interactive",
    "card": {
        "config": {
                "wide_screen_mode": True,
                "enable_forward": True
        },
        "elements": [{
                "tag": "div",
                "text": {
                        "content": sendtext,
                        "tag": "lark_md"
                }
        }, {
                "actions": [{
                        "tag": "button",
                        "text": {
                                "content": "点我直达Zabbix :玫瑰:",
                                "tag": "lark_md"
                        },
                        "url": "https://zabbix.com",
                        "type": "default",
                        "value": {}
                }],
                "tag": "action"
        }],
        "header": {
                "title": {
                        "content": subject,
                        "tag": "plain_text"
                }
        }
    }
}

encoded_data = json.dumps(data).encode("utf-8")
http = urllib3.PoolManager()
result = http.request(
    "POST",
      url,
    body = encoded_data,
    headers = {
        'content-type':'application/json;charset=UTF-8'
    }
)
   
print(result)
