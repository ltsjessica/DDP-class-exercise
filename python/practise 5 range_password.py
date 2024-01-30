for x in range (5):
    print(x)

for x in range (5,10):
    print(x)

for x in range (5,10,2):
    print(x) 


correctpassword= "1234"
for chance in range(5):
    password = input("please enter password:")
    if password == correctpassword:
        print("correctpassword")
        break
    elif password != correctpassword and chance <4:
        print("incorrect password, please try again")
        print(f"there are {4-chance} remaining")
    else:
        print("you've entered incorrect password more than four times, your account has been locked")