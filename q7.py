from q3 import is_prime

no_prime = 0
i = 1
while no_prime < 10001:
    i += 1
    prime, _ = is_prime(i)
    if prime:
        no_prime += 1

print(i)
