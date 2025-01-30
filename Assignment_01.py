# dictionary basic example 01

my_dict = {
#    "name" : "Bilal",
#    "class" : 10,
#    "age" : 17,
#    "subjects" : ["physics" , "maths" , "urdu" , "chemistry"],
#    "marks" : [74 , 66 , 58 , 87],   
}

# my_dict["name"] = "Haris"    overwrite value
# print(my_dict)

# dictionary basic example 02

info = {
#    "name" : "Haris",
#    "class" : "second_year",
#    "qualification" : "intermedia",
#    "subjects" : ["python" , "css" , "html"],
#    "topic" : ("dictionary" , "function"),
#    "age" : 20,
}

# print(info["topic"])

# dictionary basic example 03

capitals = {
#    "pakistan" : "Islamabad",
#    "india" : "New_delhi",
#    "japan" : "Tokyo",
#    "germany" : "Berlin",
#    "america" : "Washington D.C", 
}

# print(capitals["america"])
# capitals["Russia"] = "moscow"
# print(capitals)

# calculator Assignment

num1 = int(input("Enter Your First Number :"))
num2 = int(input("Enter Your Second Number :"))
operator = (input("Enter Your Operator (+,-,*,/) :"))

def calculator(num1 , num2 , operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        return "invalid operator"

result = calculator(num1 , num2 , operator)

print(result)


# data types
# 1.string
# 2.integer
# 3.boolean
# 4.list
# 5.tuple
# 6.dictonary

# student ={
#    "name": "Haris",
#    "class": 10,
#    "age": 18,
# }

# print(student["name"])
# student["Rollno"] = 4455
# print(student)


# static function

# Addition

x = 12
y = 15

def add():
    return(x + y)

sum = add()
print(sum)

# substraction
def sub():
    return(x - y)

sub = sub()
print(sub)

# multiple
def multiple():
    return(x * y)

mul = multiple()
print(mul)

# division
def division():
    return(x / y)

div = division()
print(div)  

# dynamic function
           
           #parameters
def greet(name,age,rollno):
    print("Assalam o alaikum" , name,"apki age kiya hai",age , rollno )

       # arguments
greet("Haris",20,311774)

# version 1.static function

# addition
num1: int = 30
num2: int = 10

def add():
    print(num1 + num2)

add()

# substraction
def sub():
    print(num1 - num2)

sub()

# multiple
def mutiple():
    print(num1 * num2)

mutiple()

# division
def div():
    print(num1 / num2)

div()

# version 2 dynamic function

def addition(num1:int , num2:int):
    return(num1 + num2)

print(addition(30,70))

result = 100
result = addition(30,70)
print(result)

final_result = 100 + 100
final_result = result + 100

print(final_result)

# substraction

def sub(num1:int , num2:int):
    return(num1 - num2)

print(sub(30,70))

result = 40
result = sub(30,70)

print(result)

final_result = 40 - 40
final_result = result - 40

print(final_result)


# Multiplication

def mul(num1:int , num2:int):
    return(num1 * num2)

print(mul(30,70))    
result = 2100
result = mul(30,70)

print(result)

final_result = 2100 * 2100
final_result = result * 2100

print(final_result)

# division

def div(num1:int , num2:int):
    return(num1 / num2)

print(div(30,70))
result = 0.428
result = div(30,70)

print(result)

final_result = 0.428 / 0.428
final_result = result / 0.428

print(final_result)
