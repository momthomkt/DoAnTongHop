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
# PHẦN THỰC HIỆN BINARIZATION
- Chạy file binary_image.py để Binarization ảnh.
```
python binary_image.py
```
- Mở file ocr_binary_img.py và comment PHẦN 2 để chạy PHẦN 1: THỰC HIỆN CHẠY OCR TRÊN FOLDER Binary_Image.
- Sau đó, comment PHẦN 1 và chạy PHẦN 2: CHẠY FILE correction.py ĐỂ SỬA LỖI
- Để xuất kết quả ra file excel, ta mở file excel.py thay đổi inputdir = "Output_OCR_BinaryImg" và sửa xuất file excel "Output_BinaryImg.xlsx"
- Lưu ý: Trước khi chạy cần tạo folder có tên là Binary_Image, Output_OCR_BinaryImg
