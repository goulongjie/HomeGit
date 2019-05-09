import os
import codecs
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]   #split:以最后一个/划分，获得路径和文件名
configPath = os.path.join(proDir,'config.ini')          #拼接路径

class ReadConfig():
    def __init__(self):
        fd = open(configPath)
        data = fd.read()

        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)


    def get_conf(self,section):
        keys=self.cf.options(section)
        conf_dict={}
        for key in keys:
            value=self.cf.get(section,key)
            conf_dict[key] = value
        return conf_dict


if __name__ == "__main__":
    a = ReadConfig().get_conf("DATABASE")["host"]
    print(a)

