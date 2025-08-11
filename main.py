from Chuong1 import *
from Chuong2 import *
from Chuong3 import *
from Chuong4 import *
from Chuong5 import *
import os

epsilon_txt = '\u03B5'
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    
clear_screen()
print("Dai hoc Bach khoa Ha Noi")
print("MI2010 - Phuong phap tinh\n")
print("1. Chuong 1: Sai so")
print("2. Chuong 2: Tinh gan dung f(x) = 0")
print("3. Chuong 3: Tinh gan dung Ax = b")
print("4 Chuong 4: Xap xi ham so")
print("5. Chuong 5: Tinh gan dung dao ham va tich phan")
print()
luaChon = int(input("Lua chon: "))

def mocCachDeu(xi) -> bool:
    khoang = xi[1] - xi[0]
    for i in range(2, len(xi)):
        if khoang != (xi[i] - xi[i - 1]):
            return False
    return True
    
match luaChon:
    case 1:
        clear_screen()
        print("Chuong 1: Sai so\n")
        print("Lua chon chuong trinh ban muon thuc hien:")
        print("1. Sai so tuong doi:")
        print("2. Sai so trong tinh toan (ham 1 hoac nhieu bien):\n")
        option = int(input("Lua chon: "))
        
        if option == 1:
            clear_screen()
            ganDung = float(input("Nhap so gan dung a:"))
            tuyetDoi = float(input("Nhap sai so tuyet doi ∆a:"))
            print()
            tdoi = saiSoTuongDoi(ganDung, tuyetDoi)
            tdoi.TuongDoi()
            
        elif option == 2:
            print()
            hamSo = input("Nhap ham so: ")
            clear_screen()
            print(hamSo)
            print()
            gan_dung = SaiSoChuong1(hamSo)
            gan_dung.uocLuong()
            
    case 2:
        clear_screen()
        print("Chuong 2: Tinh gan dung f(x) = 0\n")
        hamSo = input("Nhap ham so f(x): ")
        left, right = map(float, input("Nhap khoang (a, b): ").split())
        epsilon = float(input("Nhap gioi han sai so (epsilon): "))

        # Unicode của epsilon
        hamso_txt = simplify(hamSo)

        clear_screen()

        def info():
            print(f"f(x) = {hamso_txt}, KCLN ({left},{right}), {epsilon_txt} = {epsilon}")
            
        print("\nChon phuong phap tinh:")
        print("1. Phuong phap chia doi")
        print("2. Phuong phap day cung")
        print("3. Phuong phap tiep tuyen (Newton)")
        print("4. Phuong phap lap don\n")
        option = int(input("Lua chon: "))

        f = KiemTraKCLN(hamSo, left, right)

        if not f.kcln():
            print("Khoang cach ly nghiem khong hop le.")

        if option == 1:
            clear_screen()
            info()
            print("Thuc hien phuong phap chia doi:\n")
            chia_doi = PPChiaDoi(hamSo, left, right, epsilon)
            chia_doi.chiaDoi()
            
        elif option == 2:
            clear_screen()
            info()
            print("Thuc hien phuong phap day cung:\n")
            day_cung = PPDayCung(hamSo, left, right, epsilon)
            if day_cung.dieuKienLap():
                day_cung.dayCung()
            else:
                print("Khong thoa man dieu kien thuc hien phuong phap day cung")
                
        elif option == 3:
            clear_screen()
            info()
            print("Thuc hien phuong phap tiep tuyen (Newton):\n")
            newton = PPNewton(hamSo, left, right, epsilon)
            if newton.dieuKienLap():
                newton.Newton()
            else:
                print("Khong thoa man dieu kien thuc hien phuong phap tiep tuyen (Newton)")
                
        elif option == 4:
            clear_screen()
            info()
            print("Thuc hien phuong phap lap don:")
            lap_don = PPLapDon(hamSo, left, right, epsilon)
            lap_don.LapDon()
        else:
            print("Khong hop le")
            
    case 3:
        clear_screen()
        print("Chuong 3: Tinh gan dung Ax = b\n")
        n = int(input("Nhap so luong an: "))
        print("Nhap cac he so tuong ung tren hang (cach nhau bang dau cach):")
        matrix = []
        for i in range(n):
            row = list(map(float, input(f"Hang {i+1}: ").split()))
            if len(row) > (n + 1):
                print("Ban da nhieu hon cho phep.")
                exit()
            elif len(row) < (n + 1):
                print ("Ban da nhap thieu he so.")
                exit()
            matrix.append(row)
            
        print("\nChon phuong phap tinh:")
        print("1. Phuong phap Gauss")
        print("2. Phuong phap Gauss - Jordan")
        print("3. Phuong phap lap don")
        print("4. Phuong phap Jacobi")
        print()
        subChoice = int(input("Lua chon: "))
        
        if subChoice == 1:
            clear_screen()
            print("Thuc hien phuong phap Gauss:")
            gauss = PPGauss(matrix, n)
            gauss.Gauss()
        
        elif subChoice == 2:
            clear_screen()
            print("Thuc hien phuong phap Gauss:")
            gauss_jordan = PPGaussJordan(matrix, n)
            gauss_jordan.GaussJordan()
            
        elif subChoice == 3:
            clear_screen()
            saiSo = input(f"Nhap sai so {epsilon_txt}: ")
            print("Thuc hien phuong phap lap don:")
            lap_don = PPLapDonC3(matrix, n, saiSo)
            lap_don.LapDonC3()
            
        elif subChoice == 4:
            clear_screen()
            saiSo = input(f"Nhap sai so {epsilon_txt}: ")
            print("Thuc hien phuong phap Jacobi:")
            jacobi = PPJacobi(matrix, n, saiSo)
            jacobi.Jacobi()
    case 4:
        clear_screen()    
        print("Chuong 4: Xap xi ham so")      
        print()
        i = int(input("Nhap so diem noi suy: "))
        print()
        xi_input = input(f"Nhap {i} gia tri x (cach nhau bang dau cach): ")
        xi = list(map(float, xi_input.strip().split()))
        
        yi_input = input(f"Nhap {i} gia tri y (cach nhau bang dau cach): ")
        yi = list(map(float, yi_input.strip().split()))

        if len(xi) != i or len(yi) != i:
            print("So luong gia tri khong khop!")
            
        print("\nChon phuong phap noi suy:")
        print("1. Phuong phap noi suy Lagrange.")
        print("2. Phuong phap noi suy Newton.")
        print("3. Phuong phap binh phuong toi thieu.")
        print()
        subChoice = int(input("Lua chon: "))
        
        
        if subChoice == 1:   
            clear_screen()
            print("Thuc hien phuong phap noi suy Lagrange:\n")
            lagrange = PPLagrange(i, xi, yi)
            lagrange.Lagrange()
            
        elif subChoice == 2:   
            clear_screen()
            if not mocCachDeu(xi): 
                print("Thuc hien phuong phap noi suy Newton moc bat ky:\n")  
                newton = NoiSuyNewton(i, xi, yi)
                newton.NewtonBatKy()
            else:
                print("Phat hien moc cach deu. Chon phuong phap noi suy:\n")
                print("1. Noi suy Newton moc bat ky.")
                print("2. Noi suy Newton moc cach deu.")
                subSub = int(input("Lua chon: "))
                if subSub == 1:
                    clear_screen()
                    print("Thuc hien phuong phap noi suy Newton moc bat ky:\n")  
                    newton = NoiSuyNewton(i, xi, yi)
                    newton.NewtonBatKy()
                elif subSub == 2:
                    clear_screen()
                    print("Thuc hien phuong phap noi suy Newton moc cach deu:\n")  
                    newton = NoiSuyNewton(i, xi, yi)
                    newton.NewtonCachDeu()
                else:
                    print("Khong hop le.")

        elif subChoice == 3:
            clear_screen()
            print("Thuc hien phuong phap binh phuong toi thieu:\n")
            bptt = BinhPhuongToiThieu(xi, yi)
            bptt.BPTT()
                        
        else:
            print("Khong hop le.")
    case 5:
        clear_screen()
        print("\nChuong 5: Tinh gan dung dao ham va tich phan")
        print("1. Tinh gan dung dao ham su dung cong thuc can")
        print("2. Tich phan theo cong thuc hinh thang")
        print("3. Tich phan theo cong thuc Simpson")
        subChoice = int(input("Lua chon: "))
        
        if subChoice == 1:
            n = int(input("Nhap so diem: "))
            xi = list(map(float, input("Nhap xi: ").split()))
            yi = list(map(float, input("Nhap yi: ").split()))
            
            if len(xi) != n or len(yi) != n:
                print("So luong gia tri khong khop.")
                exit()
            clear_screen()
            print("Thuc hien tinh toan gan dung dao ham:\n")
            gan_dung = tinhGanDung(xi, yi) 
            gan_dung.congThucDiem()

        elif subChoice == 2:
            hamSo = input("Nhap ham so f(x): ")
            a, b = map(float, input("Nhap khoang tich phan (a b) (cach nhau bang dau cach): ").split())
            n = int(input("Nhap so doan chia: "))
            clear_screen()
            print(f"f(x) = {hamSo}, (a, b) = ({a}, {b}), n = {n}")
            print("Thuc hien tinh toan theo cong thuc hinh thang:\n")  
            ht = HinhThang(hamSo, b, a, n)
            ht.hinhThang()
            
        elif subChoice == 3:
            hamSo = input("Nhap ham so f(x): ")
            a, b = map(float, input("Nhap khoang tich phan (a b) (cach nhau bang dau cach): ").split())
            n = int(input("Nhap so doan chia (n, phai la so chan): "))
            clear_screen()
            print(f"f(x) = {hamSo}, (a, b) = ({a}, {b}), n = {n}")
            print("Thuc hien tinh toan theo cong thuc Simpson:\n")  
            sp = Simpson(hamSo, a, b, n)
            sp.simpson()
                    
        else:
            print("Khong hop le.")

    case _:
        print("Khong hop le.")
        exit()