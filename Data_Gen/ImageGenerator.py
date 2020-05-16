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

symbol_list = ["Do_Not_Enter.png", "No_Left_Turn_Symbol.png", "No_Right_Turn.png", "No_U_Turn.png", "Stop_Sign.png", "Barrel.png"]
folder_list = ["do_not_enter", "no_left_turn", "no_right_turn", "no_u_turn", "stop", "barrel"]
img_base_prefix = "C:\\Users\\1995h\\PycharmProjects\\senior_project\\Data_Gen\\background_images\\"
img_path_prefix = "C:\\Users\\1995h\\PycharmProjects\\senior_project\\Data_Gen\\"

# img_base = "C:\\Users\\1995h\\PycharmProjects\\senior_project\\Data_Gen\\base.PNG"
# img_path = "C:\\Users\\1995h\\PycharmProjects\\senior_project\\Data_Gen\\No_Left_Turn_Symbol.jpg"

# img = cv2.imread(img_path)
# img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
#
# img_base = cv2.imread(img_base)
# img_base = cv2.cvtColor(img_base, cv2.COLOR_RGB2BGR)

# plt.imshow(img_base)
# plt.show()


def rotation(image, angle):
    return rotate(image, angle)


def add_noise(image):
    noise_index = random.randint(0, 2)
    seed = random.randint(5000, 12000)
    if noise_index == 0:
        mean = random.random()/2 - 0.25
        var = random.random() / 2 + 0.3
        return random_noise(image, mode="gaussian", seed=seed, mean=mean, var=var)
    elif noise_index == 1:
        amount = random.random() / 4 + 0.4
        return random_noise(image, mode="pepper", seed=seed, amount=amount)
    elif noise_index == 2:
        amount = random.random() / 4 + 0.4
        return random_noise(image, mode="salt", seed=seed, amount=amount)
    else:
        amount = random.random() / 4 + 0.4
        return random_noise(image, mode="s&p", seed=seed, amount=amount)


def blur_image(image):
    return cv2.GaussianBlur(image, (9, 9), 0)


def paste_image(base, sign):
    base = base.copy()
    sign = rotation(sign.copy(), 10)
    length = base.shape[0]
    width = base.shape[1]
    ratio = 1/20
    sign = Image.fromarray((sign * 255).astype(np.uint8))
    sign.thumbnail((30, 30))
    base = Image.fromarray(base)
    # new_sign = Image.fromarray(sign)
    base.paste(sign, (350, 200))
    base.save("C:\\Users\\1995h\\PycharmProjects\\senior_project\\Data_Gen\\sign_gen_sample3.PNG", "PNG")


# paste_image(img_base, img)


def img_gen(start, end, traffic_sign):
    random.seed(datetime.now())
    base_length = 80
    for i in range(start, end, 1):
        func_index = random.randint(0, 1)
        img_base_path = img_base_prefix + "background_" + str(random.randint(1, base_length)) + ".PNG"
        traffic_path = img_path_prefix + symbol_list[traffic_sign]
        try:
            img = cv2.imread(traffic_path)
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            img_base = cv2.imread(img_base_path)
            img_base = cv2.cvtColor(img_base, cv2.COLOR_RGB2BGR)
            base = img_base.copy()
            if func_index == 0:
                degree = random.randint(-7, 7)  # randomly rotate -7 degree to 7 degree clockwise
                sign = rotation(img.copy(), degree)
            elif func_index == 1:
                sign = add_noise(img.copy())
            else:
                sign = blur_image(img.copy())
            sign = Image.fromarray((sign * 255).astype(np.uint8))
            resize_dim = random.randint(30, 100)    # randomly resize the traffic sign from 30 x 30 to 100 x 100
            sign.thumbnail((resize_dim, resize_dim))
            base = Image.fromarray(base)
            horizontal = random.randint(100, 1000)
            vertical = random.randint(100, 600)
            base.paste(sign, (horizontal, vertical))
            save_path = "C:\\Users\\1995h\\PycharmProjects\\senior_project\\Data_Gen\\generated_images\\" + folder_list[traffic_sign] + "\\" + "gen_" + str(i) + "_" + symbol_list[traffic_sign]
            base.save(save_path, symbol_list[traffic_sign].split(".")[1])
        except Exception as e:
            print(e)
            print(img_base_path)
            print(traffic_path)
            continue
    print("Done!")


img_gen(1, 501, 5)
