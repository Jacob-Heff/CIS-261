# Jacob Heffington
# CIS261
# Iteration and Recursion

def iteration(num):
    factorial = 1
    if num == 0:
        print(num,"! = ", 1)
    else:
        for i in range(1,num + 1):
            factorial = factorial*i
        print(num, "! = ", factorial)

def recursive(num, factorial, track):
    if num == 0:
        return str(num) + "! = 1"
    elif num == 1:
        return str(num) + "! = " + str(factorial)
    elif track != 1:
        return recursive(num,factorial*(track-1),track-1)
    else:
        return str(num) + "! = " + str(factorial)


print("Factorial results using an interative function")
iteration(0)
iteration(5)
iteration(10)
iteration(25)
iteration(50)
iteration(100)
print("Factorial results using an recursive function")
print(recursive(0,0,0))
print(recursive(5,5,5))
print(recursive(10,10,10))
print(recursive(25,25,25))
print(recursive(50,50,50))
print(recursive(100,100,100))