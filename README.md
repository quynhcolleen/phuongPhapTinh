# 💻 Phương pháp tính

 - Dự án code lại bộ môn **Phương Pháp Tính** của **Đại học Bách Khoa Hà Nội** trên máy tính.
 - Version 0.4.1:
    - Chương 1 - Sai số:
        - Sai số tương đối.
        - Sai số trong tính toán

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
        - Tính gần đúng đạo hàm sử dụng công thức điểm. (input: dãy giá trị xi, yi)
        - Tính gần đúng tích phân sử dụng công thức hình thang.
        - Tính gần đúng tích phân sử dụng công thức Simpson.
        - Input của chương trình: hàm số, mốc tích phân, số đoạn chia.

## 📦 Yêu cầu

### Cách 1:
- Python 3.12
- Thư viện [SymPy](https://www.sympy.org/en/index.html)
- Thư viện [Tabulate](https://pypi.org/project/tabulate/)
- Thư viện [Scipy](https://scipy.org/)

### Cách 2&3:
- Docker 28.3.1-1
- Docker compose

## 🛠 Cài đặt

### Cách 1:

1. Clone hoặc tải project về máy.
2. Cài thư viện `sympy`, `tabulate` & `scipy` nếu chưa có:

```bash
pip install -r requirements.txt
```
3. Chạy `main.py`.

### Cách 2:

```bash
docker compose -f docker-compose-dev.yml
```

### Cách 3 (Dùng win đơ):

1. 
```bash
docker compose -f docker-compose-dev.yml up -d
```
2. 
```bash 
docker exec -it ppt-docker-dev python -u main.py
```  