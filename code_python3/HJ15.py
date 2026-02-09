s = input().strip()
s1 = bin(int(s))
sum = 0
for i in s1[2:]:
    if i == '1':
        sum += 1
print(sum)
