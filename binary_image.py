import os
import cv2
from tqdm import tqdm

inputDir = './Split Image'
resultDir = 'Binary_Image'
arr = os.listdir(inputDir)  # list image


# Function gray scale:
def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


for i in tqdm(range(len(arr))):
    file = arr[i]
    im_gray = cv2.imread(inputDir + '/' + file, cv2.IMREAD_GRAYSCALE)
    # Binarisation
    thresh, im_bw = cv2.threshold(im_gray, 125, 255, cv2.THRESH_BINARY)
    cv2.imwrite(os.path.join(resultDir, file), im_bw)

