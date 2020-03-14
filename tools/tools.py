import api
from tools.get_log import GetLog

log = GetLog.get_logger()


class Tool:
    # 提取token
    @classmethod
    def common_token(cls, response):
        log.info("正在调用公共方法提取token")
        # 提取token
        token = response.json().get("data").get("token")
        # 追加到请求头中
        api.headers['Authorization'] = "Bearer " + token

    # 断言
    @classmethod
    def common_assert(cls, response, status_code=201):
        log.info("正在调用公共方法断言")
        # 断言状态
        assert status_code == response.status_code
        # 断言message
        assert "OK" == response.json().get("message")
