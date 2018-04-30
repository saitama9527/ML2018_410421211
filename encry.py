import warnings
warnings.filterwarnings('ignore')
import numpy as np
from PIL import Image

ep = Image.open("Eprime.png")
print("\nloading images...\n")
print("load Eprime.png--")
print(ep.format, ep.size ,ep.mode)
k1 = Image.open("key1.png")
print("\nload key1.png--")
print(k1.format, k1.size ,k1.mode)
k2 = Image.open("key2.png")
print("\nload key2.png--")
print(k2.format, k2.size ,k2.mode)
im = Image.open("I.png")
print("\nload I.png--")
print(im.format, im.size ,im.mode)
e = Image.open("E.png")
print("\nload E.png--")
print(e.format, e.size ,e.mode)
print("\nstart decryption...")

epa = np.asarray(ep).copy()
k1a = np.asarray(k1).copy()
k2a = np.asarray(k2).copy()
ima = np.asarray(im).copy()
ea = np.asarray(e).copy()

i = 400*300

w = np.array([1,1,1])
wt = np.transpose(w)


epoch = 1
eptest = np.random.randn(300,400)

for epoch in range(10):
    for k in range(300):
        for p in range(400):
            x = np.array([k1a[k,p],k2a[k,p],ima[k,p]])
            xt = np.transpose(x)

            a = np.dot(w,xt)
            etemp = ea[k,p]-a
            w = w + (0.00001*etemp*xt)
w = np.transpose(w)

for k in range(300):
    for p in range(400):
        eptest[k,p] = (epa[k,p] - w[0]*k1a[k,p] - w[1]*k2a[k,p])/w[2]
        if eptest[k,p] >255:
            eptest[k,p] = 255
        elif eptest[k,p] <0:
            eptest[k,p] = 0


eptest = np.array(eptest,dtype=np.uint8)
etest = Image.fromarray(eptest)
etest.save("Iprime.png")

print("\nComplete! Decrypted image save as 'Iprime'\n")
