# program_restricciones
Grupo formado por: José Luis Rodríguez y Alexandre Muñoz


El link de este repositorio es el siguiente: [GitHub](https://github.com/joseluis031/program_restricciones.git)

# Código rompecabezas
```
from ortools.sat.python import cp_model # Importamos la libreria de ortools
from impresora import *
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
