from tkinter import filedialog

import customtkinter as ctk
from PIL import Image

from models.models import IAWModel
from utils.config import BIG_IMG_CONTAINER_SIZE
from utils.helpers import calcAspectRatioImg, resizeToSquareImg
from views.editorView import EditorView


class EditorController:
    def __init__(self, root, model):
        self.root = root
        self.root.geometry("1024x600")
        self.root.title("Wautomarker - editor")
        self.root.grid_columnconfigure(0, minsize=250, weight=0)
        self.root.grid_columnconfigure(1, weight=1)

        self.model = model

        for img in self.model.imgsPath:
            self.model.imgsAndWatermark.append(
                IAWModel(Image.open(img), Image.open(self.model.watermarkPath))
            )

        self.editorView = EditorView(master=root, controller=self)

        self.displaySelectedImg(iawObject=self.model.imgsAndWatermark[0])

    def displaySelectedImg(self, iawObject):
        openImg = self.displayWithWatermark(iawObject)
        self.editorView.mainImg.destroy()
        aspectRatio = calcAspectRatioImg(openImg.size)
        ctkImage = ctk.CTkImage(
            openImg, size=(resizeToSquareImg(aspectRatio, BIG_IMG_CONTAINER_SIZE))
        )
        self.editorView.mainImg = ctk.CTkLabel(self.editorView, image=ctkImage, text="")
        self.editorView.mainImg.pack()

    def displayWithWatermark(self, iawObject):
        """Return a Image Opened object"""
        resizedWatermark = iawObject.watermark.resize(iawObject.size)
        iawObject.img.paste(resizedWatermark, iawObject.position)
        return iawObject.img
