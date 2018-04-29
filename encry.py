import warnings
warnings.filterwarnings('ignore')
import numpy as np
from PIL import Image

im = Image.open("I.png")
print(im.format, im.size ,im.mode)
