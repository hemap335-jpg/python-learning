a=int(input("enter an age:"))
if(a>=1 and a<=12):
    print("child")
elif(a>=13 and a<=17):
    print("teen")
elif(a>=18 and a<=19):
    print("adult+teen")
elif(a>19):
    print("senior citizen")
else:
    print("retired")
