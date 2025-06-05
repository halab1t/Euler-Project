function is_prime(num)
	if num <= 1
		return false, 1
	end

	for i in 2:floor(Int, sqrt(num))
		if num % i ==0
			return false, i
		end
	end

	return true, -1

end

function factor(num)
    if num == 1
	    return [1]
    end

    prime, factor = is_prime(num)
    factors = [1, num]
    prev_factor = 1

    while !prime
	prev_factor *= factor 
        num = div(num, factor)
        push!(factors, num)
        push!(factors, prev_factor)

        prime, factor = is_prime(num)
    end

    return factors
end

