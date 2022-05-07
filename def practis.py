def sum1list():
    lst1 = [8,2,3,0,7]
    print(sum(lst1))

sum1list()

def maxnums(x,y,z):
    if x < y and y > z:
        print(y,"is greater" )
    elif y < z and z > x :
        print(z,"is greater ")
    elif z < x and x > y :
        print (x,"is greater")
    else :
        print("error")
        return

x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))


maxnums(x,y,z)

print("Do you want to continue?, type y/n")





