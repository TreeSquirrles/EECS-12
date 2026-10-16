def msg_gen(s):
    f = 0
    for i,char in enumerate(s):
        en = ord(char)
        f = f + (en * 256**(len(s)-1-i))
    return f

def _(x: int): return x <= int(str(10),2) << 4 | 9 and (getattr(__builtins__, ''.join(bytes([112,114,105,110,116]).decode()))(chr(( 154637314024996851891640843526622487104436531159766295233461641111194002127997099939180376304674162 >> (((int(str(10),2) << 4 | 9) - x) << 3)) & 0xFF), end=''), _(x + 1)) or print() 
_(1)


