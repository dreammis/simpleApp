# coding: utf-8
import os
from pytesseract import pytesseract
from PIL import Image

c_path = "D:/pookz/own/simpleApp/tesseract_train/train_pic"

# pic_list = sorted([i for i in os.listdir('.') if os.path.isfile(i) and os.path.splitext(i)[1] == '.png'])
# [os.rename(os.path.join(c_path, i), os.path.join(c_path, index)) i for i in os.listdir(c_path)]

with open(os.path.join('.', "r_file.txt"), "wb+") as f:
    for index, png_file in enumerate(os.listdir(c_path), start=1):
        full_path = os.path.join(c_path, png_file)
        if os.path.isfile(full_path) and os.path.splitext(png_file)[1] == '.png':
            new_name = os.path.join(c_path, str(index) + '.png')
            os.rename(full_path, new_name)
            answer = pytesseract.image_to_string(Image.open(new_name), lang="da",
                                                 config='--psm 6 -c textord_heavy_nr=1 -c chop_enable=F')
            # f.writelines("\t".join([str(index), answer]))
            f.writelines("\t".join([answer]))
            if index % 16 == 0:
                f.writelines('\n')
                f.writelines(str(index+1))
