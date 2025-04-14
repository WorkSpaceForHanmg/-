total = 0
for i in range(1, 101):
    if i % 3 == 0:
        total += i
print(f"3의 배수의 합: {total}")