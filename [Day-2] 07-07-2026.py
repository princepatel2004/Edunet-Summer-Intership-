# Dictionary - 5 Methods

student = {"name": "Prince", "age": 21}

# update() - Adds new key-value pairs or updates existing ones.
student.update({"city": "Surat"})
print("Update:", student)

# keys() - Returns all keys of the dictionary.
print("Keys:", student.keys())

# values() - Returns all values of the dictionary.
print("Values:", student.values())

# get() - Returns the value of the specified key.
print("Get:", student.get("name"))

# pop() - Removes the specified key and returns its value.
removed = student.pop("age")
print("Popped:", removed)
print(student)


# List - 5 Methods

numbers = [10, 20, 30]

# append() - Adds an element at the end of the list.
numbers.append(40)
print("Append:", numbers)

# extend() - Adds multiple elements to the end of the list.
numbers.extend([50, 60])
print("Extend:", numbers)

# insert() - Inserts an element at the specified position.
numbers.insert(1, 15)
print("Insert:", numbers)

# remove() - Removes the first occurrence of the specified element.
numbers.remove(30)
print("Remove:", numbers)

# pop() - Removes and returns the last element by default.
numbers.pop()
print("Pop:", numbers)


# Tuple - 5 Methods

t = (10, 20, 30, 20, 40)

# count() - Returns the number of occurrences of a value.
print("Count:", t.count(20))

# index() - Returns the index of the first occurrence of a value.
print("Index:", t.index(30))

# len() - Returns the total number of elements in the tuple.
print("Length:", len(t))

# max() - Returns the largest element in the tuple.
print("Maximum:", max(t))

# min() - Returns the smallest element in the tuple.
print("Minimum:", min(t))

# Set - 5 Methods

s = {1, 2, 3}

# add() - Adds a single element to the set.
s.add(4)
print("Add:", s)

# update() - Adds multiple elements to the set.
s.update([5, 6])
print("Update:", s)

# remove() - Removes the specified element from the set.
s.remove(2)
print("Remove:", s)

# discard() - Removes an element if present without giving an error.
s.discard(10)
print("Discard:", s)

# pop() - Removes and returns a random element from the set.
s.pop()
print("Pop:", s)


# If Statement: Executes a block only if the condition is True.
x = 10

if x > 5:
    print("If: x is greater than 5")

# If-Else : Executes one block if True, otherwise another block.
age = 18

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")

# If-Elif-Else - Checks multiple conditions in sequence.
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
else:
    print("Grade C")

# Nested If-Else - An if statement inside another if statement.
num = 12

if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    print("Negative Number")


# Break Example- Terminates the loop immediately.
for i in range(1, 6):
    if i == 4:
        break
    print("Break:", i)

# Continue Example - Skips the current iteration and moves to the next.
for i in range(1, 6):
    if i == 3:
        continue
    print("Continue:", i)


# Pass Example - Does nothing and acts as a placeholder.
for i in range(3):
    if i == 1:
        pass
    print("Pass:", i)


# Input Method - Takes input from the user as a string.
name = input("Enter your name: ")
print("Hello,", name)


# Range Function - Generates a sequence of numbers.
print("Range:")
for i in range(1, 6):
    print(i)

# Len Function - Returns the number of items in an object.
text = "Python"
print("Length:", len(text))


# Type Function - Returns the data type of an object.
a = 10
print("Type:", type(a))


# For Loop - Repeats a block for each item in a sequence.
print("For Loop:")
for i in range(5):
    print(i)


# While Loop - Repeats a block as long as the condition is True.
print("While Loop:")
i = 1
while i <= 5:
    print(i)
    i += 1
