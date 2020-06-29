import math

def discr(a=0, b=0, c=0):

    res = b ** 2 - 4 * a * c
    return float(res)

def solve_eq(a, b, c):
    
    x1, x2 = None, None
    
    d = discr(a,b,c)
    print('D = ',float(d))

    
    if d > 0:    
        d = float(math.sqrt(d))
        x1 = float((-b + d) / (2 * a))
        x2 = float((-b - d) / (2 * a))
        return (x1, x2)

    elif d == 0:
         return ((-b) / (2 * a))
    elif d < 0:
        return x1, x2
        


# 1 test case = тестовый случай 
discr(1)  # 0

# 2 
discr(1, c=1/4) # -1.0 

# 3
discr(1,b=2,c=1/4) # 3.0 

# 4
discr(1,b=2,c=3) # -8.0

# 5
discr()  # 0.0

# 5
discr()  # 0.0

# 6
discr()



if __name__ == '__main__':
    assert solve_eq(1,2,3) == (None, None)
    assert solve_eq(1,-6,9) == (3)
    assert solve_eq(1,-8,12) == (6,2)
