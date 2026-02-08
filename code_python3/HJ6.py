import math



def f1(a):
    """计算a中元素的积"""
    sum = 1
    for i in a:
        sum *= i
    return sum


def find_prime(num):
    # 假设找6的质数
    res = []
    flag = False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            res.append(i)
            flag = True

    if not flag:
        # 当前num已经是质数
        return res

    # if f1(res) == num:
    #     return res

    return res + find_prime(num / res[-1])

n = int(input().strip())
print(find_prime(n))
