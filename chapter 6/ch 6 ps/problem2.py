marks1 = int(input("enter markas 1:"))
marks2 = int(input("enter markas 2:"))
marks3 = int(input("enter markas 3:"))

# Check for total percentage
total_percentage =(100*(marks1 + marks3 + marks2))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("you are pass", total_percentage)

else:
    print("you failed, try again", total_percentage)