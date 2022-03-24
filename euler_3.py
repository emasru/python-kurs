def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return False

    return True

def trial_division(n: int) -> list[int]:
    """Return a list of the prime factors for a natural number."""
    a = []               # Prepare an empty list.
    f = 2                # The first possible factor.
    while n > 1:         # While n still has remaining factors...
        if n % f == 0:   # The remainder of n divided by f might be zero.
            a.append(f)  # If so, it divides n. Add f to the list.
            n //= f      # Divide that factor out of n.
        else:            # But if f is not a factor of n,
            f += 1       # Add one to f and try again.
    return a             # Prime factors may be repeated: 12 factors to 2,2,3.


def prime_factors(n):
    factors = trial_division(n)

    for i in factors:
        if is_prime(i) is False:
            factors.remove(i)

    return factors


answer_list = trial_division(600851475143)

print(answer_list[len(answer_list)-1])
