


# 受保护的属性，加一个下划线
# 类内部，子类内部，模块内其他位置可以访问受保护属性
# 但是不建议在模块内其他位置访问受保护属性
# 跨模块无法访问受保护属性
# 但如果使用__all__ = ['_a']，并使用from 模块 import *， 则可以访问受保护属性


class Animal:
    _x = 10
    def test(self):
        # 类内部可以访问受保护属性_x
        print(Animal._x)
        print(self._x)

class Dog(Animal):
    def test(self):
        # 子类内部可以访问父类的受保护属性_x
        print(Dog._x)
        print(self._x)


a = Animal()
a.test()

dog1 = Dog()
dog1.test()

# 模块内其他位置可以访问受保护属性_x
print(Animal._x)
print(Dog._x)
print(a._x)
print(dog1._x)