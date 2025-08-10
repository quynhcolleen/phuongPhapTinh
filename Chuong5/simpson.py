from sympy import symbols, sympify, Interval, simplify, solveset, diff, lambdify, N # pyright: ignore[reportMissingModuleSource]
from tabulate import tabulate # pyright: ignore[reportMissingModuleSource]

x = symbols('x')

class Simpson:
    def __init__(self, hamSo, a, b, n):
        if n % 2 != 0:
            raise ValueError("So doan chia n phai la so chan.")
        self.parsedFunction = sympify(hamSo)
        self.a = a
        self.b = b
        self.n = n 

    def simpson(self):
        h = (self.b - self.a) / self.n

        x_i = [self.a + i * h for i in range(self.n + 1)]
        y_i = [self.parsedFunction.subs(x, xi).evalf() for xi in x_i]

        table = [["i"] + list(range(len(x_i))),
                 ["x_i"] + x_i,
                 ["y_i"] + y_i]
        print(tabulate(table, tablefmt="grid", stralign="center"))
        print(f"\nh = {h}\n")

        sum_le = sum(y_i[1:-1:2]) 
        sum_chan = sum(y_i[2:-1:2]) 

        tichPhan = (h / 3) * (y_i[0] + y_i[-1] + 4 * sum_le + 2 * sum_chan)

        closed_interval = Interval(self.a, self.b, left_open=False, right_open=False)
        f_4th = simplify(diff(self.parsedFunction, x, 4))
        critical_points_4 = solveset(diff(f_4th, x), x, domain=closed_interval)
        f4_lamb = lambdify(x, f_4th)
        values = []

        for pt in critical_points_4:
            if pt.is_real and self.a <= pt <= self.b:
                values.append(f4_lamb(pt))
        values.append(f4_lamb(self.a))
        values.append(f4_lamb(self.b))

        M4 = max(map(abs, values))
        saiSo = (M4 / 180) * (self.b - self.a) * (h**4)

        print(f"Ket qua: I = {tichPhan} ± {N(saiSo):.7f}")