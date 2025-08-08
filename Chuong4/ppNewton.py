from sympy import * # pyright: ignore[reportMissingModuleSource]
from tabulate import * # pyright: ignore[reportMissingModuleSource]

x = symbols('x')

class NoiSuyNewton:
    def __init__(self, _i, x_i, y_i):
        self._i = _i
        self.x_i = x_i
        self.y_i = y_i
        
    def bangGiaTri(self):
        table = [["xi"] + self.x_i, ["yi"] + self.y_i]
        print(tabulate(table, tablefmt="grid", stralign="center"))
        print()
    
    def Newton(self):
        n = self._i
        self.bangGiaTri()
        
        print("Thiet lap bang gia tri ti sai phan:\n")
        tsp = [[None for _ in range(n - 1)] for _ in range(n)]

        for i in range(1, n):
            tsp[i][0] = (self.y_i[i] - self.y_i[i - 1]) / (self.x_i[i] - self.x_i[i - 1])
            
        bac_tsp = 2
        for j in range(1, n - 1):
            for i in range(j + 1, n):
                tsp[i][j] = (tsp[i][j - 1] - tsp[i - 1][j - 1]) / (self.x_i[i] - self.x_i[i - bac_tsp])
            bac_tsp += 1
        
        tsp_print = [["" for _ in range(n - 1)] for _ in range(n)]
        for i in range (n):
            for j in range (n - 1):
                if tsp[i][j] != None:
                    tsp_print[i][j] = Rational(tsp[i][j]).limit_denominator()
        
                
        headers = ["x", "y"] + [f"TSP {k}" for k in range(1, n)]
        table_data = []
        for i in range(n):
            row = [self.x_i[i], self.y_i[i]] + tsp_print[i]
            table_data.append(row)
        
        print(tabulate(table_data, headers=headers, tablefmt="grid", stralign="center"))
        
           
x_data = [1.2, 1.4, 1.8, 2.0]
y_data = [3, 3.5, 4, 4.3]

ns = NoiSuyNewton(4, x_data, y_data)
ns.Newton()