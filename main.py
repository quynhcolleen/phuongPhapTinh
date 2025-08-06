from Chuong2.KCLN import *
from Chuong2.ppChiaDoi import *
from Chuong2.ppDayCung import *
from Chuong2.ppNewton import *
from Chuong2.ppLapDon import *
from Chuong3.ppGauss import *
from Chuong3.ppGaussJordan import *
from Chuong3.ppLapDon import *
from Chuong3.ppJacobi import *
import os

epsilon_txt = '\u03B5'
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    
clear_screen()
print("Dai hoc Bach khoa Ha Noi")
print("MI2010 - Phuong phap tinh\n")
print("1. Chuong 2: Tinh gan dung f(x) = 0")
print("2. Chuong 3: Tinh gan dung Ax = b")
print()
luaChon = int(input("Lua chon: "))

match luaChon:
    case 1:
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
            
        print("\nChọn phương pháp tính:")
        print("1. Phuong phap chia doi")
        print("2. Phuong phap day cung")
        print("3. Phuong phap tiep tuyen (Newton)")
        print("4. Phuong phap lap don\n")
        option = input("Lua chon: ")

        f = KiemTraKCLN(hamSo, left, right)

        if not f.kcln():
            print("Khoang cach ly nghiem khong hop le.")

        if option == "1":
            clear_screen()
            info()
            print("Thuc hien phuong phap chia doi:\n")
            chia_doi = PPChiaDoi(hamSo, left, right, epsilon)
            chia_doi.chiaDoi()
            
        elif option == "2":
            clear_screen()
            info()
            print("Thuc hien phuong phap day cung:\n")
            day_cung = PPDayCung(hamSo, left, right, epsilon)
            if day_cung.dieuKienLap():
                day_cung.dayCung()
            else:
                print("Khong thoa man dieu kien thuc hien phuong phap day cung")
                
        elif option == "3":
            clear_screen()
            info()
            print("Thuc hien phuong phap tiep tuyen (Newton):\n")
            newton = PPNewton(hamSo, left, right, epsilon)
            if newton.dieuKienLap():
                newton.Newton()
            else:
                print("Khong thoa man dieu kien thuc hien phuong phap tiep tuyen (Newton)")
                
        elif option == "4":
            clear_screen()
            info()
            print("Thuc hien phuong phap lap don:")
            lap_don = PPLapDon(hamSo, left, right, epsilon)
            lap_don.LapDon()
        else:
            print("Khong hop le")
            
    case 2:
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
            
    case _:
        print("Khong hop le.")
        exit()
            