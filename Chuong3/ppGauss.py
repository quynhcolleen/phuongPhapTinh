from sympy import nsimplify # pyright: ignore[reportMissingModuleSource]

class PPGauss():
    def __init__(self, mat, soAn):
        self.mat = mat
        self.soPT = len(mat)
        self.soAn = soAn

    # Cho nó đẹp
    def to_subscript(self, num: int | str) -> str:
        sub = {
            '0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄',
            '5': '₅', '6': '₆', '7': '₇', '8': '₈', '9': '₉',
        }
        return ''.join(sub.get(ch, ch) for ch in str(num))

    def maTranBanDau(self):
        print("\nHe phuong trinh ban dau:")
        for i, row in enumerate(self.mat):
            terms = []
            for j in range(self.soAn):
                coef = row[j]
                if coef == 0:
                    continue

                var = f"x{self.to_subscript(j + 1)}"

                if coef == 1:
                    term = var
                elif coef == -1:
                    term = f"-{var}"
                else:
                    term = f"{coef:.0f}{var}"

                terms.append(term)

            rhs = row[-1]
            expr = ' + '.join(terms).replace('+ -', '- ')
            print(f"Hang {i+1}: {expr} = {rhs:.0f}")
        
        print()
              
    def hienThiMaTran(self):  
        col_labels = [f"x{j+1}" for j in range(self.soPT)] + ["= "]
        header = "       | " + "  ".join(f"{label:>9}" for label in col_labels) + " |"
        print(header)
        print("-------+" + "-" * (len(header) - 8) + "+")

        for i, row in enumerate(self.mat):
            # Thank you ChatGPT for this absolute UI hẹ hẹ hẹ
            row_str = f"h{i+1:>2} -> | " + "  ".join(f"{str(nsimplify(val)):>9}" for val in row) + " |"
            print(row_str)
        print()

    def Gauss(self):
        self.maTranBanDau()
        
        # Khử thuận
        for k in range(self.soPT):
            i_max = max(range(k, self.soPT), key=lambda i: abs(self.mat[i][k]))
            if self.mat[i_max][k] == 0:
                print("Ma tran suy bien - khong giai duoc theo PP Gauss.")
                print("He vo nghiem." if self.mat[i_max][self.soPT] else "He vo so nghiem.")
                return

            if i_max != k:
                print(f"h{k+1} <-> h{i_max+1}")
                self.mat[k], self.mat[i_max] = self.mat[i_max], self.mat[k]
                self.hienThiMaTran()

            for i in range(k + 1, self.soPT):
                f = self.mat[i][k] / self.mat[k][k]
                print(f"h{i + 1} -> h{i + 1} - ({nsimplify(f)}) * h{k + 1}")
                for j in range(k, self.soPT + 1):
                    self.mat[i][j] -= f * self.mat[k][j]
                self.mat[i][k] = 0.0
                self.hienThiMaTran()

        # Thế ngược
        x = [0] * self.soPT
        for i in range(self.soPT - 1, -1, -1):
            x[i] = (self.mat[i][self.soPT] - sum(self.mat[i][j] * x[j] for j in range(i + 1, self.soPT))) / self.mat[i][i]

        print("\nKet qua:")
        for idx, xi in enumerate(x, 1):
            print(f"x{idx} = {nsimplify(xi)}")