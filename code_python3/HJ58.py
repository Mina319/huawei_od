n, k = [int(i) for i in input().strip().split(" ")]
a = [int(i) for i in input().strip().split(" ")]
a.sort()
print(' '.join(map(str, a[:k])))
