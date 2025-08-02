from models.KCLN import *
from models.ppChiaDoi import *

hamSo = input("Nhap ham so f(x): ")
left, right = map(float, input("Nhap khoang (a, b): ").split())
epsilon = float(input("Nhap gioi han sai so (epsilon): "))

f = KiemTraKCLN(hamSo, left, right)
if f.kcln():
    ChiaDoi = PPChiaDoi(hamSo, left, right, epsilon)
    ChiaDoi.chiaDoi()
else:
    print("Khong du dieu kien de thuc hien phuong phap chia doi.")

