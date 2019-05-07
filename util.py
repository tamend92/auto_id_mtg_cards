class Util:

    @staticmethod
    def flip_threshold_values(threshold_img):
        threshold_img[threshold_img == 0] = 254
        threshold_img[threshold_img == 255] = 0
        threshold_img[threshold_img == 254] = 255
        return threshold_img