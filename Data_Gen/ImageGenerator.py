import cv2
import numpy as np
import random
import matplotlib.pyplot as plt
import os
from skimage import io
from skimage.transform import rotate, AffineTransform, warp, resize
from skimage.util import random_noise
from datetime import datetime
from PIL import Image

from datetime import datetime

img_base_list = ["Do_Not_Enter.png", "No_Left_Turn_Symbol.jpg", "No_Right_Turn.png", "No_U_Turn.png", "Stop_Sign.png"]
img_base_prefix = "C:\\Users\\1995h\\PycharmProjects\\senior_project\\Data_Gen\\"

img_base = "C:\\Users\\1995h\\PycharmProjects\\senior_project\\Data_Gen\\base.PNG"
img_path = "C:\\Users\\1995h\\PycharmProjects\\senior_project\\Data_Gen\\No_Left_Turn_Symbol.jpg"

img = cv2.imread(img_path)
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

img_base = cv2.imread(img_base)
img_base = cv2.cvtColor(img_base, cv2.COLOR_RGB2BGR)

plt.imshow(img_base)
plt.show()


def rotation(image, angle):
    return rotate(image, angle)


def add_noise(image):
    random.seed(datetime.now())
    seed = random.randint(0, 12000)
    return random_noise(image, seed=seed)


def blur_image(image):
    return cv2.GaussianBlur(image, (9, 9), 0)


def paste_image(base, sign):
    base = base.copy()
    sign = rotation(sign.copy(), 10)
    back_sign = sign.copy()
    length = base.shape[0]
    width = base.shape[1]
    ratio = 1/20
    # sign.resize(round(length * ratio), round(width * ratio), 3)
    sign = Image.fromarray((sign * 255).astype(np.uint8))
    sign.thumbnail((40, 40))
    base = Image.fromarray(base)
    # new_sign = Image.fromarray(sign)
    base.paste(sign, (350, 200))
    base.save("C:\\Users\\1995h\\PycharmProjects\\senior_project\\Data_Gen\\sign_gen_sample2.PNG", "PNG")


paste_image(img_base, img)


def img_gen(num):
    random.seed(datetime.now())
    for i in range(num):
        random.randint(3)
