#Q. Given an integer,n, perform the following conditional actions:

#=>If  is odd, print Weird
#=>If  is even and in the inclusive range of  2 to 5 , print "Not Weird"
#=>If  is even and in the inclusive range of 6 to 20, print "Weird"
#=>If  is even and greater than 20, print "Not Weird"

n=int(input("number:"))
if n%2==0:
    if n>=2 and n<=5:
        print("not weired")
    elif n>=6 and n<=20:
        print("weired")
    else:
        print("not weired")
else:
    print("weired")

##Output:
##    number:6
##    weired

