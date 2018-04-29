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

epa = np.asarray(ep).copy()
k1a = np.asarray(k1).copy()
k2a = np.asarray(k2).copy()


eptest = epa-k1a-k2a

print(eptest)

etest = Image.fromarray(eptest)
etest.save("test.png")
