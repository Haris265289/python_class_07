# range function / Method

# Numbers = [1,2,3,4,5,6,7,8,9,10]
# x = range (1,5) # 1,2,3,4

# 1.starting point
# 2.condition
# 3.increment
# print(Numbers)
# print(list(x))

# Aam zindagi

# print("2 x 1 = " , 2 * 1)
# print("2 x 2 = " , 2 * 2)
# print("2 x 3 = " , 2 * 3)
# print("2 x 4 = " , 2 * 4)
# print("2 x 5 = " , 2 * 5)
# print("2 x 6 = " , 2 * 6)
# print("2 x 7 = " , 2 * 7)
# print("2 x 8 = " , 2 * 8)
# print("2 x 9 = " , 2 * 9)
# print("2 x 10 = " , 2 * 10)

# mintos zindagi

# 1. for loop

for num in range(1,11):
    print(f"2 x {num} = {2 * num}")  # fstring

for i in range(1,11):
    print(f"3 x {i} = {3 * i}")

for h in range(1,11):
    print(f" 4 x {h} = {4 * h}")

for a in range(1,11):
    print(f"5 x {a} = {5 * a}")

for x in range (1,11):
    print(f"6 x {x} = {6 * x}")    

# 2. while loop

# while condition ya true hogi ya phr False

num = 1

while num <= 10:
    print("num")
    num = num + 1

name = "hammad"

names: list [str] = ["haris" , "shayan" , "sani" , "shoaib" , "hammad" , "osama" ]

print(names)
names [4] = "bilal"
print(names)

# tuple

# num = 2

# num: list [int] =(2,4,6,8,10)
# print(num)
# print(num[3])

fruits_name = "cherry"

fruits_name: list [str] = ("apple" , "banana" , "orange" , "cherry" , "pineapple")

print(fruits_name)
print(fruits_name[4])




