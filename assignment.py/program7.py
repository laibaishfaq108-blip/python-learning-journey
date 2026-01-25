while True:
    n=input("enter a number or 'quitt':")
    if n.lower()=="quit":
        break
    num=int(n)
    if (num > 0):
     print("positive")
    elif(num < 0):
     print("negative")  
    else:
     print('zero') 
