
def exponentiation_rapide(a, b):
    result = 1
    base = a
    while b > 0:
        if b % 2 == 1:  # Si l'exposant est impair
            result *= base
        base *= base
        b //= 2
    return result

def exponentiation_modulaire(a, b, n):
    result = 1
    base = a % n
    while b > 0:
        if b % 2 == 1:  # Si l'exposant est impair
            result = (result * base) % n
        base = (base * base) % n
        b //= 2
    return result
