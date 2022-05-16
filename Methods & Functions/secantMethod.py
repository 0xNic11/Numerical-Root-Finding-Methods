def secantMethod(equation, error, max_iterations, xi_minus1, xi):
        
    global x
    x = sym.symbols('x')
    
    def equation_simplify(equation):
        global x
        simplifiedEquation = equation.strip()
        simplifiedEquation = simplifiedEquation.replace('x', '*x')
        
        if simplifiedEquation[0] == '*':
            simplifiedEquation = simplifiedEquation.replace('*', '')
            
        equation_list = []
        equation_list[:0] = simplifiedEquation # Seprate each character into an item in a list
        
        # Remove extra spaces in the equation if exists
        if ' ' in equation_list:
            equation_list.remove(' ')
        
        for i in range(len(equation_list)):

            if (equation_list[i] == '+' or equation_list[i] == '-') and equation_list[i+1] == '*':
                equation_list[i+1] = ''
                
        simplifiedEquation = ''.join(equation_list) # Concatenate all list items to equation
        simplifiedEquation = simplifiedEquation.replace('^', '**')
        return sym.sympify(simplifiedEquation)

    equation=equation_simplify(equation)

    def f(value):
        return round(float(equation.subs(x,value)),3)
    
    solution =[]
    index = 1
    
    iteration_counter = 0
    
    if max_iterations == 0:
        return False
    
        solution.append((index, xi_minus1, f(xi_minus1), xi, f(xi)))
        index += 1
    
    while(True):
        xi_old = xi
        xi = xi - ( (f(xi) * (xi_minus1 - xi)) / (f(xi_minus1) - f(xi)) )
        xi_minus1 = xi_old
        
        eps = abs((xi - xi_minus1) / xi) * 100
        
        solution.append((index, xi_minus1, f(xi_minus1), xi, f(xi), str(round(eps, 3))+"%"))
        index += 1
        #display(Math('Iteration: %g \\space | \\space x_{i-1}=%g \\quad \\quad \\space | \\space f(x_{i-1})=%g \\space | \\space xi =%g \\space | \\space f(xi)=%g \\space | \\space error = %g ' % (iteration_counter, round(xi_minus1, 3), f(xi_minus1), round(xi, 3), f(xi), round(eps, 3))))
        
        iteration_counter+=1
        
        if (eps <= error):
            #display(Math('\Root = %s' %round(xi, 3)))
            return solution
        
        if max_iterations <= iteration_counter:
            #display(Math('\Root = %s' %round(xi, 3)))
            return solution
