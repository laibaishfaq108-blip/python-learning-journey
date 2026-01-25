
salary=int(input("Enter your salary:"))
if(salary<=30000):
  print("Your tax rate is 5%")
elif(salary>=30000 and salary<=70000):
  print("Your tax rate is 15%")
elif(salary>=70000):
  print("Your tax rate is 25%")
else:
 print("invalid input")
 