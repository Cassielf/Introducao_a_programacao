a=8
b= a-2
if (b>=5):
    if (a>=7):
        b= a/2+4
        c= 3*a-b
    else:
        a=b+5
        c=b%3+2
elif(a==8):
    c=3+a*b
else:
    c=2*a-b

if (c%b>a):
    a= a+b
elif (b<a):
    b= 2*b+a
else:
    b=b%a+1
c= a//5+1

print (a,b,c)
