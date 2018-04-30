import warnings
warnings.filterwarnings('ignore')
import numpy as np
from PIL import Image

ep = Image.open("Eprime.png")
print(ep.format, ep.size ,ep.mode)
k1 = Image.open("key1.png")
print(k1.format, k1.size ,k1.mode)
k2 = Image.open("key2.png")
print(k2.format, k2.size ,k2.mode)
im = Image.open("I.png")
print(im.format, im.size ,im.mode)
e = Image.open("E.png")
print(e.format, e.size ,e.mode)

epa = np.asarray(ep).copy()
k1a = np.asarray(k1).copy()
k2a = np.asarray(k2).copy()
ima = np.asarray(im).copy()
ea = np.asarray(e).copy()

i = 400*300

w = np.random.randn(1,3)
print(w)
wt = np.transpose(w)
print(w)

#x = np.array([k1a[0,0],k2a[0,0],ima[0,0]])
#y = np.array([1,2,3])
#xt = x.T

#print(x*y)

epoch = 1
eptest = np.random.randn(300,400)

for epoch in range(0,10):
    for k in range(0, 300):
        for p in range(0, 400):
            x = np.array([k1a[k,p],k2a[k,p],ima[k,p]])
            #print(x.shape)
            #print(w[epoch].shape)
            #print(x)
            xt = np.transpose(x)

            a = np.dot(w,xt)
            etemp = ea[k,p]-a
            w = w + (0.00001*etemp*xt)

w = np.transpose(w)
print(w)

for k in range(0, 300):
    for p in range(0, 400):
        eptest[k,p] = abs((epa[k,p] - w[0]*k1a[k,p] - w[1]*k2a[k,p])/w[2])



etest = Image.fromarray(eptest)
etest.save("test.png")
