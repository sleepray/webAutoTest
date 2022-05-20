import yaml
import os

class YamlMethod(object):

    @classmethod
    def yaml_read(cls, yaml_path):
        '''
        读取yaml文件
        :param yaml_path: yaml路径
        :return:
        '''

        def __init__(self, name):
            self.file_name = '%s.yaml' % name
            self.element_path = os.path.join(cm.ELEMENT_PATH, self.file_name)
            if not os.path.exists(self.element_path):
                raise FileNotFoundError("%s 文件不存在！" % self.element_path)
            with open(self.element_path, encoding='utf-8') as f:
                self.data = yaml.safe_load(f)

        with open(yaml_path, 'r', encoding='utf-8') as f:
            result = f.read()
            data = yaml.load(result, Loader=yaml.FullLoader)
            return data

    @classmethod
    def yaml_write(cls, yaml_path, data):
        with open(yaml_path, 'w', encoding='utf-8') as f:
            yaml.dump(data, f)
