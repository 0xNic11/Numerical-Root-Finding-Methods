def newtonMethod(equation, error, max_iterations, xo):
    global x
    x = sym.symbols("x")
    
    global pyEq
    global eq_diff
    
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
    
    pyEq = eqConverter(equation)
    eq_diff = pyEq.diff(x)

    def f(value):
        return round(float(pyEq.subs(x, value)), 3)

    
    def df(value):
        return round(float(eq_diff.subs(x, value)), 3)

    iteration_counter = 0
    
    if max_iterations == 0:
        return False
    
    print(f"Equation: {equation}, Error: {error}, Max Iterations: {max_iterations}, Initial Value: {xo}")
    
    solution = []
    index = 1
    
    # Iteration #1
    iteration_counter+=1
    xi = xo
#     display(Math('\\text{Iteration: }%g \\space | \\space x_i=%g \\quad \\quad \\space | \\space f({x_i})=%g \\space|\\space f\'({x_i})=%g | \\space \epsilon_a= -----' 
#                  %(iteration_counter, xi, f(xi), f_diff(xi))))
    print(f"Iteration: {iteration_counter} | xi = {xi} | f\'(xi) = {df(xi)}")
    
    solution.append((index, xi, f(xi), df(xi), "---"))
    index += 1
    
    if max_iterations <= iteration_counter:
#         display(Math('\nRoot = %s' %round(xi, 3)))
        print(f"Root = {xi}")
        return solution
    
    # Iteration #2
    iteration_counter+=1
    xiplus1 = xi - ( f(xi) / df(xi) )
    eps = abs((xiplus1 - xi) / xiplus1) * 100
#     display(Math('\\text{Iteration: }%g \\space | \\space x_i=%g \\quad \\quad \\space | \\space f({x_i})=%g \\space|\\space f\'({x_i})=%g | \\space \epsilon_a=%g \%%' 
#                  %(iteration_counter, xiplus1, f(xiplus1), f_diff(xiplus1), round(eps, 3))))

    print(f"Iteration: {iteration_counter} | xi = {xiplus1} | f\'(xi) = {df(xiplus1)} | error = {eps}%")
    
    solution.append((index, xiplus1, f(xiplus1), df(xiplus1), str(round(eps, 3))+"%"))
    index += 1
    
    if eps <= float(error):
#         display(Math('\nRoot = %s' %round(xi, 3)))
        print(f"Root = {xiplus1}")
        return solution
    
    if max_iterations <= iteration_counter:
#         display(Math('\nRoot = %s' %round(xi, 3)))
        print(f"Root = {xiplus1}")
        return solution

    while(eps > float(error)):  
        iteration_counter+=1
        xi = xiplus1
        xiplus1 = xi - ( f(xi) / df(xi) )
        eps = abs((xiplus1 - xi) / xiplus1) * 100
        
#         display(Math('\\text{Iteration: }%g \\space | \\space x_i=%g \\quad \\space | \\space f({x_i})=%g \\space|\\space f\'({x_i})=%g | \\space \epsilon_a=%g \%%' 
#                      %(iteration_counter, xiplus1, f(xiplus1), f_diff(xiplus1), round(eps, 3))))
        print(f"Iteration: {iteration_counter} | xi = {xiplus1} | f\'(xi) = {df(xiplus1)} | error = {eps}%")
        
        solution.append((index, xiplus1, f(xiplus1), df(xiplus1), str(round(eps, 3))+"%"))
        index += 1
        
        if eps <= float(error):
#             display(Math('\nRoot = %s' %round(xi, 3)))
            print(f"Root = {xiplus1}")
            return solution
        
        if max_iterations <= iteration_counter:
#             display(Math('\nRoot = %s' %round(xi, 3)))
            print(f"Root = {xiplus1}")
            return True    
