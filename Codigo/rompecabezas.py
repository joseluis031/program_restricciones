from ortools.sat.python import cp_model # Importamos la libreria de ortools

# Definimos el modelo
modelo = cp_model.CpModel()

# Definimos las variables
base = 10

c = modelo.NewIntVar(1, base - 1, "C")
p = modelo.NewIntVar(0, base - 1, "P")
i = modelo.NewIntVar(1, base - 1, "I")
s = modelo.NewIntVar(0, base - 1, "S")
f = modelo.NewIntVar(1, base - 1, "F")
u = modelo.NewIntVar(0, base - 1, "U")
n = modelo.NewIntVar(0, base - 1, "N")
t = modelo.NewIntVar(1, base - 1, "T")
r = modelo.NewIntVar(0, base - 1, "R")
e = modelo.NewIntVar(0, base - 1, "E")


letters = [c, p, i, s, f, u, n, t, r, e]    # Letras

assert base >= len(letters) # Verificamos que la base sea mayor o igual a la cantidad de letras

# Definimos las restricciones
modelo.AddAllDifferent(letters)

# CP + IS + FUN = TRUE
modelo.Add(
    c * base + p + i * base + s + f * base * base + u * base + n
    == t * base * base * base + r * base * base + u * base + e
)

