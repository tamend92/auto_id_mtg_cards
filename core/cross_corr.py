import operator
import cv2
import os
import numpy as np


def calculate_cross_correlations(target_im_path):
    #gets target image path
    #just passing in the name for now until we can use something different

    set_directory = 'D:/nyufiles/Computer Vision/Project_Fork/auto_id_mtg_cards/png_set_images/'
    cv2_method = 'cv2.TM_CCORR_NORMED'

    targ_set_im = cv2.imread(target_im_path, cv2.COLOR_RGB2GRAY)
    #need to crop the target set image to remove white space noise
    #potential white space to image ratio damaging correlation

    t_im_height, t_im_width, channel = targ_set_im.shape

    cross_correlation_results = { }

    for filename in os.listdir(set_directory):
        if filename.endswith('.png'):
            curr_set_image = cv2.imread(set_directory + filename, cv2.COLOR_RGB2GRAY)

            resized_set_image = cv2.resize(curr_set_image, (t_im_width, t_im_height), interpolation = cv2.INTER_AREA)

            result = cv2.matchTemplate(targ_set_im, resized_set_image, cv2.TM_CCORR_NORMED)

            cross_correlation_results[filename] = result

    print(max(cross_correlation_results.items(), key=operator.itemgetter(1))[0])
    print(max(cross_correlation_results.items(), key=operator.itemgetter(1))[1])

if __name__ == '__main__':
    calculate_cross_correlations('tyler_test.jpg')


