import logging


def log(func):
    def wrapper(*arg, **kwargs):
        logging.info('%s is running...' % func.__name__)
        print('方法名：{}'.format(func.__name__))
        func(*arg, **kwargs)  # 把today当作参数传递进来，执行func()就相当于执行today()
        print("=====")

    return wrapper


@log
def today(*arg, **kwargs):
    print('2018-05-25 arg:' + str(arg) + "kw:" + str(kwargs))


today("dd", "bbb", aa="aa", bb="bb")
