def largo(num):
    if num == 0:
        return 0
    else:
        return 1+largo(num//10)

def tralalero(num):
    if num == 0:
        return 0
    else:
        return (num%10) * (10**(largo(num)-1))+tralalero(num//10)

print(tralalero(124567))


