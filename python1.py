x=input("Enter the number or alphabate ")
if(ord(x)>=97 and ord(x)<=123):
    print("given input is alphate and is a Small alphabate")
elif(ord(x)>=65 and ord(x)<=91):
    print("given input is alphate and is a Capital alphabate")
elif(ord(x)>=48 and ord(x)<=57):
    print("given input is number")
