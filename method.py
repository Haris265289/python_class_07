# def func(a,b):
#    return a + b

# c = func(2,3)
# print(c)


# def box(a,b=4):
#    return a + b

# sum = box(10)
# print(sum)


# 1.string method:

new_str = "my name is haris.my nationality is pakistani"

# capitalize: ka kam hai ke ye first alphabet ko capital krde ga.
print(new_str.capitalize())

# count: count sy murad hum word ya letter ko count kr skte hai. 
print(new_str.count("is"))

# length: length sy hum word ya sentence ki length maloom kr skte hai.
print(len(new_str))

# find: find sy hum koi bhi word ya sentence ko search kr skte hai.
print(new_str.find("my"))

# index: index sy hum koi bhi word ya sentence ka index maloom kr skte hai.
print(new_str.index("is"))

# replace: replance ke liye pehle ap old keys likhy phir new keys likhe. 
print(new_str.replace("pakistani" , "russian").upper())

#  string method example 2

info_str = "my name is bilal.my age is 20,and my class is matric"

print(info_str.capitalize())

print(info_str.count("class"))

print(len(info_str))

print(info_str.find("name"))

print(info_str.index("age"))

print(info_str.replace("bilal" , "haris").upper())


# 2. list method 

my_friend_list = ["shayan" , "shoaib" , "sani" , "hammad" , "osama"]

# append:

my_friend_list.append("haris")
print(my_friend_list)

# insert:

my_friend_list.insert(3,"hassan")
print(my_friend_list)

# reverse:

my_friend_list.reverse()
print(my_friend_list)

# pop:

my_friend_list.pop(2)
print(my_friend_list)

# sort:

my_friend_list.sort()
print(my_friend_list)

# extend:

new_friend = ["hassan" , "zoya"]
print(my_friend_list)
new_friend.extend(my_friend_list)
print(new_friend)

# 3. Dictionary method

info = {
    "name": "Haris",
    "age": 20,
    "subject": "python",
    "topic": "dictionary",
}
print(info)
print(info["topic"])

# keys:

print(info.keys())

# values:

print(info.values())

# items:

print(info.items())                     # as a tuple form

# get:

print(info.get("age"))

# pop:

print(info.pop("name"))

# update:

new_info = {"city": "karachi"}
new_info2 = {"country": "pakistan"}

print(new_info.update(new_info))
print(new_info2.update(new_info2))

# clear:

info.clear()
print(info)

# 4. tuple method

fruits_list = ("apple" , "banana" , "orange" , "mango" , "cherry" , "mango")

print(fruits_list)

# count:

print(fruits_list.count("mango"))


# index:

print(fruits_list.index("cherry"))
