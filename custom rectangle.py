#####
#   #
#   #
#####

# width = int(input("how wide do you want your rectangle to be?  "))
# height = int(input("how wide do you want your rectangle to be?  "))

width = int(input("how wide do you want your rectangle to be?  "))
height = int(input("how tall do you want your rectangle to be?  "))
fill = (input("what do you want your rectangle to be filled with  "))
border = (input("what do you want the bordor of the rectangle to be  "))
w = width
h = height
f=fill
b=border



i= 0
print(w*b)
while i<h-2:
    print(b+((w-2)*f)+b)



    i = i +1
print(w*b)