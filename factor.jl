function factor(num)
    prime, factor = is_prime(num)
    prime_factors = []
    nonprime_factors = []

    while !prime
        num = div(num, factor)
        push!(nonprime_factors, num)
        push!(prime_factors, factor)

        prime, factor = is_prime(num)
    end

    push!(prime_factors, num)
    return prime_factors, nonprime_factors
end

