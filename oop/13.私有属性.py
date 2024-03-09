
# 私有属性，使用双下划线__开头
# 私有属性只能在类内部访问，子类和类外部不可以访问
# 但如果使用__all__ = ['__a']，也就是指定私有属性，并使用from 模块 import *， 则可以跨模块访问私有属性

# 私有属性的实现机制，通过改名字，将私有属性改名字，改名字的规则是：_类名__私有属性名
# 目的是防止外界访问私有属性，另一个目的是防止被子类同名属性覆盖
# 其应用场景是数据保护和数据保护

class Animal:
    __x = 10
    def test(self):
        # 类内部可以访问私有属性__x
        print(Animal.__x)
        print(self.__x)

class Dog(Animal):
    def test(self):
        # 子类内部不可以访问父类的私有属性__x
        print(Dog.__x)
        print(self.__x)


a = Animal()
a.test()

# 通过__dict__可以查看到私有属性__x的改名字，改成了_Animal__x
print(Animal.__dict__)

# dog1 = Dog()
# dog1.test()

# # 模块内其他位置不可以访问私有属性__x
# print(Animal.__x)
# print(Dog.__x)
# print(a.__x)
# print(dog1.__x)