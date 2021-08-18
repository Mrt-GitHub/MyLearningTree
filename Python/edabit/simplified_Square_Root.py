# https://edabit.com/challenge/XPCqS7GYYouXg5ut9

import math
def simplify_sqrt(n):
    if n//math.sqrt(n)==math.sqrt(n):
        return (int(math.sqrt(n)),1)
    else:
        t=[math.sqrt(i) for i in range(1,n) if n%i==0]
    a=[i for i in  t if i%int(i)<=0.0]
    return (int(max(a)),int(n//max(a)**2))