# def add_numbers(n1, n2):
#     result = n1 + n2
#     print("The sum is = ", result)

# num1 = int(input("Enter the num1 = "))
# num2 = int(input("Enter the num2 = "))
# add_numbers(num1,num2)

# def my_name(name):
#     print(name)
# my_name("nagraj")

# def size(x,y):
#     if x > y :
#         print("x is greater")
#     else :
#         print("y is greater")
#         if y > x :
#             print("Bigger")
        
# x = int(input("X = "))
# y = int(input("Y = "))
# size(x,y)

# def add(x,y):
#     print("the sum of", x, "and", y, "is", x+y)
# x = 9
# y = 10
# add(x,y)


# def size(x,y,z):
#     if x > y and y < z :
#         print("y is small")
#     elif y > z and z < x :
#         print("z is small")
#     elif z > x and x < y :
#         print("x is small")
#     elif x == y == z:
#         print("equal")
#     else :
#         print("error")

# x = int(input("x = "))
# y = int(input("y = "))
# z = int(input("z = "))
# size(x,y,z)

# print("hello world")

def count1():
    list1 = [2,3,4,5,6]
    for i in list1:
        if i < 4 :
            print("yes im small")
        elif i > 4 :
            print("yes im big")
        elif i == 4 :
            print("equal")
        print(type(i))
        
count1()