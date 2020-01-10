#!/usr/bin/env python3
# author: zuoguocai@126.com
# Function:  send alert message via exchange
import  zmail
import sys
import ast

to = sys.argv[1]
subject = sys.argv[2]
data = sys.argv[3]

# 把字符串转为字典
message  = ast.literal_eval(data)

HOSTNAME = ': '.join(('告警主机',message["HOSTNAME"]))
HOSTIP = ': '.join(('告警地址',message["HOSTIP"]))
ITEMNAME = ': '.join(('监控项目',message["ITEMNAME"]))
ITEMLASTVALUE = ': '.join(('监控取值',message["ITEMLASTVALUE"]))
TRIGGERSEVERITY = ': '.join(('告警等级',message["TRIGGERSEVERITY"]))
TRIGGERSTATUS = ': '.join(('当前状态',message["TRIGGERSTATUS"]))
TRIGGERNAME = ': '.join(('告警信息',message["TRIGGERNAME"]))
EVENTTIME = ': '.join(('告警时间',message["EVENTTIME"]))
EVENTAGE = ': '.join(('持续时间',message["EVENTAGE"]))
EVENTID = ': '.join(('事件ID',message["EVENTID"]))


msg = '<br>'.join((HOSTNAME,HOSTIP,ITEMNAME,ITEMLASTVALUE,TRIGGERSEVERITY,TRIGGERSTATUS,TRIGGERNAME,EVENTTIME,EVENTAGE,EVENTID))

begin = '''<div style="font-family:verdana;padding:20px;width:200px;border-radius:10px;border:3px solid #86CC89;">
<h3 style="color:#86CC89 ;display:inline;"> :-) '''

middle = '''</h3>
<h5 style="color:black">'''

end = '''</h3> 
</div> 
<br>
<br>
<br>
<br> 
<br>
'''


content_html = ' '.join((begin,subject,middle,msg,end))


def  mail_push(to,subject,content_html):
    server = zmail.server('myusername', 'mypassword', smtp_host='myexchangehostip', smtp_port=25,smtp_tls=True, smtp_ssl=False)
    mail = {
        'subject': subject,
        'content_html': content_html,
    }
    #server.send_mail(['zuoguocai@126.com','zuoguocai@outlook.com'],mail)
    server.send_mail(to,mail)


mail_push(to,subject,content_html)
