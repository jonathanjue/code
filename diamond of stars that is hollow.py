

# l = 20-1

# i = 1
# while i <= 20:
#     print(l  * " " + "*" * 1)
#     l=l-1
#     i = i+1
# while j<=20:
#     print(j  * " " + "*" * 1)

#     j= j+1

width = int (input("how wide do you want your diamond(in 2d)?  "))




initial = width//2
j = initial
k= 1
start = j
while j>0:
    if j==start:
        print(j*" "+"*")
    else :
        print(j*" "+"*"+ k *" "+"*  ")
        k = k+2
    j=j-1

#bottom half
m=0
k=2*initial-1
while m<=initial:
    if m ==initial:
        print(m*" "+"*")
    else :
        print(m*" "+"*"+ k *" "+"*")
        k = k-2

    m=m+1



#         *
#        * *
#       *   *
#      *     *
#       *   *
#        * *
#         * 
