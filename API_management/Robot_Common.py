import json

from Common.request_util import SendRequestUtil
from Common import parameter as param
from Common.get_token import GetToken


class Robot_Common:
    headers = {
        "content-type": 'text/html;charset=utf-8',
        "Traceid": '1649405809057368167413067233110960208255',
        "token": GetToken().get_token()
    }

    def __init__(self):
        self.sr = SendRequestUtil()

    def send_http_request(self, method, url, data):
        return self.sr.send_request(method=method,
                                    url=url,
                                    headers=self.headers,
                                    data=json.dumps(data))

