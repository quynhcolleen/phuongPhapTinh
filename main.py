from Chuong2.KCLN import *
from Chuong2.ppChiaDoi import *
from Chuong2.ppDayCung import *
from Chuong2.ppNewton import *
from Chuong2.ppLapDon import *
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

hamSo = input("Nhap ham so f(x): ")
left, right = map(float, input("Nhap khoang (a, b): ").split())
epsilon = float(input("Nhap gioi han sai so (epsilon): "))

# Unicode của epsilon
epsilon_txt = '\u03B5'
hamso_txt = simplify(hamSo)

clear_screen()

def info():
    print(f"f(x) = {hamso_txt}, KCLN ({left},{right}), {epsilon_txt} = {epsilon}")
    
print("\nChọn phương pháp tính:")
print("1. Phuong phap chia doi")
print("2. Phuong phap day cung")
print("3. Phuong phap tiep tuyen (Newton")
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