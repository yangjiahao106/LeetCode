#! python3
# __author__ = "YangJiaHao"
# date: 2018/12/26
# 1. 两个字符串的交集

def intersection(str1, str2):
    myset = set(str1)
    res = set()
    for c in str2:
        if c in myset:
            res.add(c)

    return res


res = intersection("abcd", "kjcb")
print(res)


# 实现一个栈，线程安全。
def singleton(cls):
    instance = {}

    def function(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return function


@singleton
class Foo(object):
    def __init__(self, name):
        self.name = name

class Singleton(object):

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class ConstValue(object):
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, key, value):
        if key in self.__dict__.keys():
            raise self.ConstError('Not allowed change const.{value}'.format(key))

        if not key.isupper():
            raise self.ConstCaseError("Const's name is not all uppercase")

        self.__dict__[key] = value




# class Singleton(object):
#     _state = {}
#     def __new__(cls, *args, **kwargs):
#         obj = super(Singleton, cls).__new__(cls)
#         obj.__dict__ = cls._state
#         return obj


t = Singleton("a")
p = Singleton("b")
print(t.name)
print(p.name)
