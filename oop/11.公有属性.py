


# 私有化属性，保证数据安全
# python中没有真正的私有化支持，但是可以通过下划线(_)实现伪私有化
# 类属性（方法）和实例属性（方法）遵循相同的规则


# 1.公有属性
# 类内部访问，子类内部访问，模块内其他位置访问，
# 跨模块访问，使用import形式导入或者使用from 模块 import *形式导入


class Animal:
    x = 10
    def test(self):
        # 类内部可以访问公有属性x
        print(Animal.x)
        print(self.x)

class Dog(Animal):
    def test(self):
        # 子类内部可以访问父类的公有属性x
        print(Dog.x)
        print(self.x)


a = Animal()
a.test()

dog1 = Dog()
dog1.test()

# 模块内其他位置可以访问公有属性x
print(Animal.x)
print(Dog.x)
print(a.x)
print(dog1.x)