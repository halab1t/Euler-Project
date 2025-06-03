function sieve_of_eratosthenes(limit)

	is_prime = trues(limit)
	is_prime[1] = false

	for i in 2:floor(Int, sqrt(limit))
		if is_prime[i]
			for multiple in i*i:i:limit
				is_prime[multiple] = false
			end
		end
	end

	return findall(is_prime)

end

primes = sieve_of_eratosthenes(2_000_000)
sum_primes = sum(primes)

println(sum_primes)
				
