# 将原始图像下采样4倍作为测试集
import enum
import cv2
import numpy
import os


SCALE = 4
filepath = 'BSDS300/images/test'
filelist = os.listdir(filepath)
outpath = 'test/'
for i,filename in enumerate(filelist):
    img_name = os.path.join(filepath+'/'+filename)
    img = cv2.imread(img_name)
    
    size_x,size_y = img.shape[0], img.shape[1]
    size = (size_y//SCALE, size_x//SCALE)
    img_out = cv2.resize(img, size, interpolation=cv2.INTER_CUBIC)
    
    out_name = os.path.join(outpath+filename)
    cv2.imwrite(out_name, img_out)
