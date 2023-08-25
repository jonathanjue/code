v = int (input("type a number the program will fractorial it!  "))

product = 1
for i in range (1,v + 1):

    print(f"{product} x {i} ={product*i}")
    product = product * i
    
print(product)

