num = 51
f = 2

if num != 1 and num != 0:
    while f < num:
        if num % f == 0:
            print("not prime")
            break
        else:
            f += 1
        if f == num:
            print("prime")
elif num == 2:
    print("prime")
else:
    print("not prime")
