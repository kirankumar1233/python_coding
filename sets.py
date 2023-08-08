# 1. The elements in the set cannot be duplicated
# 2.the elements in the set are mutable
# 3.there is no index attached to any element in a python set so it does'nt support slicing
# 4.set is created by placing all the elements in curly  brackets and seperated with comma(,) or by using builtin set set function

'''kiran={1,5,3,6,3,3,9,8,1,10,7,}
print(type(kiran))
print(kiran)'''



'''hyd={1,4,6.6,7,'k','l','kiran'}
print(type(hyd))
print(hyd)
hyd.add("kiran") #it cannot added because set does'nt support duplicatae values
print(hyd)'''

'''bell={1,4,6,7,3,8,'f','6',"kiran",8.8,99,0}
a=type(bell)
print(a)
bell.add("man")
print(bell)
bell.pop() #by using pop we cannot remove our requirments it delets only first element
print(bell)
bell.remove('man') #by using remove we can remove any element
print(bell)
bell.remove("kiran") #remove takes exatly one argument
print(bell)
bell.clear()
print(bell)
bell.update({1,5,6,7,7,"k","hyd"})
print(bell)
bell.copy()
print(bell)
bell.pop()
print(bell)
bell.update({2,5,99}) '''  #after using copy we cannot add anything to set



'''kiran={1,4,6,7,8,}
print(type(kiran))
kiran.pop()
print(kiran)'''

'''kiran={1,5,6,7,9.9,0,8,7j,7j,'k','kiran',1,3}
#print(type(kiran))
#print(kiran)
#a=type(kiran)
#print(a)
#kiran.add(5)
#print(kiran)
a=kiran
a.add('python')
print(a)'''

#atp={1,5,6,7,7,6,7,5.6,'kiran','python',8j,'p'}
#atp.pop()
#print(atp)

#atp.remove(8j)
#print(atp)
#atp.update(['rapthadu'],['hyderabad']) #adds total word as single word
#print(atp)
#atp.update('kumar','rapthadu')  # adds each character as a element
#print(atp)

#rams={1,6,7,8,0,8.6,8.6,9,4,1,6,0,5,7,7.3,88,53,64,1,1,1,}
#print(min(rams))
#print(max(rams))

from ctypes import Union


''''str1={1,5,6,7,9,6,9,1,}
str2={4,6,7,7,9,21,64,67,}
print(str1.union(str2))
print(str2.intersection(str1))
print(str1.difference(str2))
print(str1.symmetric_difference(str2))'''

#kiran=input(set)
#print(min(kiran))


'''s1={1,3,4,6,7,}
s2={2,5,6,7,8,}
print(s1.union(s2))
print(s1.intersection(s2))'''


'''s1={1,3,4,5,6,}
s2={4,5,6,8,4}
print(s1.difference(s2)) # common elements eleminated and only prints first set data/elements
print(s1.symmetric_difference(s2)) # opposite to intersection i.e except common elements remining elements of both sets prints
print(s1.issubset(s2))'''


'''s1={1,3,4,5,6,7,8}
s2={1,3,4,5,6,7,8,9,10}
print(s2.issubset(s1))
print(s1.issubset(s2))
print(s2.issuperset(s1))
print(s1.issuperset(s2))'''


'''s1={1,2,3,4,5,6}
s2={7,8,9,10,11}
print(s1.isdisjoint(s2))
print(s2.isdisjoint(s1))''' # if both the sets have different elements it is called disjoint

'''mahi={1,2,3,4,5,6}
mahi.apend("sampoo")
print(mahi) '''#set does'nt support append

'''mahi=[1,2,4,3,5,6]
mahi.append('sampoo')
print(mahi)
vinay=frozenset(mahi)
print(vinay)'''

'''mahi=[1,3,4,5,6,7]
samanta=frozenset(mahi)
c=samanta.append('atp')
print(c)'''