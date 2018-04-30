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
w1 = w2 = w3 = 0.1

w = np.random.randn(10,3)

#x = np.array([k1a[0,0],k2a[0,0],ima[0,0]])
#y = np.array([1,2,3])
#xt = x.T

#print(x*y)

epoch = 1
eptest = np.random.randn(300,400)

for epoch in range(0,5):
    for k in range(0, 300):
        for p in range(0, 400):
            x = np.array([k1a[k,p],k2a[k,p],ima[k,p]]).T
            #print(x.shape)
            #print(w[epoch].shape)
            a = np.dot(w[epoch].T,x)
            etemp = ea[k,p]-a
            w[epoch+1] = w[epoch]+(0.00001*etemp*x)


print(w[5])

for k in range(0, 300):
    for p in range(0, 400):
        eptest[k,p] = (epa[k,p] - w[5,0]*k1a[k,p] - w[5,1]*k2a[k,p])/w[5,2]



etest = Image.fromarray(eptest)
etest.save("test.png")
