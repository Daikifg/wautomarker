class MainModel:
    def __init__(self):
        self.imgs = []
        self.watermark = str
        self.watermark_position = ()

    def save_imgs(self, path):
        self.imgs.append(path)

    def save_watermark(self, path):
        self.watermark = path

    def set_watermark_position(self, coordinates=(0, 0)):
        self.watermark_position = coordinates


# TODO make this a unique model file
