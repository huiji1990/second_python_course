
# import 包.模块.类/函数
# 模块即py文件名
import a.util
from a import test as t
import b.util


if __name__=='__main__':
    a.util.util.a()
    b.util.util.a()
    t.test()