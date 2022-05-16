import sympy as sym
import tkinter as tk
from tkinter import *
from tkinter import ttk

global x 

def bisection(equation, error, max_iterations, xL, xU):
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
    
    iteration_counter = 0
    
    if max_iterations == 0:
        return False
    
    
    solution = []
    index = 1
    
    xR = (xL + xU) / 2
    
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
        xR = (xL + xU) / 2
        eps = abs((xR - xR_old) / xR) * 100
        #print(f"Iteration: {iteration_counter} | xL = {xL} | f(xL) = {f(xL)} | xU = {xU} | f(xU) = {f(xU)} | xR = {xR} | f(xR) = {f(xR)} | error = {eps}")
        
        solution.append((iteration_counter, xL, f(xL), xU, f(xU), xR, f(xR), str(round(eps, 3))+"%"))
        index += 1
    
        if (eps <= error):
            #print(f"Root = {xR}")
            return solution

        if (f(xL) * f(xR)) < 0:
            xU = xR
        else:
            xL = xR

        if max_iterations <= iteration_counter:
            #print(f"Root = {xR}")
            return solution
        

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


class welcomeScreen:
    def __init__(self, window=None):
        self.master = window
        window.geometry("1280x720+383+106")
        window.minsize(120, 1)
        window.maxsize(1370, 749)
        window.resizable(0, 0)
        window.title("Numerical Calculator")
        p1 = PhotoImage(file='./num.png')
        window.iconphoto(True, p1)
        window.configure(background="#3BACB6")
        window.configure(cursor="arrow")
        

        
        
        self.Labelframe1 = tk.LabelFrame(window, relief='groove', font="-family {Segoe UI} -size 13 -weight bold",
                                         foreground="#001c37", text="Select a Method", background="#fffffe")
        self.Labelframe1.place(relx=0.081, rely=0.081, relheight=0.415, relwidth=0.848)

        self.Button1 = tk.Button(self.Labelframe1, activebackground="#ececec", activeforeground="#000000",
                                 background="#00254a", borderwidth="0", disabledforeground="#a3a3a3",
                                 font="-family {Segoe UI} -size 11", foreground="#fffffe",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                 text="Bisection Method", command=self.bisection)
        self.Button1.place(relx=0.667, rely=0.195, height=34, width=181, bordermode='ignore')

        self.Button2 = tk.Button(self.Labelframe1, activebackground="#ececec", activeforeground="#000000",
                                 background="#00254a", borderwidth="0", disabledforeground="#a3a3a3",
                                 font="-family {Segoe UI} -size 11", foreground="#fffffe",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                 text="False Position Method", command=self.falsePosition)
        self.Button2.place(relx=0.04, rely=0.195, height=34, width=181, bordermode='ignore')

        self.Button3 = tk.Button(self.Labelframe1, activebackground="#ececec", activeforeground="#000000",
                                 background="#00254a", borderwidth="0", disabledforeground="#a3a3a3",
                                 font="-family {Segoe UI} -size 11", foreground="#fffffe",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text="Simple Fixed Point Method",
                                 command=self.simpleFixedPoint)
        self.Button3.place(relx=0.667, rely=0.683, height=34, width=181, bordermode='ignore')

        self.Button4 = tk.Button(self.Labelframe1, activebackground="#ececec", activeforeground="#000000",
                                 background="#00254a", borderwidth="0", disabledforeground="#a3a3a3",
                                 font="-family {Segoe UI} -size 11", foreground="#fffffe",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                 text="Newton Method", command=self.newton)
        self.Button4.place(relx=0.04, rely=0.439, height=34, width=181, bordermode='ignore')

        self.Button5 = tk.Button(self.Labelframe1, activebackground="#ececec", activeforeground="#000000",
                                 background="#00254a", borderwidth="0", disabledforeground="#a3a3a3",
                                 font="-family {Segoe UI} -size 11", foreground="#fffffe",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                 text="Secant Method", command=self.secant)
        self.Button5.place(relx=0.667, rely=0.439, height=34, width=181, bordermode='ignore')
        
        self.Button3 = tk.Button(self.Labelframe1, activebackground="#ececec", activeforeground="#000000",
                                 background="#00254a", borderwidth="0", disabledforeground="#a3a3a3",
                                 font="-family {Segoe UI} -size 11", foreground="#fffffe",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text="Exit",
                                 command=self.exit)
        self.Button3.place(x=45, y=200, height=34, width=181, bordermode='ignore')
        


    def bisection(self):
        Bisection(Toplevel(self.master))

    def falsePosition(self):
        FalsePosition(Toplevel(self.master))
            
    def simpleFixedPoint(self):
        SimpleFixedPoint(Toplevel(self.master))
            
    def newton(self):
        Newton(Toplevel(self.master))
            
    def secant(self):    
        Secant(Toplevel(self.master))
        
    def exit(self):
        self.master.withdraw()
            
            
            
            
class Bisection:
    def __init__(self, window=None):
        self.master = window
        window.geometry("1280x720+512+237")
        window.minsize(120, 1)
        window.maxsize(1370, 749)
        window.resizable(0, 0)
        window.title("Bisection Method")
        window.configure(background="#f2f3f4")
        
        
        self.Label1 = tk.Label(window, activebackground="#f9f9f9", activeforeground="black", background="#f2f3f4",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='''Equation:''', font="-family {Segoe UI} -size 12 -weight bold")
        self.Label1.place(height=31, width=100, x=100, y=100)
        
        self.Entry1 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", insertbackground="black", selectbackground="blue",
                               selectforeground="white")
        self.Entry1.place(height=30, width=300, x=200, y=100)
        
        
        self.Label2 = tk.Label(window, activebackground="#f9f9f9", activeforeground="black", background="#f2f3f4",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='''Error:''', font="-family {Segoe UI} -size 12 -weight bold")
        self.Label2.place(height=31, width=100, x=115, y=150)
        
        self.Entry2 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", insertbackground="black", selectbackground="blue",
                               selectforeground="white")
        self.Entry2.place(height=30, width=100, x=200, y=150)

        
        self.Label3 = tk.Label(window, activebackground="#f9f9f9", activeforeground="black", background="#f2f3f4",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='''Max Iterations:''', font="-family {Segoe UI} -size 12 -weight bold")
        self.Label3.place(height=31, width=200, x=30, y=200)
        
        self.Entry3 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", insertbackground="black", selectbackground="blue",
                               selectforeground="white")
        self.Entry3.place(height=30, width=100, x=200, y=200)

        
        self.Label4 = tk.Label(window, activebackground="#f9f9f9", activeforeground="black", background="#f2f3f4",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='''xL:''', font="-family {Segoe UI} -size 12 -weight bold")
        self.Label4.place(height=31, width=100, x=125, y=250)
        
        self.Entry4 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", insertbackground="black", selectbackground="blue",
                               selectforeground="white")
        self.Entry4.place(height=30, width=100, x=200, y=250)

        
        self.Label5 = tk.Label(window, activebackground="#f9f9f9", activeforeground="black", background="#f2f3f4",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='''xU:''', font="-family {Segoe UI} -size 12 -weight bold")
        self.Label5.place(height=31, width=100, x=125, y=300)
        
        self.Entry5 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", insertbackground="black", selectbackground="blue",
                               selectforeground="white")
        self.Entry5.place(height=30, width=100, x=200, y=300)
        
        
        self.Button1 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                 borderwidth="0", disabledforeground="#a3a3a3", foreground="#ffffff",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text="Solve",
                                 command=lambda: self.bisection(self.Entry1.get(), self.Entry2.get(), self.Entry3.get(), self.Entry4.get(), self.Entry5.get()))
        self.Button1.place(height=30, width=100, x=700, y=300)
        
        self.Button2 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                 borderwidth="0", disabledforeground="#a3a3a3", foreground="#ffffff",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text="Back",
                                 command=self.back)
        self.Button2.place(height=30, width=100, x=850, y=300)
        
        
        global Frame1_1_2
        Frame1_1_2 = tk.Frame(window, relief='groove', borderwidth="2", background="#fffffe")
        Frame1_1_2.place(height=350, width=1000, x=150, y=350)
        
    
    def back(self):
        self.master.withdraw()
        
    def bisection(self, equation, error, max_iterations, xL, xU):
        fltError = float(error)
        intMax_iterations = int(max_iterations)
        fltxL = float(xL)
        fltxU = float(xU)
        result = bisection(equation, fltError, intMax_iterations, fltxL, fltxU)
        
        print("Bisection Function Called")
        
        bisection_table = ttk.Treeview(Frame1_1_2)
        

        bisection_table['columns'] = ('i', 'xL', 'f(xL)', 'xU', 'f(xU)', 'xR', 'f(xR)', 'eps')

        bisection_table.column("#0", width=0, stretch=NO)
        bisection_table.column("i", anchor=CENTER, width=125)
        bisection_table.column("xL", anchor=CENTER, width=125)
        bisection_table.column("f(xL)", anchor=CENTER, width=125)
        bisection_table.column("xU", anchor=CENTER, width=125)
        bisection_table.column("f(xU)", anchor=CENTER, width=125)
        bisection_table.column("xR", anchor=CENTER, width=125)
        bisection_table.column("f(xR)", anchor=CENTER, width=125)
        bisection_table.column("eps", anchor=CENTER, width=125)

        bisection_table.heading("#0", text="", anchor=CENTER)
        bisection_table.heading("i", text="Id", anchor=CENTER)
        bisection_table.heading("xL", text="xL", anchor=CENTER)
        bisection_table.heading("f(xL)", text="f(xL)", anchor=CENTER)
        bisection_table.heading("xU", text="xU", anchor=CENTER)
        bisection_table.heading("f(xU)", text="f(xU)", anchor=CENTER)
        bisection_table.heading("xR", text="xR", anchor=CENTER)
        bisection_table.heading("f(xR)", text="f(xR)", anchor=CENTER)
        bisection_table.heading("eps", text="eps", anchor=CENTER)

        for index, item in enumerate(result):
            bisection_table.insert(parent='',index='end', iid=index,text='', values=item)

        bisection_table.pack()

class FalsePosition:
    def __init__(self, window=None):
        self.master = window
        window.geometry("1280x720+512+237")
        window.minsize(120, 1)
        window.maxsize(1370, 749)
        window.resizable(0, 0)
        window.title("False Position Method")
        window.configure(background="#f2f3f4")
        
        self.Label1 = tk.Label(window, activebackground="#f9f9f9", activeforeground="black", background="#f2f3f4",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='''Equation:''', font="-family {Segoe UI} -size 12 -weight bold")
        self.Label1.place(height=31, width=100, x=100, y=100)
        
        self.Entry1 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", insertbackground="black", selectbackground="blue",
                               selectforeground="white")
        self.Entry1.place(height=30, width=300, x=200, y=100)
        
        
        self.Label2 = tk.Label(window, activebackground="#f9f9f9", activeforeground="black", background="#f2f3f4",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='''Error:''', font="-family {Segoe UI} -size 12 -weight bold")
        self.Label2.place(height=31, width=100, x=115, y=150)
        
        self.Entry2 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", insertbackground="black", selectbackground="blue",
                               selectforeground="white")
        self.Entry2.place(height=30, width=100, x=200, y=150)

        
        self.Label3 = tk.Label(window, activebackground="#f9f9f9", activeforeground="black", background="#f2f3f4",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='''Max Iterations:''', font="-family {Segoe UI} -size 12 -weight bold")
        self.Label3.place(height=31, width=200, x=30, y=200)
        
        self.Entry3 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", insertbackground="black", selectbackground="blue",
                               selectforeground="white")
        self.Entry3.place(height=30, width=100, x=200, y=200)

        
        self.Label4 = tk.Label(window, activebackground="#f9f9f9", activeforeground="black", background="#f2f3f4",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='''xL:''', font="-family {Segoe UI} -size 12 -weight bold")
        self.Label4.place(height=31, width=100, x=125, y=250)
        
        self.Entry4 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", insertbackground="black", selectbackground="blue",
                               selectforeground="white")
        self.Entry4.place(height=30, width=100, x=200, y=250)

        
        self.Label5 = tk.Label(window, activebackground="#f9f9f9", activeforeground="black", background="#f2f3f4",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='''xU:''', font="-family {Segoe UI} -size 12 -weight bold")
        self.Label5.place(height=31, width=100, x=125, y=300)
        
        self.Entry5 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", insertbackground="black", selectbackground="blue",
                               selectforeground="white")
        self.Entry5.place(height=30, width=100, x=200, y=300)
        
        
        self.Button1 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                 borderwidth="0", disabledforeground="#a3a3a3", foreground="#ffffff",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text="Solve",
                                 command=lambda: self.falsePosition(self.Entry1.get(), self.Entry2.get(), self.Entry3.get(), self.Entry4.get(), self.Entry5.get()))
        self.Button1.place(height=30, width=100, x=700, y=300)
        
        self.Button2 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                 borderwidth="0", disabledforeground="#a3a3a3", foreground="#ffffff",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text="Back",
                                 command=self.back)
        self.Button2.place(height=30, width=100, x=850, y=300)
        
        
        global Frame1_1_2
        Frame1_1_2 = tk.Frame(window, relief='groove', borderwidth="2", background="#fffffe")
        Frame1_1_2.place(height=200, width=1000, x=150, y=350)
        
    
    def back(self):
        self.master.withdraw()
        
    def falsePosition(self, equation, error, max_iterations, xL, xU):
        fltError = float(error)
        intMax_iterations = int(max_iterations)
        fltxL = float(xL)
        fltxU = float(xU)
        result = falsePosition(equation, fltError, intMax_iterations, fltxL, fltxU)
        print("False Position Function Called")
        
        falsePosition_table = ttk.Treeview(Frame1_1_2)
        
        falsePosition_table['columns'] = ('i', 'xL', 'f(xL)', 'xU', 'f(xU)', 'xR', 'f(xR)', 'eps')
        
        falsePosition_table.column("#0", width=0, stretch=NO)
        falsePosition_table.column("i", anchor=CENTER, width=125)
        falsePosition_table.column("xL", anchor=CENTER, width=125)
        falsePosition_table.column("f(xL)", anchor=CENTER, width=125)
        falsePosition_table.column("xU", anchor=CENTER, width=125)
        falsePosition_table.column("f(xU)", anchor=CENTER, width=125)
        falsePosition_table.column("xR", anchor=CENTER, width=125)
        falsePosition_table.column("f(xR)", anchor=CENTER, width=125)
        falsePosition_table.column("eps", anchor=CENTER, width=125)
        
        falsePosition_table.heading("#0", text="", anchor=CENTER)
        falsePosition_table.heading("i", text="Id", anchor=CENTER)
        falsePosition_table.heading("xL", text="xL", anchor=CENTER)
        falsePosition_table.heading("f(xL)", text="f(xL)", anchor=CENTER)
        falsePosition_table.heading("xU", text="xU", anchor=CENTER)
        falsePosition_table.heading("f(xU)", text="f(xU)", anchor=CENTER)
        falsePosition_table.heading("xR", text="xR", anchor=CENTER)
        falsePosition_table.heading("f(xR)", text="f(xR)", anchor=CENTER)
        falsePosition_table.heading("eps", text="eps", anchor=CENTER)

        for index, item in enumerate(result):
            falsePosition_table.insert(parent='',index='end', iid=index,text='', values=item)

        falsePosition_table.pack()


class SimpleFixedPoint:
    def __init__(self, window=None):
        self.master = window
        window.geometry("1280x720+512+237")
        window.minsize(120, 1)
        window.maxsize(1370, 749)
        window.resizable(0, 0)
        window.title("Simple Fixed Point Method")
        window.configure(background="#f2f3f4")
        
        self.Label1 = tk.Label(window, activebackground="#f9f9f9", activeforeground="black", background="#f2f3f4",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='''Equation:''', font="-family {Segoe UI} -size 12 -weight bold")
        self.Label1.place(height=31, width=100, x=100, y=100)
        
        self.Entry1 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", insertbackground="black", selectbackground="blue",
                               selectforeground="white")
        self.Entry1.place(height=30, width=300, x=200, y=100)
        
        
        self.Label2 = tk.Label(window, activebackground="#f9f9f9", activeforeground="black", background="#f2f3f4",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='''Error:''', font="-family {Segoe UI} -size 12 -weight bold")
        self.Label2.place(height=31, width=100, x=115, y=150)
        
        self.Entry2 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", insertbackground="black", selectbackground="blue",
                               selectforeground="white")
        self.Entry2.place(height=30, width=100, x=200, y=150)

        
        self.Label3 = tk.Label(window, activebackground="#f9f9f9", activeforeground="black", background="#f2f3f4",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='''Max Iterations:''', font="-family {Segoe UI} -size 12 -weight bold")
        self.Label3.place(height=31, width=200, x=30, y=200)
        
        self.Entry3 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", insertbackground="black", selectbackground="blue",
                               selectforeground="white")
        self.Entry3.place(height=30, width=100, x=200, y=200)

        
        self.Label4 = tk.Label(window, activebackground="#f9f9f9", activeforeground="black", background="#f2f3f4",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='''x0:''', font="-family {Segoe UI} -size 12 -weight bold")
        self.Label4.place(height=31, width=100, x=125, y=250)
        
        self.Entry4 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", insertbackground="black", selectbackground="blue",
                               selectforeground="white")
        self.Entry4.place(height=30, width=100, x=200, y=250)

        
        self.Button1 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                 borderwidth="0", disabledforeground="#a3a3a3", foreground="#ffffff",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text="Solve",
                                 command=lambda: self.simpleFixedPoint(self.Entry1.get(), self.Entry2.get(), self.Entry3.get(), self.Entry4.get()))
        self.Button1.place(height=30, width=100, x=700, y=300)
        
        self.Button2 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                 borderwidth="0", disabledforeground="#a3a3a3", foreground="#ffffff",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text="Back",
                                 command=self.back)
        self.Button2.place(height=30, width=100, x=850, y=300)
        
        
        global Frame1_1_2
        Frame1_1_2 = tk.Frame(window, relief='groove', borderwidth="2", background="#fffffe")
        Frame1_1_2.place(height=350, width=1000, x=150, y=350)
        
    
    def back(self):
        self.master.withdraw()
        
    def simpleFixedPoint(self, equation, error, max_iterations, x_value):
        fltError = float(error)
        intMax_iterations = int(max_iterations)
        fltx_value = float(x_value)
        result = simpleFixedPoint(equation, fltError, intMax_iterations, fltx_value)
        print("Simple Fixed Point Function Called")
        
        simpleFixedPoint_table = ttk.Treeview(Frame1_1_2)
        simpleFixedPoint_table['columns'] = ('i', 'xi', 'eps')
        simpleFixedPoint_table.column("#0", width=0, stretch=NO)
        simpleFixedPoint_table.column("i", anchor=CENTER, width=330)
        simpleFixedPoint_table.column("xi", anchor=CENTER, width=330)
        simpleFixedPoint_table.column("eps", anchor=CENTER, width=330)
        simpleFixedPoint_table.heading("#0", text="", anchor=CENTER)
        simpleFixedPoint_table.heading("i", text="Id", anchor=CENTER)
        simpleFixedPoint_table.heading("xi", text="xL", anchor=CENTER)
        simpleFixedPoint_table.heading("eps", text="eps", anchor=CENTER)

        for index, item in enumerate(result):
            simpleFixedPoint_table.insert(parent='',index='end', iid=index,text='', values=item)

        simpleFixedPoint_table.pack()


class Newton:
    def __init__(self, window=None):
        self.master = window
        window.geometry("1280x720+512+237")
        window.minsize(120, 1)
        window.maxsize(1370, 749)
        window.resizable(0, 0)
        window.title("Newton Method")
        window.configure(background="#f2f3f4")

        self.Label1 = tk.Label(window, activebackground="#f9f9f9", activeforeground="black", background="#f2f3f4",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='''Equation:''', font="-family {Segoe UI} -size 12 -weight bold")
        self.Label1.place(height=31, width=100, x=100, y=100)
        
        self.Entry1 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", insertbackground="black", selectbackground="blue",
                               selectforeground="white")
        self.Entry1.place(height=30, width=300, x=200, y=100)
        
        
        self.Label2 = tk.Label(window, activebackground="#f9f9f9", activeforeground="black", background="#f2f3f4",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='''Error:''', font="-family {Segoe UI} -size 12 -weight bold")
        self.Label2.place(height=31, width=115, x=110, y=150)
        
        self.Entry2 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", insertbackground="black", selectbackground="blue",
                               selectforeground="white")
        self.Entry2.place(height=30, width=100, x=200, y=150)
        
        
        self.Label3 = tk.Label(window, activebackground="#f9f9f9", activeforeground="black", background="#f2f3f4",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='''Max Iterations:''', font="-family {Segoe UI} -size 12 -weight bold")
        self.Label3.place(height=31, width=115, x=75, y=200)
        
        self.Entry3 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", insertbackground="black", selectbackground="blue",
                               selectforeground="white")
        self.Entry3.place(height=30, width=100, x=200, y=200)

        
        self.Label4 = tk.Label(window, activebackground="#f9f9f9", activeforeground="black", background="#f2f3f4",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='''xO:''', font="-family {Segoe UI} -size 12 -weight bold")
        self.Label4.place(height=31, width=200, x=80, y=250)
        
        self.Entry4 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", insertbackground="black", selectbackground="blue",
                               selectforeground="white")
        self.Entry4.place(height=30, width=100, x=200, y=250)

        
        self.Button1 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                 borderwidth="0", disabledforeground="#a3a3a3", foreground="#ffffff",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text="Solve",
                                 command=lambda: self.newtonMethod(self.Entry1.get(), self.Entry2.get(), self.Entry3.get(), self.Entry4.get()))
        self.Button1.place(height=30, width=100, x=700, y=300)
        
        self.Button2 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                 borderwidth="0", disabledforeground="#a3a3a3", foreground="#ffffff",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text="Back",
                                 command=self.back)
        self.Button2.place(height=30, width=100, x=850, y=300)
        
        
        global Frame1_1_2
        Frame1_1_2 = tk.Frame(window, relief='groove', borderwidth="2", background="#fffffe")
        Frame1_1_2.place(height=350, width=1000, x=150, y=350)
        
    
    def back(self):
        self.master.withdraw()
        
    def newtonMethod(self, equation, error, max_iterations, xo):
        fltError = float(error)
        intMax_iterations = int(max_iterations)
        fltxo = float(xo)
        result = newtonMethod(equation, fltError, intMax_iterations, fltxo)
        print("Newton Method Function Called")
        
        newtonMethod_table = ttk.Treeview(Frame1_1_2)
        newtonMethod_table['columns'] = ('i', 'xi', 'f(xi)', 'df(xi)', 'eps')
        newtonMethod_table.column("#0", width=0, stretch=NO)
        newtonMethod_table.column("i", anchor=CENTER, width=200)
        newtonMethod_table.column("xi", anchor=CENTER, width=200)
        newtonMethod_table.column("f(xi)", anchor=CENTER, width=200)
        newtonMethod_table.column("df(xi)", anchor=CENTER, width=200)
        newtonMethod_table.column("eps", anchor=CENTER, width=200)
        newtonMethod_table.heading("#0", text="", anchor=CENTER)
        newtonMethod_table.heading("i", text="Id", anchor=CENTER)
        newtonMethod_table.heading("xi", text="xi", anchor=CENTER)
        newtonMethod_table.heading("f(xi)", text="f(xi)", anchor=CENTER)
        newtonMethod_table.heading("df(xi)", text="df(xi)", anchor=CENTER)
        newtonMethod_table.heading("eps", text="eps", anchor=CENTER)
        

        for index, item in enumerate(result):
            newtonMethod_table.insert(parent='',index='end', iid=index,text='', values=item)

        newtonMethod_table.pack()

class Secant:
    def __init__(self, window=None):
        self.master = window
        window.geometry("1280x720+512+237")
        window.minsize(120, 1)
        window.maxsize(1370, 749)
        window.resizable(0, 0)
        window.title("Secant Method")
        window.configure(background="#f2f3f4")
        self.Label1 = tk.Label(window, activebackground="#f9f9f9", activeforeground="black", background="#f2f3f4",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='''Equation:''', font="-family {Segoe UI} -size 12 -weight bold")
        self.Label1.place(height=31, width=100, x=100, y=100)
        
        self.Entry1 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", insertbackground="black", selectbackground="blue",
                               selectforeground="white")
        self.Entry1.place(height=30, width=300, x=200, y=100)
        
        
        self.Label2 = tk.Label(window, activebackground="#f9f9f9", activeforeground="black", background="#f2f3f4",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='''Error:''', font="-family {Segoe UI} -size 12 -weight bold")
        self.Label2.place(height=31, width=115, x=105, y=150)
        
        self.Entry2 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", insertbackground="black", selectbackground="blue",
                               selectforeground="white")
        self.Entry2.place(height=30, width=100, x=200, y=150)
        
        
        self.Label3 = tk.Label(window, activebackground="#f9f9f9", activeforeground="black", background="#f2f3f4",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='''Max Iterations:''', font="-family {Segoe UI} -size 12 -weight bold")
        self.Label3.place(height=31, width=150, x=50, y=200)
        
        self.Entry3 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", insertbackground="black", selectbackground="blue",
                               selectforeground="white")
        self.Entry3.place(height=30, width=100, x=200, y=200)

        
        self.Label4 = tk.Label(window, activebackground="#f9f9f9", activeforeground="black", background="#f2f3f4",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='''xMinus1:''', font="-family {Segoe UI} -size 12 -weight bold")
        self.Label4.place(height=31, width=100, x=100, y=250)
        
        self.Entry4 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", insertbackground="black", selectbackground="blue",
                               selectforeground="white")
        self.Entry4.place(height=30, width=100, x=200, y=250)

        
        self.Label5 = tk.Label(window, activebackground="#f9f9f9", activeforeground="black", background="#f2f3f4",
                               disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='''xi:''', font="-family {Segoe UI} -size 12 -weight bold")
        self.Label5.place(height=31, width=100, x=125, y=300)
        
        self.Entry5 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3",
                               font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                               highlightcolor="black", insertbackground="black", selectbackground="blue",
                               selectforeground="white")
        self.Entry5.place(height=30, width=100, x=200, y=300)

        
        self.Button1 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                 borderwidth="0", disabledforeground="#a3a3a3", foreground="#ffffff",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text="Solve",
                                 command=lambda: self.secantMethod(self.Entry1.get(), self.Entry2.get(), self.Entry3.get(), self.Entry4.get(), self.Entry5.get()))
        self.Button1.place(height=30, width=100, x=700, y=300)
        
        self.Button2 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                 borderwidth="0", disabledforeground="#a3a3a3", foreground="#ffffff",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text="Back",
                                 command=self.back)
        self.Button2.place(height=30, width=100, x=850, y=300)
        
        
        global Frame1_1_2
        Frame1_1_2 = tk.Frame(window, relief='groove', borderwidth="2", background="#fffffe")
        Frame1_1_2.place(height=350, width=1000, x=150, y=350)
        
    
    def back(self):
        self.master.withdraw()
        
    def secantMethod(self, equation, error, max_iterations, xi_minus1, xi):
        fltError = float(error)
        intMax_iterations = int(max_iterations)
        fltxi_minus1 = float(xi_minus1)
        fltxi = float(xi)
        result = secantMethod(equation, fltError, intMax_iterations, fltxi_minus1, fltxi)
        print("Secant Method Function Called")
        
        secantMethod_table = ttk.Treeview(Frame1_1_2)
        secantMethod_table['columns'] = ('i', 'xi_minus1', 'f(xi_minus1)', 'xi', 'f(xi)', 'eps')
        secantMethod_table.column("#0", width=0, stretch=NO)
        secantMethod_table.column("i", anchor=CENTER, width=165)
        secantMethod_table.column("xi_minus1", anchor=CENTER, width=165)
        secantMethod_table.column("f(xi_minus1)", anchor=CENTER, width=165)
        secantMethod_table.column("xi", anchor=CENTER, width=165)
        secantMethod_table.column("f(xi)", anchor=CENTER, width=165)
        secantMethod_table.column("eps", anchor=CENTER, width=165)
        secantMethod_table.heading("#0", text="", anchor=CENTER)
        secantMethod_table.heading("i", text="Id", anchor=CENTER)
        secantMethod_table.heading("xi_minus1", text="xi_minus1", anchor=CENTER)
        secantMethod_table.heading("f(xi_minus1)", text="f(xi_minus1)", anchor=CENTER)
        secantMethod_table.heading("xi", text="xi", anchor=CENTER)
        secantMethod_table.heading("f(xi)", text="f(xi)", anchor=CENTER)
        secantMethod_table.heading("eps", text="eps", anchor=CENTER)
        
        

        for index, item in enumerate(result):
            secantMethod_table.insert(parent='',index='end', iid=index,text='', values=item)

        secantMethod_table.pack()
        
        
root = tk.Tk()
top = welcomeScreen(root)
root.mainloop()
