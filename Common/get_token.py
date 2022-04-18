from API_management.login_api import LoginAPI
from Common.json_util import GetJson
from Common.parameter import login_js_path


class GetToken:
    def __init__(self):
        self.login = LoginAPI()
        self.get_token = GetJson(login_js_path)

    def get_token(self):
        res, token = self.login.login(self.get_token.data['login_test'])
        return token
