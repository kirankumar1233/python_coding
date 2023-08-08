# STRING
#kiran='anantapur'
#print(kiran)

#krish="hyderabad"
#print(krish)

#TDP='''telengana'''
#A=TDP
#print(A)

#a='pune'
#b="maharastra"
#c='''delhi'''
#print(type(a),type(b),type(c))

'''a='DEHLI IS IN INDIA AND IT IS THE CAPTIAL OF INDIA'
print(type(a))
b=a.lower()
print(b)
print(a.count('INDIA'))
print(a.count('DEHLI'))'''

#print(dir(str)) #to find out string methods and constructors

'''kiran="rama is a good boy"
a=kiran.split() #split converts string to list
print(a)
print(kiran.startswith('rama'))
print(kiran.endswith('boy'))
print(kiran.count('rama'))# it tells how many tims string repeats
print(kiran.upper()) 
a=kiran.find('kiran')# find=unknown string output= -1 #index(unknown string) out put error
print(a) #it tells index of a particular string'''

''''d="hai {a} how are you".format(a="kiran")
print(d)

k="hello {h} where are you ".format(h="world")
print(k)'''
'''j="congratulations {m} you got selected as a junion engineer .ALL THE BEST.".format(m="KIRAN KUMAR")
print(j)

z="hai mr.{y} how are you doing".format(y="KIRAN")
print(z)'''

'''names=['kiran','varun','anil','vinay','ajay','charan','rajesh']
for i in names:
    d="hai {a} how are you".format(a=i)
    print(d)''' #use for bulk amount of messages sent



'''a='kiran'
d=f"hai {a} meeru inka tiffen cheyaleda meekosam 40% offfer"
print(d)''' #advanced method

'''k='hyderabad'
a=k.isalpha()
print(a)'''

'''g='Bengaluru'
print(g.isnumeric())
print(g.isalpha())
print(g.isalnum())
print(g.islower())
print(type(g))
print(g.istitle())'''

'''atp="this is mango"
#print(len(atp))
k=atp.strip()
print(len(k))
print(k)'''


'''k="     india is my country     " 
print(k)
print(len(k))
u=k.strip() #reduces white spaces
print(len(u)) 
print(u)
print(k.lstrip()) # left strip
print(k.rstrip())''' # right strip

#kiran="we are indians"
#print(kiran.title()) # it prints every strins first letter should be caital letter

#kiran="my name is kiran kumar"
#print(kiran.replace('kiran','vinod'))
#print(kiran.replace('kumar','aggrwal'))
#print(kiran.replace('kiran kumar','vinod sharma'))

'''kk="vinod kumar"
print(kk.removeprefix("vinod"))
print(kk.removesuffix('kumar'))'''

'''j="this is pen"
l="this is book"
k=j.join(l)
print(k)  '''   #doubt


'''print("hai")
print('hai')'''


'''a="hello, World"
print(a[0])
print(a[7])
print(a[9])'''

#for i in "kwivi":
 #   print(i)

#for j in "kiran kumar":
 #   print(j)


#for n in "indian_sub_continent":
 #   print(n)


'''h="hello world"
j="welcome to world"
print(len(j,),len(h))'''

'''text="the best things in life are free"
print("free" in text)
print("kiran" in text)
print("best" in text)'''

'''a= "hello world"
b="welcome to world"
print(a[0:4])
print(b[4:8])'''


'''h='Hello, world'
print(h[:5])
print(h[2:])
print(h[-5:-2])'''


'''a='welcome to world'
b='Hello World'
print(a.upper())
print(b.upper())'''

'''a='   Hello WorLD    '
print(a)
#print(a.lower())
#print(a.upper())
print(a.strip())'''

#a= "hello world"
#print(a.replace("world","india"))

'''h='welcome, to ,the, world'
j="hello, world"
print(j.split(","))
print(h.split(","))'''

a='free fire of india'
print("free" not in a)
print("free" in a)