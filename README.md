# program_restricciones
Grupo formado por: José Luis Rodríguez y Alexandre Muñoz


El link de este repositorio es el siguiente: [GitHub](https://github.com/joseluis031/program_restricciones.git)

# Código rompecabezas
El rompecabezas criptográfico es un ejercicio matemático en el que los dígitos de algunos números se representan con letras (o símbolos). Cada letra representa un dígito único. El objetivo es encontrar los dígitos de modo que se verifique una determinada ecuación matemática:

CP + IS + FUN = TRUE

Una asignación de letras a dígitos proporciona la siguiente ecuación:

23 + 74 + 968 = 1065

```
from ortools.sat.python import cp_model # Importamos la libreria de ortools
from impresora import *
# Definimos el modelo
modelo = cp_model.CpModel()

# Definimos las variables
#Usamos NewIntVar, para declarar nuestros dígitos (números enteros).
#Distinguimos entre las letras que pueden ser cero y las que no (C, I, F y T).
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
#Primero, nos aseguramos de que todas las letras tengan valores diferentes con el método auxiliar AddAllDifferent.
#Luego, usamos el método de ayuda AddEquality para crear restricciones que apliquen la igualdad CP + IS + FUN = TRUE.

modelo.AddAllDifferent(letters)

# CP + IS + FUN = TRUE
modelo.Add(
    c * base + p + i * base + s + f * base * base + u * base + n
    == t * base * base * base + r * base * base + u * base + e
)


def main():
    solver = cp_model.CpSolver()
    impresion = impresora(letters)
    # Enumerate all solutions.
    solver.parameters.enumerate_all_solutions = True
    # Solve.
    status = solver.Solve(modelo, impresion)

    # Statistics.
    print("\Estadisticas")
    print(f"  estado   : {solver.StatusName(status)}")
    print(f"  conflictos: {solver.NumConflicts()}")
    print(f"  branches : {solver.NumBranches()}")
    print(f"  Tiempo: {solver.WallTime()} s")
    print(f"  soluciones encontradas: {impresion.solution_count()}, (1 solucion cada fila)")
```

# Código impresora
#muestra cada solución a medida que la encuentra.
```
from ortools.sat.python import cp_model # Importamos la libreria de ortools




class impresora(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__contador = 0

    def on_solution_callback(self):
        self.__contador += 1
        for v in self.__variables:
            print(f"{v}={self.Value(v)}", end=" ")
        print()

    def solution_count(self):
        return self.__contador
```

# Codigo run
```
from rompecabezas import main  

if __name__ == "__main__":
    main()
```
