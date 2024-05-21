from tkinter import filedialog

from models.imgModel import ImgModel
from views.mainView import MainView


class MainController:
    def __init__(self, root):
        self.root = root
        self.model = ImgModel()
        self.view = MainView(master=root, controller=self)

    def selectImgs(self):
        imgs_paths = filedialog.askopenfilenames()
        for img in imgs_paths:
            self.model.save_imgs(img)
