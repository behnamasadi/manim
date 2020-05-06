from sympy import *
init_printing(use_latex=True)
x = symbols('x')
equation=Eq(Integral(exp(x) * cos(x), x), exp(x) * sin(x) / 2 + exp(x) * cos(x) / 2)

pprint(equation)
pprint(equation,use_unicode=False)
print(latex(equation))

x = symbols('x')
y = symbols('y')
z = symbols('z')
g = symbols('g')
state = Matrix([x, y, z])
g = Matrix([x ** 2 + y ** 2, y - z])
g.jacobian(state)
