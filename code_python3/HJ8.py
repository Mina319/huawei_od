n = int(input().strip())

res = {}
for i in range(n):
    i, v = [int(a) for a in input().strip().split(' ')]
    if i in res:
        res[i] += v
    else:
        res[i] = v

# 按键排序
res1 = dict(sorted(res.items(), key=lambda x: x[0]))
for k, v in res1.items():
    print(f'{k} {v}')

