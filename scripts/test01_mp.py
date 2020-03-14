from api.api_mp import ApiMp
import api
from tools.get_log import GetLog

from tools.tools import Tool

log = GetLog.get_logger()


class TestMp:
    # 初始化
    def setup_class(self):
        # 获取ApiMp对象
        self.mp = ApiMp()
        log.info("正在获取ApiMp对象：{}".format(self.mp))

    # 登录接口 测试方法
    def test01_mp_login(self, mobile=api.phone, code=api.code):
        # 调用登录接口
        r = self.mp.api_mp_login(mobile, code)
        try:
            # 提取token
            Tool.common_token(r)
            # 断言
            Tool.common_assert(r)
        except Exception as e:
            # 1. 日志
            log.error(e)
            # 2. 抛异常
            raise
            # 发布文章 接口测试方法

    def test02_mp_article(self, title=api.title, content=api.content):
        # 调用发布文章接口
        r = self.mp.api_mp_article(title, content)
        try:
            # 提取文章id
            api.article_id = r.json().get("data").get("id")
            log.info("正在提取发布文章id：{}".format(api.article_id))
            # 断言
            Tool.common_assert(r)
        except Exception as e:
            # 1. 日志
            log.error(e)
            # 2. 抛异常
            raise
