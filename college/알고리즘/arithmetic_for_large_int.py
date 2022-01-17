def ladd(u,v):
    n = len(u) if len(u) > len(v) else len(v)
    result = []
    carry = 0
    for k in range(n):
        i = u[k] if k <len(u) else 0 
        j = v[k] if k <len(v) else 0
        value = i+j+carry
        carry = value // 10
        result.append(value%10)
    if carry >0:
        result.append(carry) 
    return result[::-1] 
u = [3,2,1]
v = [5,4]
print(123+45)
print(ladd(u,v))

def prod (u,n):
    n = len(u) if len(u) > len(v) else len(v):
    if len(u) == 0 or len(v) == 0:
        return[0]
    elif n <threshold:
        return lmult(u,v)
    else:
        m = n//2
        x = div(u,m); y = rem(u,m)
