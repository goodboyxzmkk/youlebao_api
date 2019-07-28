class myclass():

    def test1(self, *args):
        print("self:", self)
        print(type(args))  # *把多个参数放在元组传递
        for value in args:
            print("args:", value)

    '''加了星号 * 的参数会以元组(tuple)的形式导入，加了** 的参数会以字典dic的形式导入'''

    def test2(self, **kwargs):
        print("self", kwargs)
        for key in kwargs:
            print("key:{},value:{}".format(key, kwargs[key]))


# lambda 来创建匿名函数
sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))

ss = myclass()
ss.test1(1, 2, 3, 4, 5, 6)
aa = {"a": 10, "b": 20}
print(type(aa))
ss.test2(a=10, b=20)
