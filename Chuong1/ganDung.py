from sympy import symbols, sympify, diff # pyright: ignore[reportMissingModuleSource]

class SaiSoChuong1:
    def __init__(self, hamSo):
        self.parsedFunction = sympify(hamSo)
        self.bien_list = sorted(list(self.parsedFunction.free_symbols), key=lambda x: x.name)
        self.values = {}  
        self.errors = {} 

    def uocLuong(self):
        print("Nhap gia tri va sai so tuyet doi cho tung bien:\n")
        for bien in self.bien_list:
            val = float(input(f"{bien} = "))
            err = float(input(f"Sai so tuyet doi cua {bien}: "))
            self.values[bien] = val
            self.errors[bien] = err

        tongSaiSo = 0
        
        for bien in self.bien_list:
            dao_ham = diff(self.parsedFunction, bien)
            dao_ham_val = float(dao_ham.subs(self.values))
            tongSaiSo += abs(dao_ham_val) * self.errors[bien]
        
        ganDung = float(self.parsedFunction.subs(self.values))
        
        print(f"Ket qua: {ganDung} ± {tongSaiSo}")
    