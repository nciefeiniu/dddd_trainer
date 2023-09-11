import os

import string
import random

base_char = string.digits + string.ascii_letters


def get_random_string(length=32):
    return ''.join(random.choices(base_char, k=length))


for image in os.listdir('./train_images/linxia'):
    old_name = image.split('_')
    os.rename('./train_images/linxia/' + image, f"./train_images/linxia/{old_name[0]}_{get_random_string()}.jpg")