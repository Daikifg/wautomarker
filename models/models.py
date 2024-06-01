class MainModel:
    def __init__(self):
        self.imgsPath = []
        self.watermarkPath = str
        self.imgsAndWatermark = []

    def set_imgs(self, path):
        self.imgsPath.append(path)

    def set_watermark(self, path):
        self.watermarkPath = path


# IAW: Image And Watermark
class IAWModel:
    def __init__(self, img, watermark):
        self.img = img
        self.watermark = watermark
        self.position = (0, 0)
        self.opacity = 1
        self.size = (100, 100)

    def set_position(self, coordinates):
        self.position = coordinates

    def set_size(self, size):
        self.size = size

    def set_opacity(self, opacity):
        self.opacity = opacity
