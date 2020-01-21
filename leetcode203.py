import math
class Solution:
    #solution1
    """ def countPrimes(self, n: int) -> int:
        count = 0
        for i in range(2,n):
            if self.isPrime(i):
                count += 1
        return count
    def isPrime(self,num):
        if num<3:
            return True
        i = 2
        while i*i<=num:
            if num%i == 0:
                return False
            i+=1
        return True """

    #solution2
    def countPrimes(self, n: int) -> int:
        isPrime = [True]*n
        isPrime[0],isPrime[1] = False,False
        for i in range(2,int(math.sqrt(n))+1):
            isPrime[i**2:n:i] = [False]*len(isPrime[i**2:n:i])
        return sum(isPrime)
    

x = Solution()
res = x.countPrimes(10)
print(res)
