def bisection_method(func, a, b, error_acceptable):
    """
    This function uses the bisection method to find the root of a function.

    Args:
        func (param): The function to find the root of.
        a (param): The lower bound of the search.
        b (param): The upper bound of the search.
        error_acceptable (param): The error acceptable.
    """
    def f(x):
        f = eval(func)
        return f
    
    error = abs(b - a)
    
    while error < error_acceptable:
        c = (b + a) / 2
        
        if f(a) * f(b) >= 0:
            print("No root in this range")
            quit()
        
        elif f(c) * f(a) < 0:    
            b = c
            error = abs(b - a)
            
        elif f(c) * f(b) < 0:
            a = c
            error = abs(b - a)
        
        else:
            print("something went wrong")
            quit()
    
    print(f"the error is {error}")
    print(f"The root is {c}")
    

print(bisection_method("-2 + 7x - 5x**2 + 6x**3", 0, 1, 0.1))