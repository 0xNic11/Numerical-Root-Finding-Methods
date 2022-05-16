def simpleFixedPoint(equation, error, max_iterations, x_value):
    x = sym.symbols("x")

    def equation_simplify(x): 
        simpliEquation = equation.strip()
        simpliEquation = simpliEquation.replace('x', '*x')
        
        if simpliEquation[0] == '*':
            simpliEquation = simpliEquation.replace('*', '')
        
        for i in range(len(simpliEquation)-1):
            if i == len(simpliEquation)-1:
                break
            
            if simpliEquation[i] == '+' and simpliEquation[i+1] =='*':
                simpliEquation = simpliEquation.replace('*', '')
            
        simpliEquation = simpliEquation.replace('^', '**')
        
        simpliEquation=sym.simplify(simpliEquation)
        return simpliEquation

    equation = equation_simplify(equation)

    def f(value):
        return round(float(equation.subs(x,value)),3)
    
    #print(f"Equation: {equation}, Error: {error}, Max Iterations: {max_iterations}, Initial Value: {x_value}")
    iteration_counter = 0
    
    solution = []
    index = 1
    
    if max_iterations == 0:
        return False
    
    iteration_counter +=1
    xi = x_value
    xiplus1 = f(xi)
    
    #print(f"Iteration: {iteration_counter} | xi = {xi}")    
    solution.append((index, xi, "---"))
    index += 1
    
    if max_iterations <= iteration_counter:
        return solution
    
    iteration_counter += 1
    eps = abs((xiplus1 - xi) / xiplus1) * 100
    xi = xiplus1
    xiplus1 = f(xi)
    
    #print(f"Iteration: {iteration_counter} | xi = {xi} | error = {eps}%")
    
    if max_iterations <= iteration_counter:
        return solution
    
    while(eps > error):
        iteration_counter += 1
        eps = abs((xiplus1 - xi) / xiplus1) * 100
        xi  = xiplus1
        xiplus1 = f(xi)
        #print(f"Iteration: {iteration_counter} | xi = {xi} | error = {eps}%")
        solution.append((iteration_counter, xi, str(round(eps, 3))+"%"))
        index += 1
        
        if (eps <= error):
            return solution
        
        if max_iterations <= iteration_counter:
            return solution
        
    #print(f"Root = {xi}")
