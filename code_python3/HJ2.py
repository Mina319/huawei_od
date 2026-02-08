result = 0
str1 = input().strip()
key = input().strip()
for s in str1:
    if s.lower() == key.lower():
        result += 1
print(result)

