# are you eligible for voting
age = int(input("enter your age "))
if age >18:
    print("you are eligible for voting")
elif age == 18:
    conf = input("do you have voter ID")
    if conf == "yes":
        print("you can vote")
    elif conf == "no":
        print("apply for voter ID")
    else:
        print("invalid output")
else:
    print("you are a juniar")