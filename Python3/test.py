#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/15

def decorator(fn):
    def warps():
        print('<b>' + fn() + '</b>')

    return warps


@decorator
def hello():
    return 'hello world'


# def Singleton(cls, *args, **kwargs):
#     instance = {}
#     def wrap(*args,**kwargs):
#         if cls in instance:
#             return instance[cls]
#         else:
#             instance[cls] = cls(*args, **kwargs)
#             return instance[cls]
#
#     return wrap

# def singleton(cls, *args, **kwargs):
#     instances = {}
#     def getinstance(*args, **kwargs):
#         if cls not in instances:
#             instances[cls] = cls(*args, **kwargs)
#         return instances[cls]
#     return getinstance
#
#
# @singleton
# class Myclass(object):
#     def __init__(self, a):
#         self.a = a
#
#
# one = Myclass('abc')
# print(one)
#
# two = Myclass('def')
# print(two)
#
#
# class Singleton(object):
#         def __new__(cls,*args,**kwargs):
#             if hasattr(cls,'_instance'):
#                 return cls._instance
#             else:
#                 cls._instance=super(Singleton,cls).__new__(cls)
#             return cls._instance
#
#
# class Myclass(Singleton):
#         def __init__(self,a):
#                 self.a=a
#
#
# one = Myclass('123')
# print(one)
# #abc
#
# two = Myclass('456')
# print(two.a)
# #cde

class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
        return cls._instance


class MyClass(Singleton):
    a = 1

one = MyClass()
print(one)
#abc

two = MyClass()
print(two)
#cde
