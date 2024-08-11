# PART A
myList = [1,2,3,4,5,6,7,8]

myList2 = myList[1:]

myList2.append(9)
myList2.pop(2)
myList3 = myList2

print('myList3',myList3)
# END OF PART A

# PART B

# 1
# returns a number in a giving string
example_string = "hello world hello"
count_result = example_string.count("hello")
print("count('hello'):", count_result)

# 2
# it makes the code to false
endswith_result = example_string.endswith("world")
print("endswith('world'):", endswith_result)

# 3
# it returns the lowest index
find_result = example_string.find("world")
print("find('world'):", find_result)

# 4
# returns as an output to the user
join_result = ", ".join(["apple", "banana", "cherry"])
print("join(', '.join(['apple', 'banana', 'cherry'])):", join_result)

# 5
# replaces it with a new code
replace_result = example_string.replace("hello", "hi", 1)
print("replace('hello', 'hi', 1):", replace_result)

# 6
# splits a string into a substrings
split_result = example_string.split(" ")
print("split(' '):", split_result)

# 7
# the string breaks a line
splitlines_result = "line1\nline2\nline3".splitlines()
print("splitlines():", splitlines_result)

# 8
# returns true with the specified prefix otherwise its false
startswith_result = example_string.startswith("hello")
print("startswith('hello'):", startswith_result)

# 9
# removes leading characters
strip_result = "  hello world  ".strip()
print("strip():", strip_result)
# END OF PART B

# PART C
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
# END OF PART C

# PART D

def disStuInfo(schoolID, *firstName, **lastEmail):
    for name in firstName:
        if name in lastEmail:
            print(schoolID)
            print(name)
            print(lastEmail[name])
        else:
            print(schoolID)
            print(name)
            print("'unmatched'")

disStuInfo(10001, 'John', 'Petter', Smith='jSmith@gmail.com', Potter="Petter@yahoo.com", Doe="j@gmail.com")

# END OF PART D




