def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes

# 테스트
print(find_primes(10, 50))  # [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]