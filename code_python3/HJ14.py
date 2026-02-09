n = int(input())
res = []
for i in range(n):
    ss = input().strip()
    res.append(ss)

res.sort()
print('\n'.join(res))
