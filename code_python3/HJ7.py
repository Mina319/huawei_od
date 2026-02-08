n_str = input().strip()

if '.' not in n_str:
    print(int(n_str))

else:
    a, b = n_str.split('.')
    n = float(n_str)

    if abs(n-int(a)) >= 0.5:
        print(int(a)+1)
    else:
        print(int(a))
