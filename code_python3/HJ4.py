str = input().strip()
n = len(str)
x = n // 8 if n % 8 == 0 else n // 8+1
for i in range(x):
    # 左对齐格式化填充0
    print(f'{str[i*8:(i+1)*8]: 0<8}')
