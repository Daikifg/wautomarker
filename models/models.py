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
        self.watermark_position = (0, 0)
        self.watermark_opacity = 1
        self.watermark_size = (100, 100)

    def set_position(self, coordinates):
        self.watermark_position = coordinates

    def set_size(self, size):
        self.watermark_size = size

    def set_opacity(self, opacity):
        self.watermark_opacity = opacity


# TODO  IMAGE SHOULD BE PROPORTIONAL
