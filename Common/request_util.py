import requests
import traceback
from Common.logger_util import error_log, info_log, warning_log, debug_log


class SendRequestUtil:

    # 默认通过session发送请求，通过session会话去关联，session默认的情况下会自动关联cookie
    # 而非本身request.xxx或request.request发送
    def __init__(self):
        self.session = requests.session()

    # 统一封装发送请求
    def send_request(self, name, method, url, **kwargs):
        info_log(f'Case名称：{name}\n')
        info_log(f"请求方式： {method}\n")
        info_log(f"请求url地址： {url}\n")

        res = ''
        if "headers" in kwargs.keys():
            info_log("请求头: %s\n" % kwargs["headers"])
        if "params" in kwargs.keys():
            info_log("请求params参数: %s\n" % kwargs["params"])
        if "data" in kwargs.keys():
            info_log("请求data参数: %s\n" % kwargs["data"])
        if "json" in kwargs.keys():
            info_log("请求json参数: %s\n" % kwargs["json"])
        if "files" in kwargs.keys():
            info_log("文件上传： %s\n" % kwargs["files"])
        try:
            method = str(method).lower()
            res = self.session.request(method, url, **kwargs)
        except Exception as e:
            error_log(f'{method}请求发送异常,{str(traceback.format_exc())}\n')
        return res
