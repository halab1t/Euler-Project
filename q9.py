from q3 import is_prime
import numpy as np
from math import sqrt

def factor(num):
    prime, factor = is_prime(num)
    prime_factors = []
    nonprime_factors = []
    while not prime:
        num = num / factor 
        nonprime_factors.append(num)
        prime_factors.append(factor)

        prime, factor = is_prime(num)

    prime_factors.append(num)

    return prime_factors, nonprime_factors

p_f, np_f = factor(1000)

print(p_f)
print(np_f)

for nonprime_factor in np_f:
    prime_f, nonprime_f = factor(nonprime_factor)

    print(prime_f)
# something will divide something else evenly if the prime factors of said thing form a subset of the prime factors of the number being divided

def co_prime(a, b, c):

    prime_factor_a, _ = factor(a)
    prime_factor_b, _ = factor(b)
    prime_factor_c, _ = factor(c)
    
    all_factors = set(prime_factor_a + prime_factor_b + prime_factor_c)

    if len(all_factors) != len(set(prime_factor_a)) + len(set(prime_factor_b)) + len(set(prime_factor_c)):

        return False
    return True

def sum_from_list(num, num_list):

    for n in num_list:
        if num - n in num_list:
            return True, num - n, n

    return False, -1, -1

def is_subset(sub_set, mother_set):
    cp_mother_set = mother_set[:]

    for num in sub_set:
        if num in cp_mother_set:
            cp_mother_set.remove(num)
        else:
            return False

    return True

to50 = range(1, 51)
squares_to50 = [n**2 for n in to50]

for square in squares_to50:

    sum_of_squares, square1, square2 = sum_from_list(square, squares_to50)
    
    if sum_of_squares:
        a, b, c = sqrt(square2), sqrt(square1), sqrt(square)
        sum_abc = a + b + c
        if 1000 % sum_abc == 0:

            print("SUCCESS!")
            print(f"a = {a} b = {b} c = {c}, sum is {sum_abc}")
