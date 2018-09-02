# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = input("Enter file name: ")
fhand = open(fname, "r")
count = 0
dic = {}
list = []
sorted_list = []
for line in fhand:
    # if not line.startswith("From"):
    # 	continue
    if line.startswith("From "):
        # if not line.startswith("From:"):
        count = count + 1
        words = line.split()
        time = words[5]
        t_time = time.split(":")
        list.append(t_time[0])
        # print(time,t_time)

print(list)

for item in list:
    dic[item] = dic.get(item, 0) + 1

# print(dic)

sorted_list = (sorted([(k, v) for k, v in dic.items()]))

# print(sorted_list)

for aaa, bbb in sorted_list:
    print(aaa, bbb)
