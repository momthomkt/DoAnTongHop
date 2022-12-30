# DoAnTongHop
Thực hiện Text Detection và Extraction trên dữ liệu là hình ảnh của từ điển Tiếng Bana.
Công cụ sử dụng:

- Python
- Tesseract
- OpenCV
- Cùng một số thư viện của Python khác...
## Sử dụng
Đầu tiên chạy:
```
python ocrusing2.py
```
- Chạy file ocrusing2.py để xử lý ảnh:
    + Ảnh sẽ được đọc từ file TU DIEN VIET-BAHNAR.pdf và kết quả được lưu trong folder TU DIEN VIET-BAHNAR
    + Ảnh sẽ tiếp tục được cắt và kết quả được lưu trong folder Split Image
    + Các ký tự trong ảnh sẽ được đọc và lưu kết quả dưới dạng file txt trong folder TU DIEN VIET-BAHNAR_converted
- Lưu ý: Trước khi chạy cần tạo các folder có tên là TU DIEN VIET-BAHNAR, Split Image, TU DIEN VIET-BAHNAR_converted
