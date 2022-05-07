# a = str(input("enter a string : "))
# b = str(input("enter the character to count : "))
# count = sum(map(lambda x : 1 if b in x else 0, a))
# print("Count of given character is : " + str(count))

from collections import Counter

a = str (input("Enter the all characters : "))
my_counter = Counter(a)
print(my_counter)





