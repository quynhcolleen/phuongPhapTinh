from sympy import * # pyright: ignore[reportMissingModuleSource]
from Chuong2.lamTronSo import *
from sympy.calculus.util import continuous_domain, minimum, maximum  # pyright: ignore[reportMissingModuleSource]

x = symbols('x')

class PPNewton:
    
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
        
    def Newton(self) -> float:
        x_curr = self.right
        
        # Tìm m1 & M2:
        
        closed_interval = Interval(self.left, self.right, left_open=False, right_open=False)
        f_prime = diff(self.parsedFunction, x)
        f_secondDeriative = simplify(diff(self.parsedFunction, x, 2))
        
        critical_points_1 = solveset(f_secondDeriative, x, domain=closed_interval)
        f_lambdified = lambdify(x, f_prime)
        values = []
        
        for point in critical_points_1:
            if point.is_real and self.left <= point <= self.right:
                values.append(f_lambdified(point))
        values.append(f_lambdified(self.left))
        values.append(f_lambdified(self.right))
        
        m1 = min(map(abs, values))
        
        critical_points_2 = solveset(diff(f_secondDeriative, x), x, domain=closed_interval)
        f_second_lambdified = lambdify(x, f_secondDeriative)
        values_second = []
        
        for pt in critical_points_2:
            if pt.is_real and self.left <= pt <= self.right:
                values_second.append(f_second_lambdified(pt))
        values_second.append(f_second_lambdified(self.left))
        values_second.append(f_second_lambdified(self.right))

        M2 = max(map(abs, values_second))

        # Chọn x0
        # f_x0_start là biến lưu giá trị ban đầu của f(x0) khi chọn x 
        f_x0_start = self.parsedFunction.subs(x, x_curr).evalf()
        f_second_x0 = f_secondDeriative.subs(x,x_curr).evalf()
        
        if f_x0_start * f_second_x0 < 0:
            x_curr = self.left
           
        # Phương pháp tiếp tuyến (Newton)
        
        if m1 == 0:
            print("Khong the danh gia sai so do m1 = 0.") 
            return None
                    
        x_list = []
        while True:
            f_x0 = self.parsedFunction.subs(x, x_curr).evalf()
            f_phay_x0 = f_prime.subs(x,x_curr).evalf()

            x_next = x_curr - f_x0/f_phay_x0
            err = abs(self.parsedFunction.subs(x, x_next).evalf()) / m1
            x_list.append(x_next)
            i = len(x_list)
            output = f"Lap lan thu {i}, x{i} = {x_next}"
            print(output)
            if err < self.gioiHanSaiSo:
                break
            x_curr = x_next
      
        saiSo = lamTron((M2 / (2 * m1)) * Abs(x_list[-1] - x_list[-2])**2)
        print("Ket qua:", lamTron(x_list[-1]), "±", saiSo)
            
        
        
        