import csv
with open("students.csv","w") as f:
    writer=csv.writer(f)
    writer.writerow(["name","age","city","\n"])
    writer.writerow(["laiba","20","FSD"])
    print("csv file created")