def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
print(max_of_three(3, 6, -5))

a = str(input("enter a string : "))
b = str(input("enter the character to count : "))
count = sum(map(lambda x : 1 if b in x else 0, a))
print("Count of given character is : " + str(count))
