import os

# 项目路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# extract yaml文件路径
ex_yaml_path = ''.join([BASE_DIR, '/data/extract.yaml'])


# login json文件路径
login_js_path = ''.join([BASE_DIR, '/data/login.json'])

# 测试报告路径
REPORT_DIR = BASE_DIR + "/Test_Reports/"

# web基础路径
base_url = 'https://monitor.autowise.tech/#/'


class login:
    login = 'login'


class module:
    summary = 'map'
    statistics = 'statistics'
    schedule = 'schedule'
    resource = 'resource'