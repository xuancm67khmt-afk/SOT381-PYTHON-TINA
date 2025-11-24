thu_nhap = int(input("Thu nhập hàng tháng (VND): "))
diem_tin_dung = int(input("Điểm tín dụng (300 - 850): "))
so_tien_vay = int(input("Số tiền muốn vay: "))

if diem_tin_dung < 580:
    ket_qua = "Từ chối"
elif diem_tin_dung >= 580 and thu_nhap > 20000000:
    ket_qua = "Duyệt"
elif diem_tin_dung >= 580 and thu_nhap < 20000000:
    ket_qua = "Cần xem xét thêm"
else:
    ket_qua = "Không xác định"

print("Kết quả xét duyệt:", ket_qua)
