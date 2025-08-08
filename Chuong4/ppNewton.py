from sympy import symbols, N, evalf, expand # pyright: ignore[reportMissingModuleSource]
from tabulate import * # pyright: ignore[reportMissingModuleSource]

x = symbols('x')

class NoiSuyNewton:
    def __init__(self, _i, x_i, y_i):
        self._i = _i
        self.x_i = x_i
        self.y_i = y_i
        
    def bangGiaTri(self):
        print("Ham y = f(x):\n")
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
                    tsp_print[i][j] = N(tsp[i][j], 5)
        
                
        headers = ["x", "y"] + [f"TSP {k}" for k in range(1, n)]
        table_data = []
        for i in range(n):
            row = [self.x_i[i], self.y_i[i]] + tsp_print[i]
            table_data.append(row)
        
        print(tabulate(table_data, headers=headers, tablefmt="grid", stralign="center"))
        print() 
        
        tsp_final = []
        for i in range(1, n):
            tsp_final.append(tsp[i][i - 1])
         
        nhan = []  
        khai_trien = []
        
        for i in range(n - 1):
            tich = 1
            for j in range(i + 1):
                tich *= (x - self.x_i[j])
            khai_trien.append(expand(tich))
               
        ptNewton = self.y_i[0] + sum(tsp_final[i] * khai_trien[i] for i in range(n - 1))
        
        print("Phuong trinh noi suy Newton:")
        print("P(x) =", ptNewton.evalf(10))
