from prime_factors import PrimeFactors


def test_prime_factors():
    prime_factor = PrimeFactors()
    assert 1==1

def test_prime_factors_of_1():
    prime_factor = PrimeFactors()
    assert prime_factor.of(1) == []

def test_prime_factors_of_2():
    prime_factor = PrimeFactors()
    assert prime_factor.of(2) == [2]

def test_prime_factors_of_3():
    prime_factor = PrimeFactors()
    assert prime_factor.of(3) == [3]

def test_prime_factors_of_4():
    prime_factor = PrimeFactors()
    assert prime_factor.of(4) == [2, 2]

def test_prime_factors_of_6():
    prime_factor = PrimeFactors()
    assert prime_factor.of(6) == [2, 3]