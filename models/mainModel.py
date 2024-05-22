class MainModel:
    def __init__(self):
        self.imgs = []
        self.watermark = str

    def save_imgs(self, path):
        self.imgs.append(path)

    def save_watermark(self, path):
        self.watermark = path


# TODO make this a unique model file
