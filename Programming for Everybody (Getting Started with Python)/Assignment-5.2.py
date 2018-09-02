

# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None
user_value =[]

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        f_num = float(num)
    except:
        print("Invalid input")
        continue
    user_value.append(f_num)


for i in user_value:
    if smallest is None:
        smallest = i
    elif i < smallest:
        smallest = i

for i in user_value:
    if largest is None:
        largest = i
    elif i> largest:
        largest = i

for i in user_value:
    if smallest is None and largest is None:
        smallest = i
        largest=i
    elif i > largest:
        largest = i
    elif i< smallest:
        smallest = i


# print(user_value)
print("Maximum is ", int(largest))
print("Minimum is ", int(smallest))