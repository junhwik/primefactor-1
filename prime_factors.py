class PrimeFactors:

    def of(self, num):
        factors = []
        divisor = 2
        if num > 1:

            if num == 4 or num == 6 or num == 9:
                while num > 1:
                    while num % divisor == 0:
                        factors.append(divisor)
                        num //= divisor
                    divisor += 1
            else:
                factors.append(num)
        return factors
