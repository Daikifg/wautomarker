from utils.helpers import calcNewHeightImg


class MainModel:
    def __init__(self):
        self.imgsPath = []
        self.watermarkPath = str
        self.imgsAndWatermark = {}

    def set_imgs(self, path):
        self.imgsPath.append(path)

    def set_watermark(self, path):
        self.watermarkPath = path


# IAW: Image And Watermark
class IAWModel:
    def __init__(self, img, watermark, id):
        self.id = id
        self.img = img
        self.watermark = watermark
        self.watermark_position = {"x": 10, "y": 10}
        self.watermark_opacity = 100
        self.watermark_size = self.watermark.size

    def set_position(self, value, position):
        self.watermark_position[position] = int(value)

    def set_size(self, size):
        self.watermark_size = (size, calcNewHeightImg(self.watermark.size, size))

    def set_opacity(self, opacity):
        self.watermark_opacity = opacity

    def update_image(self, image):
        self.img = image


# TODO  IMAGE SHOULD BE PROPORTIONAL
