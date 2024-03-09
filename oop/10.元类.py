


# 对象是由类产生的，类也是一个对象，所以类对象也是由一个类产生的，这个类就是元类
# 元类就是type类，type类是所有类的元类， s.__class__就是s的类，s.__class__.__class__就是s的类的类
# 打印显示出type，也就是元类。元类的作用就是创建其他类对象

num = 10
print(num.__class__)
print(num.__class__.__class__)

s = 'abc'
print(s.__class__)
print(s.__class__.__class__)

class Student:
    pass

stu = Student()
print(stu.__class__)
print(stu.__class__.__class__)


# 类对象的创建流程，检测类对象中是否明确 __metaclass__属性
# 检测父类中是否有__metaclass__属性
# 检测模块中是否有__metaclass__属性
# 通过type创建类对象

