x=input("Enter the alphanumeric  ")
y=[x[i:i+1] for i in range(0,len(x),1)]
r1=[]
r2=[]
r3=[]
r4=[]
r5=[]
r6=[]
for i in y :
    if(ord(i)>=97 and ord(i)<=123):
        r1.append(i)
    elif(ord(i)>=65 and ord(i)<=91):
        r2.append(i)
    elif(ord(i)>=48 and ord(i)<=57):
        r3.append(i)
r1.sort()
r2.sort()
r3.sort()

for j in r3 :
    if(ord(j)%2==0):
        r4.append(j)
    else :
        r5.append(j)
r4.sort()
r5.sort()        

r6=r1+r2+r5+r4
for k in r6 :
    print(k,end="")
