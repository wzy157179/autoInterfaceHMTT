"""以下为公共变量"""
# host域名/ip
from tools.read_yaml import read_yaml

HOST = "http://ttapi.research.itcast.cn"
# 请求信息头
headers = {"Content-Type": "application/json"}
# 文章id
article_id = None
# 读取参数数据
data = read_yaml("mp_article.yaml")

# 文章标题
title = data[0][0]
# 文章内容
content = data[0][1]
# 频道
channel = data[0][2]
# 频道id
channel_id = data[0][3]


data = read_yaml("mp_login.yaml")

# 登录电话
phone = data[0][0]
# 登录验证码
code = data[0][1]
# 后台账号
mis_user = data[0][2]
# 后台密码
mis_pwd = data[0][3]

