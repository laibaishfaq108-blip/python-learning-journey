#WAP to enter marks of 3 subject from the user and store them in dictionary.
dict={}
a=input("Enter phy marks:")
b=input("Enter maths marks:")
c=input("Enter english marks:")
dict.update({"phy ":a})
dict.update({"maths":b})
dict.update({"english":c})
print(dict)

