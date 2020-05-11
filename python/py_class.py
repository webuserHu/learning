'''
class Student(object):
    pass

a = Student()
a.name = "aaaa"
print(a.name)
'''

'''
class Student(object):
    #相当于有参构造
    def __init__(self,name,age):
        self.name = name
        self.age = age

a = Student("aaa",20)
print(a.name)
print(a.age)
'''
'''
class Student(object):
    #私有属性,加__
    def __init__(self,name,age):
        self.__name = name
        self.age = age

a = Student("aaa",20)
#print(a.name)#访问不到
#print(a.age)#可以访问
'''
'''
#继承
class Animal(object):

    def run(self):
        print("animal")
animal = Animal()
animal.run()

class Dog(Animal):
    def run(self):
        print("dog")
dog = Dog()
dog.run()

#获取对象信息
print(isinstance(animal,Dog))#判断animal是否为dog类型
print(type(animal))#返回是什么类型
print(dir('ABC'))#返回属性和方法
print(hasattr('ABC',"lower"))#某对象是否有某属性或方法
'''
'''
#getter setter
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth
'''