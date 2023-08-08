
# single inheritance - it contains only one parent class and only child class

'''class Parent():
    def output(self):
        print("this is parent")
class Child(Parent):
    def result(self):
        print("this is child class")
obj=Child()
obj.output()
obj.result()'''  

'''class Super():
    def kiran(self):
        print("THIS IS SUPER CLASS")
class Duper(Super):
    def varuna(self):
        print("This is varuna class")
kir=Duper()
kir.kiran()
kir.varuna()'''

'''class Hyd():
    def output(self):
        print("this is hyderabad class")
class Bgl(Hyd):
    def result(self):
        print("this is bangalore class")
super=Bgl()
super.output()
super.result()'''


# Multiple inheritance - it has two or more parent classes and only one child class


'''class Father():
    def output(self):
        print("This Is Father Class")
class Mother():
    def result(self):
        print("This Is Mother Class")
class Child(Father,Mother):
    def kiran(self):
        print("This Is Child Class")
obj=Child() # object name = class name
obj.kiran()
obj.result()
obj.output()'''


'''class Ashoka():
    def vinay(self):
        print("This is super class")
class Sivaji():
    def gandhi(self):
        print("this is base class")
class Nehru(Sivaji,Ashoka):
    def modi(self):
        print("This is derivative class")
rahul=Nehru()
rahul.vinay()
rahul.gandhi()
rahul.modi()'''



'''class Sun():
    def output(self):
        print("this is sun class")
class Moon():
    def result(self):
        print("this is moon class")
class Star():
    def tree(self):
        print("this is star class")
class Cloud():
    def air(self):
        print("this is cloud class")
class Rain(Sun,Moon,Star,Cloud):
    def water(self):
        print("this is rain class")
crops=Rain()
crops.output()
crops.result()
crops.tree()
crops.air()
crops.water()'''


# multilevel inheritance - it has more than two parent and children class

'''class Grandfather():
    def output(self):
        print("This is grandfather class")
class Father(Grandfather):
    def result(self):
        print("this is father class")
class Child(Father):
    def kiran(self):
        print("this is child class")
obj=Child()
obj.output()
obj.result()
obj.kiran()'''

'''class Greatgrandfather():
    def india(self):
        print("this is great grandfather class")
class Grandfather(Greatgrandfather):
    def output(self):
        print("This is grandfather class")
class Father(Grandfather):
    def result(self):
        print("this is father class")
class Child(Father):
    def kiran(self):
        print("this is child class")
obj=Child()
obj.india()
obj.output()
obj.result()
obj.kiran()'''

# Hierarchial inheratence one parent class and multiple child class

'''class Father():
    def output(self):
        print("this is father class")
class Child1(Father):
    def outputchild1(self):
        print("this is child1 class")
class Child2(Father):
    def outputchild2(self):
        print("this is child2 class")
obj1=Child1()
obj2=Child2()
obj1.output()
obj1.outputchild1()
obj2.output()
obj2.outputchild2()'''

'''class Mango():
    def outputm(self):
        print("this is mango class")
class Apple(Mango):
    def outputa(self):
        print("this is Apple class")
class Orange(Mango):
    def outputo(self):
        print("this is Orange class")
class Guva(Mango):
    def outputg(self):
        print("this is Guva class")
obj1=Apple()
obj2=Orange()
obj3=Guva()
obj1.outputm()
obj1.outputa()
obj2.outputo()
obj3.outputg()''' 





