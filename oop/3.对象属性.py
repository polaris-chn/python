# 对象属性和类属性
# 属性必须通过一个对象来进行访问



# 如何让一个对象拥有属性：直接给对象添加，例如：对象.属性名 = 属性值
# 或者通过构造方法添加，例如：__init__(self, 属性1, 属性2, ...)


# 1. 定义一个类
class Person:
    pass

# 2. 根据类创建一个对象
p1 = Person()

# 3. 给对象添加属性
p1.name = "zhangsan"
p1.age = 18


# 4. 通过对象访问属性
print(p1.name)
print(p1.age)
# __dict__属性可以查看对象的所有属性
print(p1.__dict__)  # {'name': 'zhangsan', 'age': 18}
print(p1.__class__)  # <class '__main__.Person'>

# 5. 修改对象的属性
p1.name = "lisi"
p1.age = 20
print(p1.name)
print(p1.age)

p1.pets = ["cat", "dog"]
p1.pets.append("pig")
print(p1.pets)

# 6. 删除对象的属性
print("删除属性前：", p1.__dict__)  # {'name': 'lisi', 'age': 20, 'pets': ['cat', 'dog', 'pig']}
del p1.age
print("删除属性后：", p1.__dict__)  # {'name': 'lisi', 'pets': ['cat', 'dog', 'pig']}
print(p1.__dict__)  # {'name': 'lisi', 'pets': ['cat', 'dog', 'pig']}

