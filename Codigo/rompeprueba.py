from ortools.sat.python import cp_model # Importamos la libreria de ortools

# Definimos el modelo
modelo = cp_model.CpModel()

# Definimos las variables
a = modelo.NewIntVar(0, 9, 'a')
b = modelo.NewIntVar(0, 9, 'b')
c = modelo.NewIntVar(0, 9, 'c')
d = modelo.NewIntVar(0, 9, 'd')
e = modelo.NewIntVar(0, 9, 'e')
f = modelo.NewIntVar(0, 9, 'f')
g = modelo.NewIntVar(0, 9, 'g')
h = modelo.NewIntVar(0, 9, 'h')
i = modelo.NewIntVar(0, 9, 'i')

# Definimos las restricciones
modelo.Add(a + b + c == 15)
modelo.Add(d + e + f == 15)
modelo.Add(g + h + i == 15)
modelo.Add(a + d + g == 15)
modelo.Add(b + e + h == 15)
modelo.Add(c + f + i == 15)
modelo.Add(a + e + i == 15)
modelo.Add(c + e + g == 15)

# Definimos el solver
solver = cp_model.CpSolver()
# Ejecutamos el solver
status = solver.Solve(modelo)

# Imprimimos la solucion
print('a =', solver.Value(a))
print('b =', solver.Value(b))
print('c =', solver.Value(c))
print('d =', solver.Value(d))
print('e =', solver.Value(e))
print('f =', solver.Value(f))
print('g =', solver.Value(g))
print('h =', solver.Value(h))
print('i =', solver.Value(i))
print('Tiempo:', solver.WallTime(), 'ms')

# Imprimimos la solucion en una matriz

print('Solucion:')
print(solver.Value(a), solver.Value(b), solver.Value(c))
print(solver.Value(d), solver.Value(e), solver.Value(f))
print(solver.Value(g), solver.Value(h), solver.Value(i))
print('Tiempo:', solver.WallTime(), 'ms')
