# file handling

'''kiran=open('projects/kiran98.txt','r')
k=kiran.read()
print(k)
kiran.close()'''


'''kiran=open("projects/kiran98.txt",mode="r")
c=kiran.readline() # it prints only first line
print(c)
kiran.close()'''

'''kiran=open("projects/kiran98.txt",mode="r")
c=kiran.readlines() # it prints all the data in list format
print(c)
kiran.close()'''

'''kiran=open('projects/kiran98.txt',mode='w')
kiran.write("this is hyderabad") # it over writes so data losses here
kiran.close()'''
'''
kiran=open('projects/kiran98.txt',mode='a')
kiran.append("this is bangalore")
kiran.close()'''

'''kiran=open('projects/kiran98.txt',mode='r+')
c=kiran.read()
print(c)
kiran.write("this is bangalore") #here not replace jst append
kiran.close()'''

'''kiran=open('projects/kiran98.txt',mode='w+')
kiran.write("this is pune")
g=kiran.read()
print(g) # w+ replaces the data
kiran.close()'''

'''hyd=open('projects/kiran98.txt','r')
hyd.read(3)
print(hyd.tell())
hyd.seek(0)
print(hyd.tell())
hyd.close()'''
# tell it tells the cursor position
# seel it changed the cursor position
