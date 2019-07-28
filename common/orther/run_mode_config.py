import configparser


class Run_Mode_Config:
    def __init__(self, run_case_config_file):
        config = configparser.ConfigParser()
        # 从配置文件中读取运行模式
        config.read(run_case_config_file)
        try:
            self.run_mode = config['RUNCASECONFIG']['runmode']
            self.run_mode = int(self.run_mode)
            self.case_list = config['RUNCASECONFIG']['case_id']
            self.case_list = eval(self.case_list)  # 把字符串类型的 list 转换为 list
        except Exception  as e:
            print('%s', e)

    def get_run_mode(self):
        return self.run_mode

    def get_case_list(self):
        return self.case_list
