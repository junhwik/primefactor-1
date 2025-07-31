from prime_factors import PrimeFactors


def test_prime_factors():
    prime_factor = PrimeFactors()
    assert 1==1

def test_prime_factors_of_1():
    prime_factor = PrimeFactors()
    assert prime_factor.of(1) == []
