from IPython.utils.tests.test_wildcard import p
from pyh import *
import time
import os


class HtmlReport:
    def __init__(self, cursor):
        self.title = 'test_report_page'  # 网页标签名称
        self.filename = ''  # 结果文件名
        self.time_took = '00:00:00'  # 测试耗时
        self.success_num = 0  # 测试通过的用例数
        self.fail_num = 0  # 测试失败的用例数
        self.error_num = 0  # 运行出错的用例数
        self.case_total = 0  # 运行测试用例总数
        self.cursor = cursor

    # 生成 HTML 报告
    def generate_html(self, head, file):
        page = PyH(self.title)
        page << h1(head, align='center')  # 标题居中
        page << p('测试总耗时： ' + self.time_took)
        # 查询测试用例总数
        query = ('SELECT  count (case_id) FROM test_result')
        self.cursor.execute(query)
        self.case_total = self.cursor.fetchone()[0]
        # 查询测试失败的用例数
        self.cursor.execute('SELECT  count (case_id) FROM test_result WHERE result = % s', ('Fail',))
        self.fail_num = self.cursor.fetchone()[0]
        # 查询测试通过的用例数
        self.cursor.execute('SELECT  count (case_id) FROM test_result  WHERE result = % s', ('Pass',))
        self.success_num = self.cursor.fetchone()[0]
        # 查询测试出错的用例数
        self.cursor.execute('SELECT  count (case_id) FROM test_result WHERE result = % s', ('Error',))
        self.error_num = self.cursor.fetchone()[0]
        page << p('测试用例数： ' + str(self.case_total) + ' & nbsp' * 10 + '成功用例数： ' + str(
            self.success_num) + '&nbsp' * 10 + '失败用例数： ' + str(self.fail_num) + ' & nbsp' * 10 + '出错用例数: ' + str(
            self.error_num))
        # 表格标题 caption 表格边框 border 单元边沿与其内容之间的空白cellpadding单元格之间间隔为cellspacing
        tab = table(border='1', cellpadding='1', cellspacing='0', cl='table')
        tab1 = page << tab
        tab1 << tr(td('用例ID', bgcolor='  # ABABAB', align='center')
                   + td('HTTP  方法', bgcolor='# ABABAB', align='center')
                   + td(' 接口名称', bgcolor='#ABABAB', align='center')
                   + td('请求URL', bgcolor='# ABABAB', align='center')
                   + td('请求参数 / / 数据', bgcolor='#ABABAB', align='center')
                   + td('测试方法 ', bgcolor='#ABABAB', align='center')
                   + td('测试描述', bgcolor='#ABABAB', align='center')
                   + td('测试结果 ', bgcolor='#ABABAB', align='center')
                   + td('失败原因', bgcolor='#ABABAB', align='center'))
        # 查询所有测试结果并记录到 html 文档
        query = (
            'SELECT case_id, http_method, request_name, request_url,request_param, test_method, test_desc, result, reason FROM test_result')
        self.cursor.execute(query)
        query_result = self.cursor.fetchall()
        for row in query_result:
            tab1 << tr(td(int(row[0]), align='center') + td(row[1]) +
                       td(row[2]) + td(row[3], align='center') +
                       td(row[4]) + td(row[5]) + td(row[6]) +
                       td(row[7], align='center') + td(row[8]))
        self._set_result_filename(file)
        page.printOut(self.filename)
        try:
            query = ('DELETE FROM test_result')
            self.cursor.execute(query)
            self.cursor.execute('commit')
        except Exception  as e:
            # 回滚
            print('%s' % e)
            self.cursor.execute('rollback')
        self.cursor.close()

        # 设置结果文件名

    def _set_result_filename(self, filename):
        self.filename = filename

        # 判断是否为目录
        if os.path.isdir(self.filename):
            raise IOError("%s must point to a file" % path)
        elif '' == self.filename:
            raise IOError('filename can not be empty')
        else:
            parent_path, ext = os.path.splitext(filename)
            tm = time.strftime('%Y%m%d%H%M%S', time.localtime())
            self.filename = parent_path + tm + ext

            # 统计运行耗时

    def set_time_took(self, time):
        self.time_took = time
        return self.time_took
