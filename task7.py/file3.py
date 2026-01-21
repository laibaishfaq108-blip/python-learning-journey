#From a file containing numbers separated by comma, print the count of even number
count=0
with open("practice2.txt","r") as f:
    data=f.read()

    nums=data.split(",")
    for val in nums:
        val=val.strip()
        if(val==""):
            continue
        if(int(val) % 2 == 0):
            count += 1
print(count)