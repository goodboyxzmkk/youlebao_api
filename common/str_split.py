def source_sub_file(filename):
    '''str='name:zhangsan' '''
    key = []
    value = []
    with open(filename, 'r') as f:
        for str1 in f.readlines():
            str1 = str1.strip()  # 去除首尾空格
            key.append(str1.split(":")[0].strip())  # 按:分割字符
            value.append(str1.split(":")[1].strip())  # 按:分割字符
            # value.append(':'.join(str1.split(":")[1:]).strip())  # 按:分割字符
    return key, value


def str_split():
    zu = source_sub_file(r'D:\转json\old_file.txt')
    f = open(r'D:\转json\new_file.txt', 'w', encoding='utf-8')
    f.write("{\n")
    print("{")
    for i in range(len(zu[0])):
        if (i == len(zu[0]) - 1):
            str1 = "\"" + zu[0][i] + "\"" + ':' + "\"" + zu[1][i] + "\""
            f.write(str1 + "\n")
        else:
            str1 = "\"" + zu[0][i] + "\"" + ':' + "\"" + zu[1][i] + "\"" + ','
            f.write(str1 + "\n")
        print(str1)
    f.write("}")
    print("}")
    f.close()


if __name__ == '__main__':
    str_split()
