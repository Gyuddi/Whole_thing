def bin2dec(b):
    dec = 0
    b = list(map(int, str(b)))
    for idx , i in enumerate(b[::-1]):
        if i == 1:
            dec += 2 ** idx
    return dec

