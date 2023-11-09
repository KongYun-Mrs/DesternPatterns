#!/usr/bin/env/python
"""
单例模式（Singleton）是一种创建型设计模式，其原理是确保一个类只有一个实例，
并且提供了一个访问该实例的全局点。

单例模式可以使用多种不同的实现方式，但它们的基本原理是相同的。
通常，单例模式使用一个私有构造函数来确保只有一个对象被创建。
然后，它提供了一个全局点访问该对象的方法，使得任何代码都可以访问该对象，而不必担心创建多个实例。
"""


class SingToln():
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            # 通过父类给自己实例化
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, *args, **kwargs) -> None:
        pass

# 装饰器实现
def deactor(cls):
    isinstance = {}
    def func(*args,**kwargs):
        if cls in isinstance:
            return isinstance[cls]
        else:
            isinstance[cls] = cls(*args,**kwargs)
            return isinstance[cls]
    return func

@deactor
class A:
    def __init__(self) -> None:
        pass


if __name__ == '__main__':
    s1 = SingToln()
    print(s1)
    s2 = SingToln()
    print(s2)
    print(s1 is s2)

    A1 = A()
    A2 = A()
    print(A1,A2)
    print(A1 is A2)
