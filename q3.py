import math 

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def is_prime(num):
    if num <= 1:
        return False, 1

    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False, i

    return True, -1

def largest_prime_factor(num):
    
    factors = [] 
    prime_num, factor = is_prime(num)

    if prime_num:
        return num
    
    factors.append(factor) 
    quotient = num

    while not prime_num:
        quotient = quotient / factor
        prime_num, factor = is_prime(quotient)

    factors.append(quotient)
    print(factors)

    return max(factors)

print(largest_prime_factor(13195))
print(largest_prime_factor(600851475143))


