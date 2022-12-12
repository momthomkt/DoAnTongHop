# -*- coding: utf-8 -*-
# """OCRusingTesseract.ipynb

# Automatically generated by Colaboratory.

# Original file is located at
#     https://colab.research.google.com/drive/19ekYcMQ_To3hISrp_fX76fOvdmkzfNdT
# """

# !sudo apt install tesseract-ocr-all libpoppler-dev poppler-utils

# !pip install pytesseract pdf2image --no-deps

# !git clone https://github.com/tesseract-ocr/tessdata
# %env TESSDATA_PREFIX=/content/tessdata

# from google.colab import drive
# drive.mount('/content/drive')

import pytesseract
import shutil
import os
import random
import cv2
import numpy as np
try:
    from PIL import Image
except ImportError:
    import Image

fname = "TU DIEN VIET-BAHNAR.pdf"
# fname = "qsb_2021_de_an.pdf" # File PDF cần chạy OCR
# !cp "/content/drive/MyDrive/Assistant/Documents/Báo cáo KC Bana - Technical/tài liệu cần in/Từ điển Bana - Pháp/dictionnairebah00dourgoog.pdf" ./$fname

# import module
from pdf2image import convert_from_path
from tqdm import tqdm
import tempfile

dname = fname[:-4]
# !rm -rf $dname
# !mkdir $dname

# shutil.rmtree(dname)
# os.mkdir(dname)

# # Store Pdf with convert_from_path function
# with tempfile.TemporaryDirectory() as path:
#     images = convert_from_path(fname, output_folder=path)
 
#     for i in tqdm(range(len(images))):
#           # Save pages as images in the pdf
#         images[i].save(dname + "/page_%03d.jpg"%i, 'JPEG')

##--------------------------------------------------------------------------------

# def find_max(lst):
#     max_col = lst[0]
#     index_max = 0
#     for i in range(len(lst)):
#         if lst[i] >= max_col:
#             max_col = lst[i]
#             index_max = i
#     return index_max

# # Ham giai he 2 phuong trinh bac 1
# def solver_SOE(x1,y1,x2,y2):
#     if x1 == x2:
#         return [1,x1,0]
#     else:
#         a = (y1 - y2)/(x1 - x2)
#         b = (x1 * y2 - x2 * y1)/(x1 - x2)
#         return [a,b]

# # Ham tim hoanh do x(toa do theo phuong ngang) duong ke trang
# def find_Index(vungchon):
#     height = vungchon.shape[0]
#     width = vungchon.shape[1]
#     lst = []
#     for i in range(width):
#         lst.append(0)


#     for i in range(height):
#         for j in range(width):
#             if (vungchon[i][j] == np.array([255,255,255])).all():
#                 lst[j] += 1

#     index = find_max(lst)
#     print(index)
#     return index

# def split_image(input_dir, output_dir):
#     img = cv2.imread(input_dir)

#     y11, y12 = 300, 500
#     x11, x12 = 393, 867

#     y21, y22 = 1090, 1290
#     x21, x22 = 393, 867

#     vungchon1 = img[y11:y12, x11:x12]
#     index1 = find_Index(vungchon1)

#     vungchon2 = img[y21:y22, x21:x22]
#     index2 = find_Index(vungchon2)

#     result = solver_SOE(index1 + x11,y11, index2 + x21, y22)

#     img1 = img.copy()
#     if len(result) == 3:
#         for i in range(img1.shape[0]):
#             for j in range(img1.shape[1]):
#                 if j > result[1]:
#                     img1[i][j] = np.array([255,255,255])
#     elif len(result) == 2:
#         for i in range(img1.shape[0]):
#             for j in range(img1.shape[1]):
#                 if j > ((i - result[1])/result[0]):
#                     img1[i][j] = np.array([255,255,255])
#     output_dir1 = output_dir + "/" + input_dir[input_dir.rfind('/') + 1:-4] + '_1.jpg'
#     cv2.imwrite(output_dir1,img1)

#     img2 = img.copy()
#     if len(result) == 3:
#         for i in range(img2.shape[0]):
#             for j in range(img2.shape[1]):
#                 if j <= result[1]:
#                     img2[i][j] = np.array([255,255,255])
#     elif len(result) == 2:
#         for i in range(img2.shape[0]):
#             for j in range(img2.shape[1]):
#                 if j <= ((i - result[1])/result[0]):
#                     img2[i][j] = np.array([255,255,255])
#     output_dir2 = output_dir + "/" + input_dir[input_dir.rfind('/') + 1:-4] + '_2.jpg'
#     cv2.imwrite(output_dir2,img2)

# list_pages0 = sorted(os.listdir(dname))
# print(list_pages0)
# # split_dir = dname + "_split"
split_dir = "Split Image"

# shutil.rmtree(split_dir)
# os.mkdir(split_dir)

# for pfile in tqdm(list_pages0):
#     split_image(dname + "/" + pfile, split_dir)

#-------------------------------------------------------------------------

list_pages = sorted(os.listdir(split_dir))
convert_dir = dname + "_converted"
# !rm -rf $convert_dir
# !mkdir $convert_dir
shutil.rmtree(convert_dir)
os.mkdir(convert_dir)

# custom_oem_psm_config = r'-l vie --oem 3 --psm 6 --nice 2'
# custom_oem_psm_config = r'-l vie --oem 1 --psm 4 --nice 2'
# custom_oem_psm_config = '-l vie --oem 3 --psm 6'
custom_oem_psm_config = '-l vie --oem 1 --psm 4'

for pfile in tqdm(list_pages):
  extractedInformation = pytesseract.image_to_string(Image.open(os.path.join(split_dir, pfile)), config=custom_oem_psm_config)
#   extractedInformation = pytesseract.image_to_string(Image.open(os.path.join(dname, pfile)), config=custom_oem_psm_config)
  with open(os.path.join(convert_dir, pfile.replace('jpg', 'txt')), "w", encoding="utf-8") as f:
    f.write(extractedInformation)