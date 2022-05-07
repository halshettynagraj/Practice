Char1 = input("Enter the String = ")

dict1 = {}

for i in Char1:
    if  i in dict1:
        dict1[i] += 1
    else :
        dict1[i] = 1

print("char : " + str(dict1))

