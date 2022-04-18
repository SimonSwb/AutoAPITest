import os
import yaml
from Common.parameter import ex_yaml_path


# 读取
def read_yaml(key):
    with open(ex_yaml_path, mode='r', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value[key]


# 写入
def write_yaml(data):
    with open(ex_yaml_path, mode='a', encoding='utf-8') as f:
        yaml.dump(data, stream=f, allow_unicode=True)


# 清空
def clear_yaml(data):
    with open(ex_yaml_path, mode='w', encoding='utf-8') as f:
        f.truncate()


if __name__ == '__main__':
    print(ex_yaml_path)
    print(read_yaml('baidu'))