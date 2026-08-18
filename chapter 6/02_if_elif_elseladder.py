a = int(input("enter your age: "))

#if elif else lader

if(a>=18):
    print("you are above the age of consent")
    print("Good for you.")

elif(a<0):
    print("you are entering an invalid age")

elif(a==0):
    print("you are entered 0 which is not a valid age")

else:
    print("you are below the age of consent")


print("end of program")