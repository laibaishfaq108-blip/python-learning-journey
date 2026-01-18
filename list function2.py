#WAP to check if a list contain a palindrome of elements.
list=[1,2,3,2,1]
copy_list=list.copy()
copy_list.reverse()
if(copy_list==list):
    print("palindrome")
else:
    print("non-palindrome")