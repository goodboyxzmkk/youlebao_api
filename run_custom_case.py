from test_interface.test_login_case import Test_Login_Case
from test_interface.test_leaguer_level_case import Test_Leaguer_Level_Case
from common import config_manage
import unittest, HTMLTestRunner, time
from common.send_dingding import send_ding,send_ding_url

'''自定义运行测试用例'''
login = unittest.TestLoader().loadTestsFromTestCase(Test_Login_Case)
leaguer_level = unittest.TestLoader().loadTestsFromTestCase(Test_Leaguer_Level_Case)

if __name__ == '__main__':
    # suites = unittest.TestSuite([online_test, login_test, leaguer_level_test])
    suites = unittest.TestSuite([login, leaguer_level])

    # now = time.strftime("%Y-%m-%d %H-%M-%S")
    # html_file = config_manage.REPORT_PATH + now + ".html"  #每次生成一份新的测试报告
    html_file = config_manage.REPORT_PATH + "TestResult_Report.html"  # 固定生成一份测试报告
    fp = open(html_file, "wb")
    '''retry，指定重试次数，如果save_last_try 为True ，一个用例仅显示最后一次测试的结果,为False，则显示所有重试的结果'''
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='游乐宝_接口自动化测试报告', description='用例执行情况:', verbosity=2,
                                           retry=0, save_last_try=False)
    runner.run(suites)
    fp.close()
    # send_ding_to_html("test")
    # send_ding("测试完成")
    # send_email.send_Email()
