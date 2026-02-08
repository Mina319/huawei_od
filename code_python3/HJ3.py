n = int(input().strip())

num = []
for i in range(n):
    a = int(input().strip())
    num.append(a)

num.sort()
for i, v in enumerate(num):
    if num[i] == num[i - 1]:
        continue
    print(v)
