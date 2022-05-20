import yaml
import os
from config.conf import cm

class Readlog(object):
    '''读取logyaml文件'''

    def __init__(self):
        self.log_yaml = os.path.join(cm.LOG_FILE, "logconfig.yaml")

    def red(self):
        if not os.path.exists(self.log_yaml):
            raise FileNotFoundError("%s 文件不存在！" % self.log_yaml)
        with open(self.log_yaml, encoding='utf-8') as f:
            data = yaml.safe_load(f)
            return data

    def write(self, data):
        with open(self.log_yaml, 'a', encoding='utf-8') as f:
            yaml.dump(data, f, allow_unicode=True)

redyaml = Readlog()

if __name__ == '__main__':
    print(redyaml.red()['logger'])
    # print(Readlog().write({"ces" : "测试"}))

