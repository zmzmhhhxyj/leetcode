def rangeBitwiseAnd(m, n):
    i = 0
    while m != n:
        m >>= 1 #delete last bit 11010-->1101-->110-->11
        n >>= 1 #11111-->1111-->111-->11
        # move three times, so add three zeros to n
        i += 1
    return n << i

ans = rangeBitwiseAnd(26,31)
print(ans)