expenses=[]
for i in range(5):
    n=int(input("Enter your expenses:"))
    expenses.append(n)
    sum=0
    for i  in expenses:
        sum+=i
ave=sum/5
print("total:",sum)
print("average:",ave)        
