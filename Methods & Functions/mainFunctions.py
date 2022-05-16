from IPython.display import display, Math
import sympy as sym
import bisectionMethod as bm
import falsePositionMethod as fpm
import simpleFixedPointMethod as sfp
import newtonMethod as nm
import secantMethod as sm



def mainFunctions():
    
    global x
    x = sym.symbols('x')
    
    global pyEq
    global eq_diff
    global okeyDokeyEq
    
    okeyDokeyEq = input("Enter the equation: ")
    if okeyDokeyEq[0:5] == 'sqrt(' and okeyDokeyEq[-1] == ')':
        display(Math('Equation: \\%s'%okeyDokeyEq))
    else:
        display(Math('Equation: %s'%okeyDokeyEq))
        
        
    pyEq = eqConverter(okeyDokeyEq)
    eq_diff = pyEq.diff(x)
    
    global error 
    error = float(input("Enter the error: "))
    
    
    global max_iterations
    max_iterations = float(input("Enter the maximum number of iterations: "))
        
    choice = str(input("""Choose the Method using the labeled letters:\n#a Bisection\n#b False Position\n#c Simple Fixed Point\n#d Newton's Method\n#e Secant\n"""))
    
    if choice == 'a':
        xL = float(input("Enter xL: "))
        xU = float(input("Enter xU: "))
        if eqChecker(xL, xU):
            bm.bisection(xL, xU)
        else:
            print("Function has no solution in the given range")
    elif choice == 'b':
        xL = float(input("Enter xL: "))
        xU = float(input("Enter xU: "))
        if eqChecker(xL, xU):
            fpm.false_position(xL, xU)
        else:
            print("Function has no solution in the given range")
    elif choice == 'c':
        x_value = float(input("Enter x_value: "))
        sfp.simple_fixed_point(x_value)
    elif choice == 'd':
        x0 = float(input("Enter x0: "))
        nm.newton(x0)
    elif choice == 'e':
        xi_minus1 = float(input("Enter xi_minus1: "))
        xi = float(input("Enter xi: "))
        sm.secant(xi_minus1, xi)
    else:
        print("Invalid choice")
        
def eqConverter(equation):
    global x
    simpleEquation = equation.strip()
    simpleEquation = simpleEquation.replace('x', '*x')
    
    if simpleEquation[0] == '*':
        simpleEquation = simpleEquation.replace('*', '')
    
    eqList = []
    eqList[:0] = simpleEquation
    
    if ' ' in eqList:
        eqList.remove(' ')
    
    for i in range(len(eqList)):
        
        if(eqList[i] == '+' or eqList[i] == '-') and eqList[i+1] == '*':
            eqList[i+1] = ''
            
    simpleEquation = ''.join(eqList)
    simpleEquation = simpleEquation.replace('^', '**')
    return sym.sympify(simpleEquation)

def f(value):
    tempEq = pyEq
    return round(float(tempEq.subs(x, value)), 3)

def f_diff(value):
    tempEqDiff = eq_diff
    return round(float(tempEqDiff.subs(x, value)), 3)

def eqChecker(xL, xU):
    """Check the validity of the given fucntion if it has a solution or not
    Args:
        xL (value): lower bound
        xU (value): upper bound
    Returns:
        true: function has a solution in the given range
        false: function has no solution in the given range
    """
    if f(xL) * f(xU) < 0:
        return True
    else:   
        return False
    

