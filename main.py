from models.KCLN import *
from models.ppChiaDoi import *
from models.ppDayCung import *

hamSo = input("Nhap ham so f(x): ")
left, right = map(float, input("Nhap khoang (a, b): ").split())
epsilon = float(input("Nhap gioi han sai so (epsilon): "))

option = input("\nChon phuong phap tinh: \n1. Phuong phap lap doi\n2. Phuong phap day cung\n\nLua chon: ")

f = KiemTraKCLN(hamSo, left, right)

if not f.kcln():
    print("Khoang cach ly nghiem khong hop le.")

if option == "1":
    print("\nThuc hien phuong phap chia doi:\n")
    chia_doi = PPChiaDoi(hamSo, left, right, epsilon)
    chia_doi.chiaDoi()
    
elif option == "2":
    print("\nThuc hien phuong phap day cung:\n")
    day_cung = PPDayCung(hamSo, left, right, epsilon)
    if day_cung.dieuKienLap():
        day_cung.dayCung()
    else:
        print("Khong thoa man dieu kien thuc hien phuong phap day cung")
else:
    print("Khong hop le")