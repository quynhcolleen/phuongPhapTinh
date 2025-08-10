from sympy import symbols, sympify, Interval, simplify, solveset, diff, lambdify, N # pyright: ignore[reportMissingModuleSource]
from tabulate import * # pyright: ignore[reportMissingModuleSource]

x = symbols('x')
        
class HinhThang:
    def __init__(self, hamSo, tren, duoi, amount):
        self.parsedFunction = sympify(hamSo)
        self.a = duoi
        self.b = tren
        self.n = amount     # Số đoạn chia
        
    def hinhThang(self):
        h = (self.b - self.a) / self.n
        x_i = [self.a + i * h for i in range (self.n + 1)]
        y_i = [self.parsedFunction.subs(x, x_i[i]).evalf() for i in range(self.n + 1)]
        
        table = [["i"] + list(range(len(x_i))), 
                 ["x_i"] + x_i, 
                 ["y_i"] + y_i]
        print(tabulate(table, tablefmt="grid", stralign="center"))
        print(f"\nh = {h}\n")
        
        middle_sum = sum(y_i[1:-1])
        tichPhan = (h / 2) * (y_i[0] + y_i[-1] + 2 * middle_sum)
        
        closed_interval = Interval(self.a, self.b, left_open=False, right_open=False)
        f_secondDeriative = simplify(diff(self.parsedFunction, x, 2))
        critical_points_2 = solveset(diff(f_secondDeriative, x), x, domain=closed_interval)
        f_second_lambdified = lambdify(x, f_secondDeriative)
        values = []
        
        for pt in critical_points_2:
            if pt.is_real and self.a <= pt <= self.b:
                values.append(f_second_lambdified(pt))
        values.append(f_second_lambdified(self.a))
        values.append(f_second_lambdified(self.b))

        M2 = max(map(abs, values))
        
        saiSo = (M2 / 12) * (self.b - self.a) * h**2
        print(f"ket qua: I = {tichPhan} ± {N(saiSo):.7f}")
        
