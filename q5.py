from q3 import is_prime
from math import prod

divisors = list(range(1,21))
print(divisors)

primes = []
non_primes = []

for div in divisors:
    prime, _ = is_prime(div)

    if prime:
        primes.append(div)
    else:
        non_primes.append(div)
def factors_needed(arr, num):
    factors = arr[:]
    extra_factors = []
    prime, factor = is_prime(num)
    while not prime:
       
        if factor not in factors:
            extra_factors.append(factor)
        else:
            factors.remove(factor)

        num = num / factor
        
        if num == 1.0:
            return extra_factors

        prime, factor = is_prime(num)

    if num not in factors:
        extra_factors.append(num)

    return extra_factors

for num in non_primes:
    extra_factors = factors_needed(primes, num)
    primes = primes + extra_factors
print(primes)
print(prod(primes))
