

# 实例属性只能通过实例访问
# 类属性可以通过类和实例访问

class Person:
    name = '小甲鱼'
    
    def shilifangfa(self):
        print('这是一个实例方法', self.name, self.age)
        print("实例方法可以访问到类属性和实例属性")
    
    @classmethod
    def leifangfa(cls):
        print('这是一个类方法', cls.name) 
        print("类方法可以访问到类属性，但是不能访问到实例属性")
    
    @staticmethod
    def jingtaifangfa():
        print('这是一个静态方法')
        print(Person.name)


p1 = Person()
p1.age = 20
# 调用实例方法
p1.shilifangfa()

# 调用类方法
Person.leifangfa()
p1.leifangfa()

# 调用静态方法
Person.jingtaifangfa()
p1.jingtaifangfa()
    