def sumtoN(n):
    if n == 0:
        return 1
    return (n*sumtoN(n-1))


print(sumtoN(10))
