#WAF to print the elements of a list in a single line.

def print_list(elements):
    for items in elements:
        print(items, end=" ")
    print()

elements=["house","cars","furniture","baggages"]

print_list(elements)  

