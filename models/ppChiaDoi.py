from sympy import *  # pyright: ignore[reportMissingModuleSource]
from models.lamTronSo import *

x = symbols('x')

class PPChiaDoi:
    
    def __init__(self, hamSo, left: float, right: float, gioiHanSaiSo: float):
        self.parsedFunction = sympify(hamSo)
        self.left = left
        self.right = right
        self.gioiHanSaiSo = gioiHanSaiSo
        
    def chiaDoi(self) -> float:
        fa = self.parsedFunction.subs(x, self.left).evalf()
        fb = self.parsedFunction.subs(x, self.right).evalf()
        
        a = self.left
        b = self.right
        n = int(ceiling((log(abs(self.right - self.left) / self.gioiHanSaiSo))/log(2)))
        print("So lan chia doi la:", n)
        
        x_list = []
        x0 = (a + b) / 2
        print("x0 =", x0)
        
        for i in range(n):
            x_temp = (a + b) / 2
            x_list.append(x_temp)
            z = self.parsedFunction.subs(x, x_temp).evalf()
            if z * fa < 0:
                b = x_temp
                fb = z
            else:
                a = x_temp
                fa = z
            
            output = f"Chia doi lan thu {i + 1}, x{i} = {x_temp}"
            print(output)
        
        print("\n")
        saiSo = x_list[-1] - x_list[-2]
        print("Ket qua:", lamTron(x_list[-1]), "±", lamTron(saiSo))
        
        
            
            