# 💻 Phương pháp tính

 - Dự án code lại bộ môn **Phương Pháp Tính** của **Đại học Bách Khoa Hà Nội** trên máy tính.
 - Version 0.4.1:
    - Chương 2 - Giải phương trình f(x) = 0:
        - Khoảng cách ly nghiệm.
        - Phương pháp chia đôi.
        - Phương pháp dây cung.
        - Phương pháp tiếp tuyến (Newton).
        - Phương pháp lặp đơn.
        - Input của chương trình: phương trình f(x), khoảng (a, b) và giới hạn sai số epsilon.

    - Chương 3 - Giải phương trình Ax = b:
        - Phương pháp Gauss.
        - Phương pháp Gauss - Jordan.
        - Phương pháp lặp đơn.
        - Phương pháp Jacobi.
        - Input của chương trình: ma trận đầu vào, số lượng ẩn và giới hạn sai số epsilon.

    - Chương 4 - Xấp xỉ hàm số:
        - Nội suy Lagrange.
        - Nội suy Newton (mốc bất kỳ: tiến/lùi).
        - Nội suy Newton (mốc cách đều).
        - Bình phương tối thiểu.
        - Input của chương trình: số lượng mốc nội suy, dãy giá trị xi và yi.
        
    - Chương 5 - Tính gần đúng đạo hàm và tích phân:
        - Tính gần đúng đạo hàm sử dụng công thức điểm.
        - Tính gần đúng tích phân sử dụng công thức hình thang.
        - Tính gần đúng tích phân sử dụng công thức Simpson.

## 📦 Yêu cầu

- Python 3.10.6+
- Thư viện [SymPy](https://www.sympy.org/en/index.html)
- Thư viện [Tabulate](https://pypi.org/project/tabulate/)
- Thư viện [Scipy](https://scipy.org/)

## 🛠 Cài đặt

1. Clone hoặc tải project về máy.
2. Cài thư viện `sympy`, `tabulate` & `scipy` nếu chưa có:

```bash
pip install sympy
pip install tabulate
pip install scipy
```
3. Chạy `main.py`.