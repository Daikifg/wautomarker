class ImgModel:
    def __init__(self):
        self.imgs = []

    def save_imgs(self, path):
        self.imgs.append(path)
        return self.imgs
