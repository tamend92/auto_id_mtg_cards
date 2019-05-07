import os
import cv2
from util import Util


class PreprocessorImg:

    def __init__(self, img_path):
        self.mtg_img = cv2.imread(img_path)
        self.mtg_just_card_thres = self._get_just_card_thres()
        self._find_set_image()
        # cv2.imwrite('blah_img.jpg', self.mtg_just_card)

    def _get_just_card_thres(self):
        """
        https://stackoverflow.com/questions/51656362/how-do-i-crop-the-black-background-of-the-image-using-opencv-in-python
        :return:
        """
        grayscale = cv2.cvtColor(self.mtg_img, cv2.COLOR_BGR2GRAY)
        thes, thresholded = cv2.threshold(grayscale, 50, 255, cv2.THRESH_BINARY)
        thresholded = Util.flip_threshold_values(thresholded)
        bbox = cv2.boundingRect(thresholded)
        x, y, w, h = bbox
        foreground = thresholded[y:y + h, x:x + w]
        cv2.imwrite("thres_img.png", foreground)
        return foreground

    def _find_set_image(self):
        """
        Finding the set image is not that hard because it will always be in the middle of the image. So we just
        find it and crop it out.
        We could use edges to find the set image(?)
        :return:
        """
        height, width = self.mtg_just_card_thres.shape
        height_into_parts_for_cropping = 20
        width_into_parts_for_cropping = 20
        set_image_width = round(width/height_into_parts_for_cropping)
        set_image_height = round(height/width_into_parts_for_cropping)
        start_height = round(set_image_height * 11.4)
        start_width = set_image_width * 16
        crop_set_img = self.mtg_just_card_thres[start_height:start_height + round(set_image_height/1.2),
                       start_width:start_width + round((set_image_width *2))]
        crop_set_img = Util.flip_threshold_values(crop_set_img)
        cv2.imwrite('thres_set_img.jpg', crop_set_img)
        cv2.waitKey()

if __name__ == '__main__':
    pre_process = PreprocessorImg(os.path.join('..', 'mtg_test_photos', 'mtg_1.jpg'))