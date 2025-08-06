from sympy import nsimplify, Matrix, symbols, linsolve, evalf, N # pyright: ignore[reportMissingModuleSource]
import copy

class PPJacobi:
    def __init__(self, mat, soAn, gioiHanSaiSo):
        self.mat = mat
        self.soPT = len(mat)
        self.soAn = soAn
        self.gioiHanSaiSo = float(gioiHanSaiSo)
    
    def chuanHang(self, Bx) -> float:
        chuanHang_list = [sum(abs(Bx[i][j]) for j in range(len(Bx[0]))) for i in range(len(Bx))]
        return max(chuanHang_list)

    def chuanCot(self, Bx) -> float:
        chuanCot_list = [sum(abs(Bx[i][j]) for i in range(len(Bx))) for j in range(len(Bx[0]))]
        return max(chuanCot_list)
        
    def troiHang(self, Bx) -> bool:
        for i in range(len(Bx)):
            diag = abs(Bx[i][i])
            sum_row = sum(abs(Bx[i][j]) for j in range(len(Bx)) if j != i)
            if diag <= sum_row:
                return False
        return True
        
    def troiCot(self, Bx) -> bool:
        n = len(Bx)
        for j in range(n):
            diag = abs(Bx[j][j])
            sum_col = sum(abs(Bx[i][j]) for i in range(n) if i != j)
            if diag <= sum_col:
                return False
        return True
        
    def Jacobi(self):
        Ax = [row[:self.soAn] for row in self.mat]
        b = [row[self.soAn] for row in self.mat]

        # Biến thành Bx + d
        Bx_temp = copy.deepcopy(Ax) 
        d_temp = [0] * self.soAn

        for i in range(self.soAn):
            diag = Ax[i][i]
            d_temp[i] = nsimplify(b[i] / diag)

            for j in range(self.soAn):
                if i == j:
                    Bx_temp[i][j] = 0
                else:
                    Bx_temp[i][j] = nsimplify(-Ax[i][j] / diag)   
        
        if self.troiHang(Ax):
            print("A la ma tran cheo troi hang")
            q_list = [sum(abs(Ax[i][j]) / abs(Ax[i][i]) for j in range(self.soAn) if j != i) for i in range(self.soAn)]
            q = max(q_list)
            _lambda = 1
            chuan = self.chuanHang
            
        elif self.troiCot(Ax):
            q_list = [sum(abs(Ax[i][j]) / abs(Ax[j][j]) for i in range(self.soAn) if i != j) for j in range(self.soAn)]
            q = max(q_list)
            diag_list = []
            for i in range(self.soAn):
                diag = Ax[i][i]
                diag_list.append(diag)
            _lambda = max(diag_list) / min(diag_list)    
            chuan = self.chuanCot
        else:
            print("Ma tran khong chéo troi hang hoac cot. Khong dam bao hoi tu Jacobi.")
            return None
        
        print("He phuong trinh da dua ve dang x = Bx + d\n")

        col_labels = [f"x{j+1}" for j in range(self.soAn)] + ["d"]
        header = "       | " + "  ".join(f"{label:>9}" for label in col_labels) + " |"
        print(header)
        print("-------+" + "-" * (len(header) - 8) + "+")

        for i in range(self.soAn):
            row = [Bx_temp[i][j] for j in range(self.soAn)] + [d_temp[i]]
            row_str = f"h{i+1:>2} -> | " + "  ".join(f"{str(nsimplify(val)):>9}" for val in row) + " |"
            print(row_str)
        print()
        
        Bx = Matrix(Bx_temp)
        d = Matrix(d_temp)
        
         # Tính nghiệm ĐÚNG
        x_symbols = symbols(f"x1:{self.soAn+1}")
        matrixNghiem = Matrix(self.mat)
        A = matrixNghiem[:, :-1]
        b = matrixNghiem[:, -1]
        nghiem = linsolve((A, b), x_symbols)
        list_nghiem = list(nghiem)[0]
        list_nghiem = [i.evalf(1) for i in list_nghiem]
        
        print("\nLua chon cach chon x0 (diem bat dau):")
        print("1. Chuong trinh tu chon.")
        print("2. Nguoi dung tu nhap\n")
        luaChon = int(input("Lua chon: "))
        
        if luaChon == 1:
            print(f"\nx0 = {list_nghiem}")
            x_curr = Matrix(list_nghiem).reshape(self.soAn, 1)
        elif luaChon == 2:
            x_curr_input = input("Nhap x0 (cach nhau bang dau cach): ")
            vector = list(map(float, x_curr_input.strip().split()))
            assert len(vector) == self.soAn, f"Ban phai nhap dung {self.soAn} phan tu."
            x_curr = Matrix(vector).reshape(self.soAn, 1)
        else:
            print("Lua chon khong hop le.")
            return
                
        count = 1
        x_list = []
        while True:
            x_next = Bx * x_curr + d
            x_list.append(x_next)
            print(f"x{count} = [" + ", ".join(f"{val.evalf():.7f}" for val in x_next) + "]")
            err = float(((q**count) * _lambda /(1 - q)) * chuan((x_next - x_curr).reshape(self.soAn, 1).tolist()))
            if err < self.gioiHanSaiSo:
                break
            count += 1
            x_curr = x_next
            
        saiSo = float(((q * _lambda)/(1 - q)) * chuan((x_next - x_curr).reshape(self.soAn, 1).tolist()))
        ket_qua = ", ".join(f"{val.evalf():.7f}" for val in x_next)
        print(f"Ket qua: x = [{ket_qua}] ± {N(saiSo):.7f}")

