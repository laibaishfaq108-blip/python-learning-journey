n=[]
for i in range(10):
    num=int(input("Enter a number:"))
    n.append(num)
    even_count=0
    odd_count=0
    for i in n:
        if(i%2==0):
            even_count+=1
        else:
            odd_count+=1
            
print("There are",even_count,"even numbers.")
print("There are",odd_count,"odd numbers.")                