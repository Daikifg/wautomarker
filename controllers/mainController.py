from tkinter import filedialog

from controllers.editorController import EditorController
from models.models import MainModel
from views.mainView import MainView
from views.watermarkView import WatermarkView


class MainController:
    def __init__(self, root):
        self.root = root
        self.model = MainModel()
        self.mainView = MainView(self.root, controller=self)
        self.watermarkView = WatermarkView(master=root, controller=self)

    def selectImgs(self):
        imgs_paths = filedialog.askopenfilenames()
        for img in imgs_paths:
            self.model.set_imgs(img)
        self.mainView.pack_forget()
        self.watermarkView.pack(expand=True)

    def selectWatermark(self):
        self.model.set_watermark(filedialog.askopenfilename())
        self.watermarkView.pack_forget()
        EditorController(self.root, self.model)
