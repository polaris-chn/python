


# 一个属性，一般是实例属性，只能读取，不能写入
# 其应用场景是只限在内部根据不同场景进行修改，对外界来说不能修改，只能读取



# 方法1：使用@property装饰器
class Person:
    # 全部隐藏，将属性变成私有属性
    def __init__(self):
        self.__age = 18

    # 使用@property装饰器，可以以使用属性的方式来使用这个方法
    @property
    def get_age(self):
        return self.__age
    
    
p2 = Person()
print(p2.get_age)  # 18
p2.get_age = 20  # AttributeError: can't set attribute, 不能修改,只能读取




# 方法2：私有属性，通过方法进行读取

class Person:
    # 全部隐藏，将属性变成私有属性
    def __init__(self):
        self.__age = 18

    # 部分公开，使用一个方法，将这个私有属性的读取方法公开出去 
    def get_age(self):
        return self.__age
    
p1 = Person()
print(p1.get_age())  # 18