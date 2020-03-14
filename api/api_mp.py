import api
import requests

from tools.get_log import GetLog

log = GetLog.get_logger()


class ApiMp:
    # 初始化方法
    def __init__(self):
        # 登录url
        self.url_login = api.HOST + "/mp/v1_0/authorizations"
        log.info("正在初始化自媒体登录url:{}".format(self.url_login))
        # 发布文章url
        self.url_article = api.HOST + "/mp/v1_0/articles"
        log.info("正在初始化自媒体发布文章 url:{}".format(self.url_article))

    # 登录接口 封装
    def api_mp_login(self, mobile, code):
        # 请求数据
        data = {"mobile": mobile, "code": code}
        log.info("正在调用自媒体登录方法，测试数据: {} 请求头：{}".format(data, api.headers))
        # 调用post方法 注意：1. 此处使用json 2.返回响应对象
        return requests.post(url=self.url_login, json=data, headers=api.headers)

    # 发布文章接口 封装
    def api_mp_article(self, title, content):
        """
        :param title: 文章标题
        :param content: 文章内容
        :channel_id:7 为数据库
        :cover:封面 0为自动选择
        :return:
        """
        # 请求数据
        data = {"title": title, "content": content, "channel_id": api.channel_id, "cover": {"type": 0, "images": []}}
        log.info("正在调用自媒体发布文章方法，测试数据: {} 请求头：{}".format(data, api.headers))
        # 调用post方法
        return requests.post(url=self.url_article, json=data, headers=api.headers)
