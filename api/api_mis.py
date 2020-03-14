import requests

import api
from tools.get_log import GetLog

log = GetLog.get_logger()


class ApiMis:
    # 1. 初始化
    def __init__(self):
        # 登录 url
        self.url_login = api.HOST + '/mis/v1_0/authorizations'
        log.info("正在初始化后台登录url:{}".format(self.url_login))
        # 查询文章 url
        self.url_find = api.HOST + '/mis/v1_0/articles'
        log.info("正在初始化查询文章url:{}".format(self.url_find))
        # 审核文章 url
        self.url_audit = api.HOST + '/mis/v1_0/articles'
        log.info("正在初始化审核url:{}".format(self.url_audit))

    # 2. 登录 接口封装
    def api_mis_login(self, account, password):
        # 请求参数
        data = {"account": account, "password": password}
        log.info("正在调用后台登录方法，测试数据: {} 请求头：{}".format(data, api.headers))
        # 调用post方法
        return requests.post(url=self.url_login, json=data, headers=api.headers)

    # 3. 查询文章 接口封装
    def api_mis_find(self):
        # 请求参数
        data = {'title': api.title, 'channel': api.channel}
        log.info("正在调用查询文章方法，测试数据: {} 请求头：{}".format(data, api.headers))
        # 调用get方法
        return requests.get(url=self.url_find, params=data, headers=api.headers)

    # 4. 审核文章 接口封装
    def api_mis_audit(self):
        # 请求参数
        data = {"article_ids": [api.article_id], "status": 2}  # 2:为审核通过
        log.info("正在调用审核文章方法，测试数据: {} 请求头：{}".format(data, api.headers))
        # 调用put
        return requests.put(url=self.url_audit, json=data, headers=api.headers)
