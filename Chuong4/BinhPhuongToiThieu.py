from sympy import symbols, sympify, diff, simplify, lambdify, sin, cos, exp # pyright: ignore[reportMissingModuleSource]
import numpy as np # pyright: ignore[reportMissingImports]
from scipy.optimize import curve_fit # pyright: ignore[reportMissingImports]

x = symbols('x')

class BinhPhuongToiThieu:
    def __init__(self, x_i, y_i):
        self.x_i = np.array(x_i, dtype=float)
        self.y_i = np.array(y_i, dtype=float)
        
    def BPTT(self):

        hamTN_input = input("Nhap dang ham thuc nghiem f(x): ")
        hamTN = sympify(hamTN_input, locals={'cos': cos, 'sin': sin, 'exp': exp})
        thamSo = sorted(hamTN.free_symbols - {x}, key=lambda s: s.name)
        
        def tuyenTinh(expr, params):
            for p in params:
                if diff(expr, p, 2) != 0: 
                    return False
            return True
        
        if tuyenTinh(hamTN, thamSo):
            print("Ham tuyen tinh.")
            
            A = []
            for p in thamSo:
                term = simplify(hamTN.coeff(p))
                func = lambdify(x, term, 'numpy')
                A.append(func(self.x_i))
                
            A = np.column_stack(A)
            coeffs, residuals, _, _ = np.linalg.lstsq(A, self.y_i, rcond=None)
            
            for p, c in zip(thamSo, coeffs):
                print(f"{p} = {c:.7f}")
            print("Sai so binh phuong toi thieu:", residuals)
            
            hamTN_final = hamTN
            for p, c in zip(thamSo, coeffs):
                hamTN_final = hamTN_final.subs(p, c)
            print("Ham thuc nghiem: y =", hamTN_final.evalf(7))
        
        else:
            print("Ham phi tuyen.")
            def model_func(x_data, *params):
                subs_dict = dict(zip(thamSo, params))
                return np.array([float(hamTN.subs({x: xv, **subs_dict})) for xv in x_data])
            
            p0 = [1.0] * len(thamSo)
            coeffs, _ = curve_fit(model_func, self.x_i, self.y_i, p0=p0)
            for p, c in zip(thamSo, coeffs):
                print(f"{p} = {c:.7f}")
            
            hamTN_final = hamTN
            for p, c in zip(thamSo, coeffs):
                hamTN_final = hamTN_final.subs(p, c)
            print("Ham thuc nghiem: y =", simplify(hamTN_final).evalf(7))

