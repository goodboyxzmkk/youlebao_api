from faker import Faker

# fake=Faker() #默认生成美国英文数据
fake = Faker(locale='zh_CN')

# 地址类
print("地址类".center(20, "-"))
print(fake.address())  # 生成地址
print(fake.street_address())  # 生成街道地址
print(fake.street_name())  # 生成街道名
print(fake.city_name(), fake.city())
print(fake.province())

# 公司类：
print("公司类".center(20, "-"))
print(fake.company())
print(fake.company_suffix())
print(fake.company_prefix())

# 个人信息类
print("个人信息类".center(20, "-"))
print(fake.name())  # 东浩
print(fake.simple_profile())
# {'username': 'leihan', 'name': '武帅', 'sex': 'F', 'address': '吉林省淮安市双滦家街C座 210434', 'mail': 'lishao@hotmail.com', 'birthdate': '1988-11-12'}
print(fake.user_name(), fake.password(special_chars=False))  # ajiang zI2QbHy02p

# 文章类
print("文章类".center(20, "-"))
print(fake.word())  # 当前
print(fake.words(3))  # ['欢迎', '支持', '图片']
print(fake.sentence(3))  # 精华有关一些.
print(fake.paragraph())  # 大家电话空间一起操作图片要求.上海发展到了之间用户也是的人.必须记者关系介绍注册.用户时候投资发布
