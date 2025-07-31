class PrimeFactors:

    def of(self, num):
        factors=[]
        divisor = 2
        if num>1:

            if num==4:
                while num %2==0:
                    factors.append(2)
                    num//=2
            elif num == 6:
                while num>1:
                    while num%divisor==0:
                        factors.append(divisor)
                        num//=divisor
                    divisor+=1

            else:
                factors.append(num)
        return factors
