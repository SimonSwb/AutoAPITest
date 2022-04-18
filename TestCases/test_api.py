import json

import allure
import pytest
import requests
from Common.yaml_util import read_yaml
from Common.json_util import GetJson
from Common.request_util import SendRequestUtil
from API_management.login_api import LoginAPI
from Common import parameter as para


@ allure.feature('测试需求分类')
class Test_Request:

    def setup_class(self):
        self.op = LoginAPI()
        self.gj = GetJson(para.login_js_path)

    @allure.story('测试模块下子功能，即测试场景')
    @allure.title('单条用例标题')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.issue(url='上报jira链接', name='上报jira标题')
    @allure.testcase('用例名：登录接口')
    @pytest.mark.vehicle
    @pytest.mark.emulation
    # @pytest.mark.parametrize('caseinfo', GetJson(login_js_path))
    def test_start(self):
        data1 = self.gj.data
        # username = data['username']
        # password = data['password']
        ts = self.op
        allure.step('发送登录请求')
        allure.attach('在发送请求时添加一个说明文件','文件名称xxx附件',allure.attachment_type.TEXT)
        res = ts.login(data=data1)


if __name__ == '__main__':
    pytest.main('--alluredir', 'E:/Study/RobotAPI/Test_Reports/temps')
