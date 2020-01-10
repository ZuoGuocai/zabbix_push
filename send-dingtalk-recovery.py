#!/usr/bin/env python3
# Author: zuoguocai@126.com
# Function:  send alert message via dingtalk
import requests
import os
import sys
import logging
import json
import urllib3
import ast
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logging.basicConfig(filename = os.path.join(os.getcwd(), 'push.log'), level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')



subject = sys.argv[1]
data = sys.argv[2]
# 把字符串转为字典
message  = ast.literal_eval(data)

# 测试用
#filename = '/usr/lib/zabbix/alertscripts/1.txt'
#with open(filename, 'w') as file_object:
#    file_object.write(data)



HOSTNAME = ': '.join(('> 告警主机',message["HOSTNAME"]))
HOSTIP = ': '.join(('告警地址',message["HOSTIP"]))
ITEMNAME = ': '.join(('监控项目',message["ITEMNAME"]))
ITEMLASTVALUE = ': '.join(('监控取值',message["ITEMLASTVALUE"]))
TRIGGERSEVERITY = ': '.join(('告警等级',message["TRIGGERSEVERITY"]))
TRIGGERSTATUS = ': '.join(('当前状态',message["TRIGGERSTATUS"]))
TRIGGERNAME = ': '.join(('告警信息',message["TRIGGERNAME"]))
EVENTTIME = ': '.join(('告警时间',message["EVENTTIME"]))
EVENTAGE = ': '.join(('持续时间',message["EVENTAGE"]))
EVENTID = ': '.join(('事件ID',message["EVENTID"]))


sendtext = '\n\n >'.join((HOSTNAME,HOSTIP,ITEMNAME,ITEMLASTVALUE,TRIGGERSEVERITY,TRIGGERSTATUS,TRIGGERNAME,EVENTTIME,EVENTAGE,EVENTID))

def send_dingtalk_message(sendtext):
    logger = logging.getLogger(__name__)
    DINGDING_API_URL="https://oapi.dingtalk.com/robot/send?access_token=x"
    data = {
        'msgtype': 'markdown',
        "markdown": {
            "title": ":-) 恢复通知",
            "text": ''.join(('## <font color=#66CDAA face="黑体">',subject,'</font> \n\n',' *** \n\n',sendtext,'\n\n *** \n\n','#### [点击转到ZABBIX](https://www.zabbix.com/) \n\n'))
        }
    }
    resp = requests.post(
        DINGDING_API_URL, data=json.dumps(data), headers={'Content-Type': 'application/json'}
    )
    print(resp.text)
    if resp.status_code != 200:
        logger.info('[REQUESTS DINGTALK API ERROR]%s' % resp.text)




send_dingtalk_message(sendtext)
