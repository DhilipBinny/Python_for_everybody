# 9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fname = input("Enter file name: ")
fhand = open(fname,"r")
count = 0
dic={}
list=[]
for line in fhand:
    # if not line.startswith("From"):
    # 	continue
    if line.startswith("From "):
        # if not line.startswith("From:"):
            count = count + 1
            words = line.split()
            email = words[1]
            list.append(email)
            print(email)
print(list)

for item in list:
    dic[item] = dic.get(item, 0) + 1

# print(dic)

bigcount=None
bigword=None
for word, count in dic.items():
    if bigcount is None or count> bigcount:
        bigword = word
        bigcount= count
print(bigword,bigcount)
