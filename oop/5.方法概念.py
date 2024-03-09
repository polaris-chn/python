


# 方法的概念：描述了一个目标的行为动作，和函数类似，都封装了一系列行为动作，执行一系列行为动作
# 最主要的区别就是调用方式

# 方法划分为实例方法，类方法，静态方法
# 实例方法：第一个参数是self，表示实例对象本身
# 类方法：第一个参数是cls，表示类本身
# 静态方法：没有默认参数
# 不管是哪一种方法，都是存储在类当中的，没有存储在实例对象当中
# 不同类型方法调用方式不同


# 首先要掌握不同类型方法的语法，调用方式，最后是根据不同场景设计怎么的方法来解决问题

class Person:
    # 第一个接受的参数是self，表示实例对象本身，这是一个实例方法
    def shilifangfa(self):
        print('这是一个实例方法', self)
        
    # 类方法，第一个参数是cls，表示类本身
    @classmethod
    def leifangfa(cls):
        print('这是一个类方法', cls)
        
    # 静态方法，没有默认参数
    @staticmethod
    def jingtaifangfa():
        print('这是一个静态方法')
        

p1 = Person()
p1.shilifangfa()
p1.leifangfa()
p1.jingtaifangfa()

print(Person.__dict__)