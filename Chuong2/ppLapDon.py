from sympy import *  # pyright: ignore[reportMissingModuleSource]
from sympy.calculus.util import continuous_domain # pyright: ignore[reportMissingModuleSource]

x = symbols('x')

class PPLapDon:
    def __init__(self, hamSo, left, right, gioiHanSaiSo):
        self.parsedFunction = sympify(hamSo)
        self.left = left
        self.right = right
        self.gioiHanSaiSo = gioiHanSaiSo
        self.interval = Interval(left, right, left_open=True, right_open=True)

    def LapDon(self):
        pt_init = self.parsedFunction
        terms = collect(self.parsedFunction, x, evaluate=False)
        mu_list = []
        for t in terms:
            if t == x:
                mu_list.append(1)
            elif t.is_Pow and t.base == x:
                mu_list.append(t.exp)
        mu_list = list(set(mu_list))

        pt_lap = []
        for mu in mu_list:
            ve_trai = x**mu
            bieu_thuc_con_lai = simplify(pt_init - terms.get(ve_trai, 0) * ve_trai)
            he_so = terms.get(ve_trai, 0)
            ve_phai_mu = simplify(-bieu_thuc_con_lai / he_so)
            g_x = Pow(ve_phai_mu, 1 / mu)
            pt_lap.append(nsimplify(g_x))

        while True:
            print("\nCac phuong trinh lap x = g(x) kha thi:")
            for i, g in enumerate(pt_lap):
                print(f"{i + 1}. x = {g}")
            
            try:
                chon = int(input("Chon phuong trinh lap (chon 0 de tu nhap phuong trinh lap): "))
                if chon == 0:
                    user_input = input("\nNhap phuong trinh lap g(x): ")
                    pt_lap_test = sympify(user_input)
                else:
                    pt_lap_test = pt_lap[chon - 1]
            except:
                print("Lua chon khong hop le. Thu lai.\n")
                continue

            # Kiểm tra điều kiện hội tụ
            closed_interval = Interval(self.left, self.right, False, False)
            g_prime = diff(pt_lap_test, x)
            g_prime_2 = diff(g_prime, x)

            f_lambdified = lambdify(x, g_prime)
            critical_points = solveset(g_prime_2, x, domain=closed_interval)
            values = []

            try:
                for point in critical_points:
                    if point.is_real and self.left <= point <= self.right:
                        values.append(abs(f_lambdified(point)))
                values.append(abs(f_lambdified(self.left)))
                values.append(abs(f_lambdified(self.right)))
            except:
                print("Khong the danh gia dao ham tren khoang. Chon lai phuong trinh.")
                continue

            q = max(values)

            if q >= 1:
                print(f"Phuong trinh lap '{pt_lap_test}' khong hoi tu do q = {N(q):.7f} >= 1. Chon lai.\n")
                continue

            print(f"Phuong trinh lap '{pt_lap_test}' hop le vi q = {N(q):.7f} < 1\n")
            break

        # Lặp đơn
        
        pt_lap_final = lambdify(x, pt_lap_test)
        x_curr = float(input("Nhap gia tri x0: "))

        x_list = [x_curr]
        x_next = pt_lap_final(x_curr)
        x_list.append(x_next)
        print(f"Lap lan thu 1, x1 = {N(x_next):.7f}")
        n = ceiling(log(self.gioiHanSaiSo * (1 - q) / Abs(x_next - x_curr)) / log(q))
        x_curr = x_next
        
        for i in range(2, n + 1):
            x_next = pt_lap_final(x_curr)
            x_list.append(x_next)
            print(f"Lap lan thu {i}, x{i} = {N(x_next):.7f}")
            x_curr = x_next

        saiSo = (q / (1 - q)) * Abs(x_list[-1] - x_list[-2])
        print(f"Ket qua:, {N(x_list[-1]):.7f} ±, {N(saiSo):.7f}")
