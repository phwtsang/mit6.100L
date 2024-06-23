"""
This is the program described at 29:02 of the lecture video
"""
def main():
    """
    This is the program described at 29:02 of the lecture video
    """
    print(count_nums_with_sqrt_close_to(10,0.1))

def count_nums_with_sqrt_close_to(n,epsilon):
    """
    n is an integer > 2
    epsilon is a positive number < 1
    returns how many integers have a square root within epsilon of n
    """
    for i in range(n):
        bisection_root(i,epsilon)

def bisection_root(x,epsilon):
    """
    x is a positive integer > 1
    epsilon is a positive number < 1
    returns an estimate for sqrt of x such that estimate**2
    is within epsilon of x
    """
    low = 0
    high = x
    ans = (high+low)/2.0
    ans_squared = ans**2
    while abs(ans_squared-x) >= epsilon:
        if ans_squared < x:
            low = ans
        else:
            high = ans
        ans = (high+low)/2.0

    return ans

main()
