

# 类也是一种对象

# 如何让类拥有属性？方法1：类名.类属性名 = 属性值
class Person:
    pass


# 方法2：在类中直接定义属性
class Student:
    name = 'LR'
    age = 27


# 1. 给类添加属性，只可以通过类名添加，不可以通过实例添加
Person.name = 'Tom'
Person.age = 18 

# 2. 查看类属性
print("通过类访问类属性")
print(Person.name, Person.age)

p1 = Person()
print("通过实例访问类属性")
print(p1.name, p1.age)

print("查看所有类属性")
print(Person.__dict__)

print("通过实例查看类属性")
stu = Student()
print(stu.name, stu.age)
print(stu.__class__)

print("通过修改__class__属性，可以将一个实例的类改变")
stu.__class__ = Person
print(stu.name, stu.age)


# 3. 修改类属性，只可以通过类名修改，不可以通过实例修改
print("修改类属性")
Person.name = 'Jerry' 
print(Person.name)
print(p1.name)
print(stu.name)

# 4. 删除类属性，只可以通过类名删除，不可以通过实例删除
print("删除类属性")
del Person.name
# 对象的__dict__属性是一个字典，存储了对象的所有属性; 类的__dict__属性也是一个字典，存储了类的所有属性
# 类属性和实例属性都存储在__dict__属性中，但两者不是一样的
print(Person.__dict__)
print(p1.__dict__)
print(p1.age)


# 5. 一般情况下，属性存储在__dict__的字典中，有些内置对象没有__dict__属性
# 一般对象可以直接修改__dict__属性，但类对象的__dict__属性是只读的默认无法修改，但可以通过setter方法修改


# 6. 类属性被所有实例共享，实例属性是每个实例独有的


# 7. 使用魔法属性__slots__限制实例的属性
class Person:
    __slots__ = ('name', 'age')  # 限制实例只能有name和age属性
    pass
p2 = Person()
p2.name = 'Jack'
print(p2.name)
p2.sex = man
print(p2.sex)


# 8. 魔法属性，在python中，所有以双下划线（__）开头和结尾的属性都是魔法属性，即magic method
# 例如类的初始化方法__init__(), 实例对象创造方法__new__(), __dict__、__class__、__slots__、__name__等
# 魔法属性是python的一种约定，不要自己定义魔法属性，因为python会自动调用这些属性，魔法属性和方法是python内置
# 的一些属性和方法，有着特殊含义，在执行特定系统操作时，会自动调用