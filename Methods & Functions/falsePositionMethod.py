def falsePosition(equation, error, max_iterations, xL, xU):
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
    
    
    solution = []
    index = 1
    
    iteration_counter = 0
    
    if max_iterations == 0:
        return False
    
    xR = xU - ((f(xU) * (xL - xU)) / (f(xL) - f(xU)) )
    
    iteration_counter += 1
    #print(f"Iteration: {iteration_counter} | xL = {xL} | f(xL) = {f(xL)} | xU = {xU} | f(xU) = {f(xU)} | xR = {xR} | f(xR) = {f(xR)}")  
    
    solution.append((index, xL, f(xL), xU, f(xU), xR, f(xR), "---"))
    index += 1
    
    if (f(xL) * f(xR)) < 0.0:
        xU = xR
    else:
        xL = xR
        
    if max_iterations <= iteration_counter:
        #print(f"Root = {xR}")
        return solution
    
    while(True):
        iteration_counter += 1
        xR_old = xR
        xR = xU - ((f(xU) * (xL - xU)) / (f(xL) - f(xU)) )
        eps = abs((xR - xR_old) / xR) * 100
        #print(f"Iteration: {iteration_counter} | xL = {xL} | f(xL) = {f(xL)} | xU = {xU} | f(xU) = {f(xU)} | xR = {xR} | f(xR) = {f(xR)} | error = {eps}")
        
        solution.append((iteration_counter, xL, f(xL), xU, f(xU), xR, f(xR), str(round(eps, 3))+"%"))
        index += 1        
        if (eps <= error):
            #print(f"Root = {xR}")
            return solution;

        if (f(xL) * f(xR)) < 0:
            xU = xR
        else:
            xL = xR

        if max_iterations <= iteration_counter:
            #display(Math('\nRoot = %s'%xR))
            return solution
