
#below is a classis recursion example
def factorial(n):
    if n <= 1: # base case 
        return 1
    return n* factorial(n-1) # recursive call


print(factorial(3))


