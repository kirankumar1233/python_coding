print("                  CALCULATOR           ")

print("*"*50)
a=float(input("enter the VALUE:"))
b=float(input("enter the value:"))
c=input("enter the operator:")
d=a+b
e=a-b
f=a*b
g=a/b
h=a%b
if c=="+":
    print("addition= ", d)
    print("*"*50)
elif c=="-":
    print("substraction:",e)
    print("*"*50)
elif c=="*":
    print("multiplication:",f)
    print("*"*50)
elif c=="/":
    print("division:",g)
    print("*"*50)
elif c=="%":
    print("reminder:",h)
    print("*"*50)