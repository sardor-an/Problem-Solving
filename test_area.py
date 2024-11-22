def fuck_hanif_pro(n, a):
    a = sorted(a)
    i = 0
    b = abs(a[i] - n)

    for k in range(len(a)):
        if abs(a[k] - n) <= b:
            i = k

    return a[i]



        
print(fuck_hanif_pro(125, [11,10, 5, 2, 1]))