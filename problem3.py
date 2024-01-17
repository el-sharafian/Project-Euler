import math

number = 600851475143
factors = []

def find_prime_factors(n):
    if(n%2 == 0):
        return False
    for i in range(2, int(math.sqrt(n))):
        if(n%i == 0):
            return False
    return True

for i in range(1, int(math.sqrt(number))):
    if(number % i == 0):
        flag = find_prime_factors(i)
        if(flag):
            factors.append(i)

for i in factors:
        print(i, end=" ")