import json
from Common.parameter import login_js_path


class GetJson:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.read_json()

    # 读取json文件，转换成python对象
    def read_json(self):
        with open(self.file_path, encoding='utf-8') as fp:
            data = json.load(fp)
            return data


a = GetJson(login_js_path)

print(a.data['case_name'])