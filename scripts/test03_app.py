import api
from api.api_app import ApiApp
from tools.get_log import GetLog
from tools.tools import Tool

log = GetLog.get_logger()


class TestApp:
    # 1. 初始化
    def setup_class(self):
        # 获取ApiMis对象
        self.app = ApiApp()
        log.info('正在获取ApiApp对象:{}'.format(self.app))

    # 2. 登录 接口测试方法
    def test01_app_login(self, phone=api.phone, code=api.code):
        # 调用登录接口
        r = self.app.api_app_login(phone, code)
        try:
            # 提取token
            Tool.common_token(r)
            # 断言
            Tool.common_assert(r)
        except Exception as e:
            log.error(e)
            raise

    # 3. 查询 接口测试方法
    def test02_app_find(self):
        # 调用查询接口
        r = self.app.api_app_find()
        try:
            # 断言
            Tool.common_assert(r, status_code=200)
        except Exception as e:
            log.error(e)
