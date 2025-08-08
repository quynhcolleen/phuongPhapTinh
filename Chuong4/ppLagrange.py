from sympy import * # pyright: ignore[reportMissingModuleSource]
from tabulate import tabulate # pyright: ignore[reportMissingModuleSource]

x = symbols('x')

class PPLagrange:
    def __init__(self, _i, x_i, y_i):
        self._i = _i
        self.x_i = x_i
        self.y_i = y_i
        
    def bangGiaTri(self):
        table = [["xi"] + self.x_i, ["yi"] + self.y_i]
        print(tabulate(table, tablefmt="grid", stralign="center"))
    
    def Lagrange(self):
        
        self.bangGiaTri()
        print("\nXay dung da thuc co so L_i(x):")

        n = self._i
        L_list = []  # Danh sách các L_i(x)

        for i in range(n):
            tuSo = 1
            mauSo = 1
            for j in range(n):
                if j != i:
                    tuSo *= (x - self.x_i[j])
                    mauSo *= (self.x_i[i] - self.x_i[j])
            Li = tuSo / mauSo
            L_list.append(Li)
            print(f"L_{i}(x) = {nsimplify(Li)}")
        
        Px = 0
        for i in range(n):
            Px += self.y_i[i] * L_list[i]
            
        Px = expand(Px)
        print(f"Da thuc noi suy Lagrange P(x) la: {N(Px, 7)}")
 