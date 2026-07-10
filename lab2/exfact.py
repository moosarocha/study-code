result = 1
n = 5

def factorial(n):
    result = 1
    for i in range(n):
        result *= (i+1)
def factorialr(n):
    if n <= 1 :
        return 1
    else:
        return n * factorialr(n-1)

#for i in range(n):
#    result *= (i+1)

print (f"{n}! = {result}")