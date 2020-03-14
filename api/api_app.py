import requests
import time
import api
from tools.get_log import GetLog

log = GetLog.get_logger()


class ApiApp:
    # 1. 初始化
    def __init__(self):
        # 登录 url
        self.url_login = api.HOST + '/app/v1_0/authorizations'
        log.info("正在初始化自媒体登录url:{}".format(self.url_login))
        # 查询文章 url
        self.url_find = api.HOST + '/app/v1_1/articles'
        log.info("正在初始化查询文章url:{}".format(self.url_find))

    # 2. 登录 接口封装
    def api_app_login(self, phone, password):
        # 请求参数
        data = {"mobile": phone, "code": password}
        log.info("正在调用自媒体登录方法，测试数据: {} 请求头：{}".format(data, api.headers))
        # 调用post方法
        return requests.post(url=self.url_login, json=data, headers=api.headers)

    # 3. 查询文章 接口封装
    def api_app_find(self):
        # 请求参数
        data = {'channel_id': api.channel_id, 'timestamp': int(time.time()), "with_top": 0}
        log.info("正在调用查询文章方法，测试数据: {} 请求头：{}".format(data, api.headers))
        # 调用get方法
        return requests.get(url=self.url_find, params=data, headers=api.headers)
