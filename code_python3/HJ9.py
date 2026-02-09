num = int(input().strip())

res = ''

while num %10 != 0:
    a = num % 10
    num //= 10
    if str(a) not in res:
        res += str(a)
print(res)
