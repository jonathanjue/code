f = int(input("how long do you want the Fibonacci Sequence to go?  "))


my_list = list()
my_list.append(0)
my_list.append(1)
for i in range(1,f):

    my_list.append(my_list[i]+my_list[i-1])

    # I want to append something to the list by adding the last two 
    # entrys in the list
    # use [] and the index like my_list [0]
    
    
    
    
    
print(my_list)
