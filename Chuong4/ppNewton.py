from sympy import symbols, N, expand, diff, factorial, simplify, sympify # pyright: ignore[reportMissingModuleSource]
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
    
    def NewtonBatKy(self):
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
                    tsp_print[i][j] = N(tsp[i][j], 7)
        
        headers = ["x", "y"] + [f"TSP {k}" for k in range(1, n)]
        table_data = []
        for i in range(n):
            row = [self.x_i[i], self.y_i[i]] + tsp_print[i]
            table_data.append(row)
        
        print(tabulate(table_data, headers=headers, tablefmt="grid", stralign="center"))
        print()
        print("Chon cong thuc noi suy Newton tuong ung:")
        print("1. Noi suy Newton tien.")
        print("2. Noi suy Newton lui.")
        pp = int(input("Lua chon: "))
        print()
        match pp:
            case 1:
                tsp_final = []
                for i in range(1, n):
                    tsp_final.append(tsp[i][i - 1])
                
                phuong_trinh = []
                
                for i in range(n - 1):
                    tich = 1
                    for j in range(i + 1):
                        tich *= (x - self.x_i[j])
                    phuong_trinh.append(expand(tich))
                    
                ptNewton = self.y_i[0] + sum(tsp_final[i] * phuong_trinh[i] for i in range(n - 1))
                
                print("Phuong trinh noi suy Newton:")
                print("P(x) =", ptNewton.evalf(10))
                print()
                
                while True:
                    x_val = input("Nhap x de tinh f(x) và f'(x) (Nhap 'x' de ket thuc chuong trinh): ")
                    if x_val.lower() == 'x':
                        exit()
                    try:
                        x_input = float(x_val)
                        f_x = ptNewton.subs(x, x_input).evalf(9)
                        f_prime = diff(ptNewton, x).subs(x, x_input).evalf(9)
                        print(f"f({x_input}) = {f_x}")
                        print(f"f'({x_input}) = {f_prime}")
                    except ValueError:
                        print("Gia tri dau vao khong hop le.")
                        
            case 2:
                tsp_final = []
                for i in range(n - 1):
                    tsp_final.append(tsp[n - 1][i])  
                          
                x_lui = self.x_i[::-1]
                phuong_trinh = []
                
                for i in range(n - 1):
                    tich = 1
                    for j in range(i + 1):
                        tich *= (x - x_lui[j])
                    phuong_trinh.append(expand(tich))
                    
                ptNewton = self.y_i[-1] + sum(tsp_final[i] * phuong_trinh[i] for i in range(n - 1))
                
                print("Phuong trinh noi suy Newton:")
                print("P(x) =", ptNewton.evalf(10))
                print()
                
                while True:
                    x_val = input("Nhap x de tinh f(x) và f'(x) (Nhap 'x' de ket thuc chuong trinh): ")
                    if x_val.lower() == 'x':
                        exit()
                    try:
                        x_input = float(x_val)
                        f_x = ptNewton.subs(x, x_input).evalf(9)
                        f_prime = diff(ptNewton, x).subs(x, x_input).evalf(9)
                        print(f"f({x_input}) = {f_x}")
                        print(f"f'({x_input}) = {f_prime}")
                    except ValueError:
                        print("Gia tri dau vao khong hop le.")              
                
    def NewtonCachDeu(self):
        t = symbols('t')
        n = self._i
        self.bangGiaTri()
        
        print("Thiet lap bang gia tri ti sai phan:\n")
        tsp = [[None for _ in range(n - 1)] for _ in range(n)]

        for i in range(1, n):
            tsp[i][0] = self.y_i[i] - self.y_i[i - 1]
            
        for j in range(1, n - 1):
            for i in range(j + 1, n):
                tsp[i][j] = tsp[i][j - 1] - tsp[i - 1][j - 1]
        
        tsp_print = [["" for _ in range(n - 1)] for _ in range(n)]
        for i in range (n):
            for j in range (n - 1):
                if tsp[i][j] != None:
                    tsp_print[i][j] = N(tsp[i][j], 7)
        
                
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
        
        ptNewton = self.y_i[0]
        tich = 1

        for i in range(1, n):
            tich *= (t - (i - 1))
            ptNewton += (tich / factorial(i)) * tsp_final[i - 1]

        ptNewton = simplify(expand(ptNewton), 7)
        print("Phuong trinh noi suy Newton moc cach deu:")
        print("P(t) =", ptNewton.evalf(10))
        
        while True:
            x_fx = input("Nhap f(x) (t = f(x) theo yeu cau) (Nhap 'x' de ket thuc chuong trinh): ")
            if x_fx.lower() == 'x':
                exit()
            try:
                x_input = sympify(x_fx)
                user_input = input("Nhap gia tri x: ")
                x_val = float(user_input)
                t_val = x_input.subs(x, x_val).evalf()
                f_t = ptNewton.subs(t, t_val).evalf(9)
                f_prime = diff(ptNewton, t).subs(t, t_val).evalf(9)
                print(f"y({x_val}) = P({t_val.evalf(2)}) = {f_t}")
                print(f"y'({x_val}) = P'({t_val.evalf(2)}) = {f_prime}")
                
            except ValueError:
                print("Gia tri dau vao khong hop le.")