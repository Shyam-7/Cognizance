#Question-3
import pandas as p
table = []

count = int(input("Enter number of students: "))

for i in range(0, count):
    print("Enter details of each student in R.No., Name, Marks format: \n")
    table.append([])
    for j in range(0, 4):
        if j==0:
            print()
            print('Enter R.No')
            Enter_details = input()
        elif j==1:
            print()
            print('Enter Name')
            Enter_details = input()
        elif j==2:
            print()
            print('Enter Marks')
            Enter_details = input()c
        else:
            Enter_details = ''
        table[i].append(Enter_details)

print(table)
b = p.DataFrame(table, columns=["R.No.", "Name", "Marks", ""])
b = b.set_index(['R.No.', 'Name', 'Marks'])
print(b)
print(b[1:2])
