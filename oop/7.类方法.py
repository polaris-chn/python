

class Person:
    def shilifangfa(self):
        print('这是一个实例方法')
       
    # 使用装饰器 
    # 装饰器的作用是在不改变原函数的情况下，增加新的功能
    @classmethod
    def leifangfa(cls, a):
        print('这是一个类方法', cls, a)




p = Person()
p.shilifangfa() 

# 1. 类方法的调用，使用类调用或者实例调用，标准调用方式
Person.leifangfa("呵呵")
p.leifangfa("哈哈")

# 2. 间接调用
func = Person.leifangfa
func("嘿嘿")


class Student(Person):
    pass

# 3. 子类在调用父类的类方法时，会把子类作为第一个参数传递给类方法
# 所以这里会打印出__main__.Student，而不是__main__.Person
Student.leifangfa("呵呵")