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

    c = (b + a)/2
    
    
    while error > error_acceptable:
        
        if f(a) * f(b) >= 0:
            print("No root in this range")
            quit()
        
        elif f(c) * f(a) < 0:    
            b = c
            c_old = c
            c = (b + a)/2
            error = abs(c - c_old)/c
            
        elif f(c) * f(b) < 0:
            a = c
            c_old = c
            c = (b + a)/2
            error = abs(c - c_old)/c
        
        else:
            print("something went wrong")
            quit()
    
    print(f"The error is {error*100}%")
    print(f"The lower bound a is {a} and the upper bound b is {b}")
    print(f"The root is {c}")
    
#Calling bisection method with the function and the bounds

#bisection_method("(-2 + (7*x) - (5*x ** 2)+ (6*x ** 3))", 0, 1, 0.1)