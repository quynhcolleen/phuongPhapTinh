from sympy import *  # pyright: ignore[reportMissingModuleSource]
from sympy.calculus.util import continuous_domain  # pyright: ignore[reportMissingModuleSource]
x = symbols('x')

class KiemTraKCLN:
    def __init__(self, hamSo, left: float, right: float):
        self.parsedFunction = sympify(hamSo)
        self.left = left
        self.right = right
        self.interval = Interval(left, right, left_open=True, right_open=True)
        
    def lienTuc(self) -> bool:
        domain = continuous_domain(self.parsedFunction, x, S.Reals)
        return self.interval.is_subset(domain)
    
    def donDieu(self) -> bool:
        f_prime = simplify(diff(self.parsedFunction, x))
        domain_df = continuous_domain(f_prime, x, S.Reals)
        
        if not self.interval.is_subset(domain_df):
            return False

        nghiem = solveset(Eq(f_prime, 0), x, domain=self.interval)
        if len(nghiem) > 0:
            return False
        
        return True
    
    def traiDau(self) -> bool:
        fa = self.parsedFunction.subs(x, self.left).evalf()
        fb = self.parsedFunction.subs(x, self.right).evalf()
        return fa * fb < 0

    def kcln(self) -> bool:
        if not self.lienTuc():
            print("Hàm không liên tục trên khoảng.")
            return False
        if not self.donDieu():
            print("Hàm không đơn điệu trên khoảng.")
            return False
        if not self.traiDau():
            print("f(a) * f(b) ≥ 0 → không phải khoảng cách ly nghiệm.")
            return False
        print("(a, b) là khoảng cách ly nghiệm hợp lệ của phương trình f(x) = 0")
        return True
