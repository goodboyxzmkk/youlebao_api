import configparser
import pymysql
import sys


class Get_DB():
    '''配置数据库 IP，端口等信息，获取数据库连接'''

    def __init__(self, ini_file, db):
        config = configparser.ConfigParser()
        # 从配置文件中读取数据库服务器 IP、域名，端口
        config.read(ini_file)
        self.host = config[db]['host']
        self.port = config[db]['port']
        self.user = config[db]['user']
        self.pwd = config[db]['passwd']
        self.db = config[db]['db']
        self.charset = config[db]['charset']

    def get_conn(self):
        try:
            conn = pymysql.connect(host=self.host, port=self.port,
                                   user=self.user, password=self.pwd, database=self.db, charset=self.charset)
            return conn
        except Exception as e:
            print('%s', e)
            sys.exit()
