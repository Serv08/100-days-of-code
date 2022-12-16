print("\nx= 2root of 2 raise to 3root of 3 raised to 4root or 4 ...")

val = 2
maxim = 100
def eval(max, maxim):
    y = max ** (1/max)
    if max == maxim:
        return y**(maxim ** (1/maxim))
    else:
        return y**(eval(max+1, maxim))

print("x = 2root of 2 raise to 3root of 3 raised to 4root or 4 ... converges at",eval(val,maxim),("(using recursion)\n"))