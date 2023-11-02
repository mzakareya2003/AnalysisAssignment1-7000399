def naive(a, n):
    result = 1
    for _ in range(n):
        result *= a
    print(result)

naive(2,6)
