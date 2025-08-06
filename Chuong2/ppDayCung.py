from sympy import * # pyright: ignore[reportMissingModuleSource]
from sympy.calculus.util import continuous_domain, minimum, maximum  # pyright: ignore[reportMissingModuleSource]

x = symbols('x')

class PPDayCung:
    
    def __init__(self, hamSo, left, right, gioiHanSaiSo):
        self.parsedFunction = sympify(hamSo)
        self.left = left
        self.right = right
        self.gioiHanSaiSo = gioiHanSaiSo
        self.interval = Interval(left, right, left_open=True, right_open=True)
    
    def dieuKienLap(self) -> bool:
        f_secondDeriative = simplify(diff(self.parsedFunction, x, 2))
        domain_df = continuous_domain(f_secondDeriative, x, S.Reals)
        
        if not self.interval.is_subset(domain_df):
            return False

        nghiem = solveset(Eq(f_secondDeriative, 0), x, domain=self.interval)
        if len(nghiem) > 0:
            return False

        return True
        
    def dayCung(self) -> float:
        d = self.left
        x_curr = self.right
        
        # Tìm m1 & M1:
        
        closed_interval = Interval(self.left, self.right, left_open=False, right_open=False)
        f_prime = diff(self.parsedFunction, x)
        f_secondDeriative = simplify(diff(self.parsedFunction, x, 2))
        critical_points = solveset(f_secondDeriative, x, domain=closed_interval)
        f_lambdified = lambdify(x, f_prime)
        values = []
        
        for point in critical_points:
            if point.is_real and self.left <= point <= self.right:
                values.append(f_lambdified(point))
        values.append(f_lambdified(self.left))
        values.append(f_lambdified(self.right))
        m1 = min(map(abs, values))
        M1 = max(map(abs, values))

        # Thực hiện phương pháp dây cung

        fd = self.parsedFunction.subs(x, d).evalf()       
        f_second_d = f_secondDeriative.subs(x, d).evalf()
        
        if fd * f_second_d < 0:
            d = self.right
            x_curr = self.left
        if m1 == 0:
            print("Khong the danh gia sai so do m1 = 0.")   
            return None 
        x_list = []
        print("x0 =", x_curr, "& d =", d)
        while True:    
            f_x_curr = self.parsedFunction.subs(x, x_curr).evalf()
            x_next = x_curr - ((f_x_curr * (x_curr - d)) / (f_x_curr - fd))
            err = abs(self.parsedFunction.subs(x, x_next).evalf()) / m1
            x_list.append(x_next)
            i = len(x_list)
            output = f"Lap lan thu {i}, x{i} = {x_next}"
            print(output)
            if err < self.gioiHanSaiSo:
                break
            x_curr = x_next
               
        saiSo = (M1 - m1) * Abs(x_list[-1] - x_list[-2]) / m1
        print(f"Ket qua: {N(x_list[-1]):.7f} ± {N(saiSo):.7f}")
