from test_interface.orther.parametrized_testcase import Parametrized_TestCase


class TestInterfaceCase(Parametrized_TestCase):
    def setUp(self):
        pass

    # 测试接口 1
    def test_login_normal(self):
        # 根据被测接口的实际情况，合理的添加 HTTP 头
        # header ={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        # 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:29.0) Gecko/20100101 Firefox/29.0'
        #  }
        # self.http.set_header(header)
        response = self.http.send_get(self.test_data.request_url,
                                      self.test_data.request_param)
        if {} == response:
            self.test_data.result = 'Error'
            try:
                # 更新结果表中的用例运行结果
                self.db1_cursor.execute('UPDATE test_result SET result = %s WHERE case_id = % s' % (
                self.test_data.result, self.test_data.case_id))
                self.db1_cursor.execute('commit')
            except Exception as e:
                print('%s' % e)
                self.db1_cursor.execute('rollback')
            return
        try:
            # 如果有需要，连接数据库，读取数据库相关值，用于和接口请求返回结果做比较
            self.db2_cursor.execute('SELECT user_id FROM 1dcq_user WHERE mobile= % s',
                                    (eval(self.test_data.request_param)['mobile'],))
            user_id = self.db2_cursor.fetchone()[0]
            self.db2_cursor.close()
            # 断言
            self.assertEqual(response['code'], 0, msg='返回ecode不等于0')
            self.assertEqual(response['msg'], '登录成功 ', msg='登录失败')
            self.assertEqual(response['data']['sex'], 2, msg='sex  错误')
            self.assertEqual(response['data']['cityId'], None, msg='cityId 错误')
            self.assertEqual(response['data']['nikeName'], None, msg='nikeName错误')
            self.assertEqual(response['data']['cityName'], None, msg='cityName 错误')
            self.assertEqual(response['data']['userId'], user_id, msg='userId  错误')  # 2910057590
            self.assertEqual(response['data']['cityName'], None, msg='cityName  错误')
            self.assertEqual(response['data']['payPasswordFlag'], 1, msg='payPasswordFlag  错误 ')
            self.assertEqual(response['data']['imgSmall'], None, msg='imgSmall错误')
            self.assertEqual(response['data']['imgBig'], None, msg='imgBig  错误')
            self.test_data.result = 'Pass'
        except AssertionError as e:
            print('%s' % e)
            self.test_data.result = 'Fail'
            self.test_data.reason = '%s' % e  # 记录失败原因
            # 更新结果表中的用例运行结果
        try:
            self.db1_cursor.execute('UPDATE test_result SET result = %s WHERE case_id= % s',
                                    (self.test_data.result, self.test_data.case_id))
            self.db1_cursor.execute('UPDATE  test_result SET reason = %s WHERE case_id = % s',
                                    (self.test_data.reason, self.test_data.case_id))
            self.db1_cursor.execute('commit')
        except Exception as e:
            print('%s' % e)
            self.db1_cursor.execute('rollback')

    # 测试接口 2
    def test_chpasswd_normal(self):

        header = {'Content- - Type': 'application/json', 'charset': 'utf- - 8'}
        self.http.header(header)
        # 步骤 1-登录
        self.db1_cursor.execute(
            'SELECT request_url, request_param FROM pre_condition_data WHERE case_id = % s and step = 1',
            (self.test_data.case_id,))
        temp_result = self.db1_cursor.fetchone()
        request_url = temp_result[0]
        request_param = temp_result[1]
        lgin_response = self.http.send_get(request_url, request_param)
        # 修改密码
        user_id = lgin_response['data']['userId']  # 获取登录接口返回的 user_id
        payPassword = eval(request_param)['password']  # 获取原密码即登录密码
        # 拼接参数，作为修改支付密码接口的传入参数
        tmp_dic = {"userId": user_id, "payPassword": payPassword}

        self.test_data.request_param = eval(self.test_data.request_param)
        self.test_data.request_param.update(tmp_dic)
        # 修改密码
        response = self.http.send_post(self.test_data.request_url,
                                       str(self.test_data.request_param))
        if {} == response:
            self.test_data.result = 'Error'
            try:
                # 更新结果表中的用例运行结果
                self.db1_cursor.execute('UPDATE test_result SET result = %s WHERE case_id = % s',
                                        (self.test_data.result, self.test_data.case_id))
                self.db1_cursor.execute('commit')
            except Exception as e:
                print('%s' % e)
                self.db1_cursor.execute('rollback')
            return
        try:
            self.assertEqual(response['code'], 0, msg='返回ecode不等于0')
            self.assertEqual(response['msg'], '支付密码修改成功', msg=' 修改支付密码失败')
            self.assertEqual(response['data'], None, msg='data  不为  N')
            self.test_data.result = 'Pass'
        except AssertionError as e:
            print('%s' % e)
        self.test_data.result = 'Fail'
        self.test_data.reason = '%s' % e  # 记录失败原因
        # 更新结果表中的用例运行结果
        try:
            self.db1_cursor.execute('UPDATE test_result SET request_param = %s WHERE case_id = % s',
                                    (str(self.test_data.request_param), self.test_data.case_id))
            self.db1_cursor.execute('UPDATE test_result SET result = %s WHERE case_id= % s',
                                    (self.test_data.result, self.test_data.case_id))
            self.db1_cursor.execute('UPDATE test_result SET reason = %s WHERE case_id = % s',
                                    (self.test_data.reason, self.test_data.case_id))
            self.db1_cursor.execute('commit')
        except Exception as e:
            print('%s' % e)
        self.db1_cursor.execute('rollback')

    def tearDown(self):

        pass
