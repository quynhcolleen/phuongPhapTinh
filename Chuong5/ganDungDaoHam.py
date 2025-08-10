from sympy import symbols # pyright: ignore[reportMissingModuleSource]
from tabulate import * # pyright: ignore[reportMissingModuleSource]
import os

x = symbols('x')

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
        
class tinhGanDung:
    def __init__(self, x_i, y_i):
        self.x_i = x_i
        self.y_i = y_i
        self.h = x_i[1] - x_i[0]
        
    def bangGiaTri(self):
        i_values = list(range(len(self.x_i) + 1))
        table = [["i"] + i_values, ["xi"] + self.x_i, ["yi"] + self.y_i]
        print(tabulate(table, tablefmt="grid", stralign="center"))
        print(f"\nh = {self.h}")
        
    def tinh_dao_ham(self, idx, mode):
        if mode == 1: 
            return (-3*self.y_i[idx] + 4*self.y_i[idx+1] - self.y_i[idx+2]) / (2*self.h)
        elif mode == 2:  
            return (-self.y_i[idx-1] + self.y_i[idx+1]) / (2*self.h)
        elif mode == 3: 
            return (self.y_i[idx-2] - 4*self.y_i[idx-1] + 3*self.y_i[idx]) / (2*self.h)
        
def congThucDiem(self):
        while True:
            clear_screen()
            self.bangGiaTri()
            print("\nTinh gan dung dao ham. Chon cong thuc:")
            print("1. Cong thuc can trai.")
            print("2. Cong thuc trung tam.")
            print("3. Cong thuc can phai.")
            print("0. Thoát.")
            
            try:
                choice = int(input("Lua chon: "))
            except ValueError:
                print("Vui long nhap so.")
                input("Nhan Enter de tiep tuc...")
                continue

            if choice == 0:
                break
            elif choice not in (1, 2, 3):
                print("Khong hop le.")
                input("Nhan Enter de tiep tuc...")
                continue

            if choice == 1:
                idx_range = range(0, len(self.x_i)-2)
            elif choice == 2:
                idx_range = range(1, len(self.x_i)-1)
            else:
                idx_range = range(2, len(self.x_i))

            try:
                idx = int(input(f"Nhap moc i {list(idx_range)}: "))
                if idx not in idx_range:
                    raise ValueError
            except ValueError:
                print("Moc i khong hop le.")
                input("Nhan Enter de tiep tuc...")
                continue

            val = self.tinh_dao_ham(idx, choice)
            print(f"y'({self.x_i[idx]}) ≈ {val:.6f}")
            input("\nNhan Enter de tiep tuc...")