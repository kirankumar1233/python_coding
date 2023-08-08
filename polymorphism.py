# polymorphism - one person palys different roles 
# there are two types 1.methodoverload and 2.method overidding

# method overload

'''class methodoverload():
    def something(self,a,b,c,d):
        print(a,b,c,d)
obj=methodoverload()
obj.something(1,3,5,6)
obj.something(1,3,4)
obj.something(1,2)
obj.something()'''

#TypeError: methodoverload.something() missing 1 required positional argument: 'd'
# for overcome this we have move to below method

'''class methodoverload():
    def something(self,a=None,b=None,c=None,d=None):
        print(a,b,c,d)
obj=methodoverload()
obj.something(1,3,5,6)
obj.something(1,3,4)
obj.something(1,2)
obj.something()'''

'''class kiran():
    def output(self,a=None,b=None,c=None,d=None):
        print(a,b,c,d)
obj=kiran()
obj.output(1,3,4,5)
obj.output("L",3,4,5)
obj.output("k","y","h","t")
obj.output(1,4,)
obj.output()'''

# method overidding
'''class methodoverid():
    def output(self):
        print("this is method overrid")
class kiran(methodoverid):
    def output(self):
        print("this is child class")
obj=kiran()
obj.output()'''
# result = this is child class i.e only child class prints to  overcome this we move to below method

'''class methodoverid():
    def display(self):
        print("this is parent class")
class childd(methodoverid):
    def display(self):
        print("this is child class")
        super().display()    # this is imp
obj=childd()
obj.display()'''


'''class kiran():
    def result(self):
        print("this is kiran class")
class hyd(kiran):
    def result(self):
        print("this is hyderabad class")
        super().result()
obj=hyd()
obj.result()'''
# output=this is hyderabad class # first prints child class 
#        this is kiran class

'''class kiran():
    def display(self):
        print("this is super class")
class india():
    def display(self):
        print("this is base class")
class asia(kiran,india):
    def display(self):
        print("this is child class")
        super().display()
obj=asia()
obj.display()'''  
  #       ENCAPSULATION- binging of methods and variables is called class and that process is called encapsulation
  # there are two methods 1. private (__ double underscore)
  # 2. protected (_ single uderscore)


'''
class Gfather():
    def __init__(self,a):
        self__y=a
        print(self.__y)
class father(Gfather):
    def display(self):
        print(self.__y)
class child(father):
    def display1(self):
        print(self.__y)
obj=child(3)
obj.display1()
obj.display()
''' #doubt
# abstract method

'''from abc import ABC, abstractmethod
class parent(ABC):
    @abstractmethod
    def done(self):
        pass
    @abstractmethod
    def kiran(self):
        pass
class child(parent):
    def done(self,a):
        print("this is child",a)
    def kiran(self):
        print("this is another")
obj=child()
obj.done(10)
obj.kiran()   ''' 


        



