

class Person:
    def run(self, name):
        print(name + ' is running')
        


p1 = Person()

# 1. 标准调用实例方法：通过实例对象调用，自动传递self，也就是这个实例对象本身
p1.run("lr")

# 表示run方法是一个函数
print(Person.run)   


# 后面两种方法很少用，本质是找到这个函数本身来调用
# 2. 通过类对象调用实例方法：需要手动传递self
Person.run(p1, "lr")  # 这里的p1就是self

# 3. 间接调用实例方法
func = p1.run
func("lr")  # 这里的p1就是self