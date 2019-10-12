print("begin")
i=input("enter a positive no")
x=int(i)
if x<10:
    print("given no is one digit no")
elif x<100:
    print("given no is two digit no")
elif x<1000:
    print("given no is three digit no")
else:
    print("given no is four digit no")
print("end")
