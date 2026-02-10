a,b = [int(i) for i in input().strip().split(" ")]
max1 = max(a,b)
min1 = min(a,b)
res = []
if max1+abs(a-b) > 0:
    res.append(max1+abs(a-b))
if min1-abs(a-b) > 0:
    res.append(min1-abs(a-b))
print(res[0])
