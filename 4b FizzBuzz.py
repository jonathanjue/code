#Write a Python program that prints numbers from 1 to 100. 
#For multiples of 3, print "Fizz" instead of the number, and for
#multiples of 5, print "Buzz". For numbers that are multiples of 
#both 3 and 5, print "FizzBuzz".



for i in range (1,100):

    if i % 3 == 0 and i % 5==0:
        print("fizzbuz")
    elif i % 3==0:
        print("fizz")
    elif i % 5== 0:
        print("buzz")

    else:
        print(i)



