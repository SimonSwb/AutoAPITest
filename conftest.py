import os
from Common.parameter import REPORT_DIR


def new_report_time():
    """
    获取最新报告的目录名（即运行时间，例如：2021_07_01_17_40_44）
    """
    files = os.listdir(REPORT_DIR)
    files.sort()
    try:
        return files[-1]
    except IndexError:
        return None


def init_report_dir(now_time):
    """
    初始化测试报告目录
    """
    os.mkdir(REPORT_DIR + now_time)