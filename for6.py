n=int(input("dati n: "))
i=1
s=0
s2=0
s3=0
pr=1
div=0
s4=0
s5=3
for i in range(1,n+1):
    s=s+i
print(s)
n=int(input("dati n: "))
for i in range(1,n+1):
   s2=((i-1)*i)+s2
print(s2)
n=int(input("dati n: "))
for i in range(1,n+1):
    pr*=i
    s3+=pr
print(s3)
s3=0
n=int(input("dati n: "))
for i in range(1,n+1):
   i=str(i)
   i=int(i+"2")
   s3=i+s3
print(s3)
n=int(input("dati n: "))
for i in range(1,n+1):
    div=i/(i+1)
    s4=div+s4
print(s4)
n=int(input("dati n: "))
for i in range(3,n+1):
    i=str(i)
    i=int("2"+i)
    s5=s5+i
print(s5)


    
   
   

    
