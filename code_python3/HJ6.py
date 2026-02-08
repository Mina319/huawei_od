import math

def find_prime(num):
    # 假设找6的质数
    res = []
    flag = False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            res.append(i)
            flag = True
            break

    if not flag:
        # 当前num已经是质数，将自己本身加进去
        res.append(num)
        return res

    return res + find_prime(num // res[-1])

n = int(input().strip())
for i in find_prime(n):
    print(i, end=' ')
