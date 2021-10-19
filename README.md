
## 项目介绍

> 项目 zabbix_push 为zabbix 集成 钉钉，邮箱，企业微信，飞书等告警媒介的脚本集合


![image](https://raw.githubusercontent.com/ZuoGuocai/zabbix_push/master/images/sendmap.png)

## 如何配置请参考以下文章

- <<如何优雅地用Python3发送Zabbix告警推送>>

https://github.com/ZuoGuocai/myarticles


##  Zabbix5.0  + Python3.8  zmail 模块server属性找不到规避方法

发邮件这里改成Python原生发邮件的模块

```

import smtplib
from email.message import EmailMessage
from email.utils import make_msgid


def mail_push(to,subject,content_html):
    msg = EmailMessage()
    asparagus_cid = make_msgid()
    msg.add_alternative(content_html.format(asparagus_cid=asparagus_cid[1:-1]), subtype='html')

    fromEmail = '发件邮箱账号'
    toEmail = to

    msg['Subject'] = subject
    msg['From'] = fromEmail
    msg['To'] = toEmail

    s = smtplib.SMTP('邮件服务器地址', 587)
    s.starttls()
    s.login(fromEmail, '邮箱密码')
    s.send_message(msg)
    s.quit()



mail_push(to,subject,content_html)


```

##  Zabbix5.0  + Python3.8  Requests 模块报错解决方法

Requests模块替换为Python原生http协议处理模块urllib3 ，见飞书脚本



## 注意事项

/usr/lib/zabbix/alertscripts 下 新建的脚本的所有者，所属组 为zabbix，并且具有可执行权限


```
chown zabbix:zabbix  send-email-problems.py
chmod +x send-email-problems.py

```








![Anurag's github stats](https://github-readme-stats.vercel.app/api?username=ZuoGuocai&show_icons=true&theme=radical)


## Stargazers over time

[![Stargazers over time](https://starchart.cc/ZuoGuocai/zabbix_push.svg)](https://starchart.cc/ZuoGuocai/zabbix_push)

