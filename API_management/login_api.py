import json

from Common.request_util import SendRequestUtil
from Common.json_util import GetJson


class LoginAPI:

    def __init__(self):
        self.headers = {'content-type': 'application/json',
                        }
        self.post_method = "post"
        self.url = 'https://monitor.autowise.tech/v1/user/login'
        self.sr = SendRequestUtil()

    def send_http_request(self, data):
        return self.sr.send_request(name=data['case_name'],
                                    method=self.post_method,
                                    url=self.url,
                                    headers=self.headers,
                                    data=json.dumps(data['json']))

    # 登录api单独拿出来获取token值
    def login(self, data):
        """
        :username 用户名
        :password 密码
        :return
        """
        res = self.send_http_request(data=data)
        print(res.text)
        return res.json()
