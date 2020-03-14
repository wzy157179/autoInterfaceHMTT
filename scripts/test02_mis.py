import api
from api.api_mis import ApiMis
from tools.get_log import GetLog
from tools.tools import Tool

log = GetLog.get_logger()


class TestMis:
    # 1. 初始化
    def setup_class(self):
        # 获取ApiMis对象
        self.mis = ApiMis()
        log.info("正在获取ApiMis对象:{}".format(self.mis))

    # 2. 登录 接口测试方法
    def test01_mis_login(self, user=api.mis_user, pwd=api.mis_pwd):
        # 调用登录接口
        r = self.mis.api_mis_login(user, pwd)
        try:
            # 提取token
            Tool.common_token(r)
            # 断言
            Tool.common_assert(r)
        except Exception as e:
            log.error(e)
            raise

    # 3. 查询 接口测试方法
    def test02_mis_find(self):
        # 调用查询接口
        r = self.mis.api_mis_find()
        try:
            # 断言
            Tool.common_assert(r, status_code=200)
        except Exception as e:
            log.error(e)
            raise

    # 4. 审核 接口测试方法
    def test03_mis_audit(self):
        # 调用登录接口
        r = self.mis.api_mis_audit()
        try:
            # 断言
            Tool.common_assert(r)
        except Exception as e:
            log.error()
            raise
