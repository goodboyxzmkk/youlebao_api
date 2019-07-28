def source_sub_file(filename):
    '''str='name:zhangsan' '''
    key = []
    value = []
    with open(filename, 'r') as f:
        for str in f.readlines():
            str = str.strip()  # 去除首尾空格
            key.append(str.split(":")[0])  # 按:分割字符
            value.append(':'.join(str.split(":")[1:]))  # 按:分割字符
    return key, value


def str_split():
    zu = source_sub_file('d:\\FiddlerSourceFile.txt')
    f = open('d:\\To_API_File.txt', 'w', encoding='utf-8')
    for i in range(len(zu[0])):
        str1 = "\"" + zu[0][i] + "\"" + ':' + "\"" + zu[1][i] + "\"" + ','
        # str2 = str1.replace(' ', '')
        f.write(str1 + "\n")
        print(str1)
    f.close()


if __name__ == '__main__':
    str_split()
