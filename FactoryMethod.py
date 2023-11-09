from abc import ABC, abstractclassmethod
"""
工厂模式的优点：
这种方法可以使代码更加灵活，因为在运行时可以选择要实例化的对象类型。
例如，可以轻松地添加新的子类来创建不同的对象类型，而无需更改现有的代码。
工厂方法模式还提供了一种解耦的方式，因为它将对象的创建逻辑与其使用代码分离。
这可以使代码更加可维护和可测试，因为可以独立地测试和修改对象的创建逻辑和使用代码。
工厂方法模式常用于框架和库中，因为它可以使用户扩展框架或库的功能，而无需更改框架或库的源代码。
"""

class Product(ABC):
    @abstractclassmethod
    def use(self):
        pass


class ProductA(ABC):
    def use(self):
        print("use ProductA")


class ProductB(ABC):
    def use(self):
        print("use ProductB")


class FactroyBase(ABC):
    @abstractclassmethod
    # 定义一个抽象类接口，让子类帮助我们去实例化对象
    def factory_init(self):
        pass

    def operation(self):
        product = self.factory_init()
        product.use()


class FactoryA(FactroyBase):
    def factory_init(self):
        return ProductA()


class FactoryB(FactroyBase):
    def factory_init(slef):
        return ProductB()


if __name__ == '__main__':
    FA = FactoryA()
    FA.operation()

    FB = FactoryB()
    FB.operation()
