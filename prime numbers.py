n=[]
num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
num3=int(input("Enter 3rd number:"))
num4=int(input("Enter 4th number:"))
num5=int(input("Enter 5th number:"))
n.append(num1)
n.append(num2)
n.append(num3)
n.append(num4)
n.append(num5)
print("prime numbers are:")
for i in n:
    if(i>1):
      for num in range(2,i):
         if(i%num==0):
            break
      else:
       print(i)