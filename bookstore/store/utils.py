import os


def get_carousel_img_list():
    carousel_img_list = []
    carousel_folder = os.walk('./static/img/carousel')
    for address, dirs, files in carousel_folder:
        for file in files:
            carousel_img_list.append(file)
    return carousel_img_list

