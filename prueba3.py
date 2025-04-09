def largo(num):
    if num == 0:
        return 0
    else:
        return 1+largo(num//10)

def invertir_num(num):
    if num == 0:
        return 0
    else:
        return (num%10) * (10**(largo(num)-1))+invertir_num(num//10)

print(invertir_num(124567))


