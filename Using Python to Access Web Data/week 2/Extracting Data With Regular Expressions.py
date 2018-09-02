# course 3 assignments
# Extracting Data With Regular Expressions

fname = input("Enter file name: ")
fhand = open(fname, "r")
import re
# count = 0
# dic = {}
list = []
sum =0
# sorted_list = []
for line in fhand:
    y = re.findall("[0-9]+", line)
    for i in y :
        list.append(i)
# print(list)
for i in list:
    sum = sum+int(i)

print(sum)
