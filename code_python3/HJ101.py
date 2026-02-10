n = input().strip()
a = [int(i) for i in input().strip().split(" ")]
op = int(input().strip())
if op == 1:
    # 降序
    a.sort(reverse=True)
else:
    a.sort()
print(' '.join(map(str, a)))
