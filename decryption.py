import warnings
warnings.filterwarnings('ignore')
import numpy as np
from PIL import Image

ep = Image.open("Eprime.png")
print("\nloading images...\n")
print("load Eprime.png--",ep.format, ep.size ,ep.mode)
k1 = Image.open("key1.png")
print("\nload key1.png--",k1.format, k1.size ,k1.mode)
k2 = Image.open("key2.png")
print("\nload key2.png--",k2.format, k2.size ,k2.mode)
im = Image.open("I.png")
print("\nload I.png--",im.format, im.size ,im.mode)
e = Image.open("E.png")
print("\nload E.png--",e.format, e.size ,e.mode)
print("\nstart decryption...\n")            #讀取照片並印出格式

epa = np.asarray(ep).copy()
k1a = np.asarray(k1).copy()
k2a = np.asarray(k2).copy()
ima = np.asarray(im).copy()
ea = np.asarray(e).copy()                   #將照片轉成二維矩陣

w = np.array([1,1,1])                       #初始化weight
wt = np.transpose(w)                        #設定weight的轉移矩陣


epoch = 1
eptest = np.random.randn(300,400)           #宣告新矩陣 大小為將要輸出的圖片

for epoch in range(10):                     #在10個epoch內，逐一檢視每個像素
    for k in range(300):
        for p in range(400):
            x = np.array([k1a[k,p],k2a[k,p],ima[k,p]])
            xt = np.transpose(x)
            a = np.dot(w,xt)
            etemp = ea[k,p]-a
            w = w + (0.00001*etemp*xt)
            w = np.transpose(w)             #執行梯度下降計算，取得weight1~3

for k in range(300):                        #對於Eprime中的像素，用公式進行反推得到新的矩陣
    for p in range(400):
        eptest[k,p] = (epa[k,p] - w[0]*k1a[k,p] - w[1]*k2a[k,p])/w[2]
        if eptest[k,p] >255:
            eptest[k,p] = 255               #控制在0~255
        elif eptest[k,p] <0:
            eptest[k,p] = 0


eptest = np.array(eptest,dtype=np.uint8)    #浮點數轉為整數
etest = Image.fromarray(eptest)             #將矩陣轉為圖檔
etest.save("Iprime.png")

print("w = ",w)

print("\nComplete! Decrypted image save as 'Iprime'\n")
