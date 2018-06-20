# -*- coding: utf-8 -*-
import sys
import os
# import pytesseract
from PIL import Image, ImageFilter, ImageEnhance, ImageChops

def img_binary(imgobj):
    """
    一种深度的二值化，速度慢
    :param imgobj:
    :return:
    """
    img = Image.open(imgobj).convert('RGBA')

    pixdata = img.load()

    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][0] < 90:
                pixdata[x, y] = (0, 0, 0, 255)

    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][1] < 136:
                pixdata[x, y] = (0, 0, 0, 255)

    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][2] > 0:
                pixdata[x, y] = (255, 255, 255, 255)
    # binaryImg = "".join(('binary__', imgobj))
    binaryImg = os.path.join(os.path.join(os.getcwd(), 'zip'), "".join(('binary__', os.path.basename(imgobj))))
    img.save(binaryImg)

    im_orig = Image.open(binaryImg)
    im_orig.resize((1000, 500), Image.NEAREST)
    return binaryImg

def binarizing(im,threshold):

     pixdata=im.load()

     w,h=im.size
     for j in range(h):
           for i in range(w):
                if pixdata[i,j]<threshold:
                     pixdata[i,j]=0
                else:
                     pixdata[i,j]=255
     return im

def denoising(im):

    pixdata=im.load()
    w,h=im.size
    for j in range(1,h-1):
        for i in range(1,w-1):
            count=0
            if pixdata[i,j-1]>245:
                count += 1
            if pixdata[i,j+1]>245:
                count += 1
            if pixdata[i+1,j]>245:
                count += 1
            if pixdata[i-1,j]>245:
                count += 1
            if count>2:
                pixdata[i,j]=255
    return im

def imgTransfer(imgobj):
    img=Image.open(imgobj)  #打开图片

    img=img.filter(ImageFilter.MedianFilter(1))  #对于输入图像的每个像素点，该滤波器从（size，size）的区域中拷贝中值对应的像素值存储到输出图像中

    img=ImageEnhance.Contrast(img).enhance(1.5)#enhance()的参数factor决定着图像的对比度情况。从0.1到0.5，再到0.8，2.0，图像的对比度依次增大.0.0为纯灰色图像;1.0为保持原始

    img=img.convert('L')   #灰度图转换

    img=denoising(img)     #图片去噪

    img=binarizing(img,200)  #图片二值化

    img = trimBoard(img)
    binaryImg = os.path.join(os.path.join(os.getcwd(), 'zip'), "".join(('binary__', os.path.basename(imgobj))))
    img.save(binaryImg)
    return binaryImg

def img_binary_simple(imgobj):
    """
    简单实用pil二值化，对待复杂的图片，不好
    :param imgobj:
    :return:
    """
    #  load a color image
    img = Image.open(imgobj)

    #  convert to grey level image
    binaryImg = os.path.join(os.path.join(os.getcwd(), 'zip'), "".join(('binary__', os.path.basename(imgobj))))
    imgobj = img.convert('L')
    imgobj.save(binaryImg)

    # #  setup a converting table with constant threshold
    # threshold = 80
    # table = []
    # for i in range(256):
    #     if i < threshold:
    #         table.append(0)
    #     else:
    #         table.append(1)
    #
    # # convert to binary image by the table
    # bim = Lim.point(table, '1')
    #
    # bim.save(binaryImg)
    return binaryImg

def trimBoard(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)







def checkIfImg(img):
    try:
        if os.path.isfile(img) and img.split('.')[1] in ('jpg', 'png', 'gif'):
            return True
        else:
            return False
    except Exception as e:
        return False

if __name__ == "__main__":
    if len(sys.argv[1:]) > 0:
        filenames = sys.argv[1:]
    else:
        # filenames =  os.listdir(os.getcwd())
        filenames = [os.path.join(os.path.join(os.path.join(os.getcwd(), 'origin')), fileitem)
                     for fileitem in os.listdir(os.path.join(os.getcwd(), 'origin'))]

    for file in filenames:
        if checkIfImg(file):
            binaryImg = imgTransfer(file)
            # vcode = pytesseract.image_to_string(Image.open(file), lang='3q+chi_sim')
            """
            0 = Orientation and script detection (OSD) only.
            1 = Automatic page segmentation with OSD.
            2 = Automatic page segmentation, but no OSD, or OCR
            3 = Fully automatic page segmentation, but no OSD. (Default)
            4 = Assume a single column of text of variable sizes.
            5 = Assume a single uniform block of vertically aligned text.
            6 = Assume a single uniform block of text.
            7 = Treat the image as a single text line.
            8 = Treat the image as a single word.
            9 = Treat the image as a single word in a circle.
            10 = Treat the image as a single character.
            -l lang and/or -psm pagesegmode must occur before anyconfigfile.
            """
            # 如果要识别圈中的数字，则不能二值化图片，需要使用原图，并加上config参数
            # vcode = pytesseract.image_to_string(Image.open(img_binary_simple(file)), lang='chi_sim+normal+3q', config='-psm 7')
            # print vcode.decode('utf-8')
        else:
            continue
