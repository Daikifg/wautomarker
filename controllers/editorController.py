from tkinter import filedialog

import customtkinter as ctk
from PIL import Image

from models.models import IAWModel
from utils.config import BIG_IMG_CONTAINER_SIZE, REFERENCE_SIZE
from utils.helpers import calcAspectRatioImg, resizeToSquareImg
from views.editorView import EditorView


class EditorController:
    def __init__(self, root, model):
        self.root = root
        self.root.geometry("1200x600")
        self.root.title("Wautomarker - editor")
        self.root.columnconfigure(0, weight=1)

        self.actualIawObj = None

        self.model = model

        for x in range(0, len(self.model.imgsPath)):
            self.model.imgsAndWatermark[x] = IAWModel(
                Image.open(self.model.imgsPath[x]).convert("RGBA"),
                Image.open(self.model.watermarkPath),
                id=x,
            )

        self.editorView = EditorView(master=root, controller=self)

        self.displaySelectedImg(iawObj=self.model.imgsAndWatermark[0])

    def displaySelectedImg(self, iawObj):
        self.actualIawObj = iawObj
        openImg = self.displayWithWatermark(iawObj)
        self.editorView.mainImg.destroy()
        aspectRatio = calcAspectRatioImg(openImg.size)
        ctkImage = ctk.CTkImage(
            openImg, size=(resizeToSquareImg(aspectRatio, BIG_IMG_CONTAINER_SIZE))
        )
        self.editorView.mainImg = ctk.CTkLabel(self.editorView, image=ctkImage, text="")
        self.editorView.mainImg.grid(column=1, row=0)

    def displayWithWatermark(self, iawObj):
        """Return a Image Opened object"""
        # TODO  ADD CHANNEL ALPHA FOR OPACITY OPTION
        resizedWatermark = self.scaleWatermark(iawObj)
        iawObj.img.paste(resizedWatermark, iawObj.watermark_position)
        return iawObj.img

    def scaleWatermark(self, iawObj):
        img = iawObj.img
        watermark = iawObj.watermark
        imgSize = img.size
        watermarkSize = iawObj.watermark_size
        referenceSize = REFERENCE_SIZE
        scalingFactor = min(
            imgSize[0] / referenceSize[0], imgSize[1] / referenceSize[1]
        )

        newWatermarkSize = (
            int(watermarkSize[0] * scalingFactor),
            int(watermarkSize[1] * scalingFactor),
        )

        scaledWatermark = watermark.resize(newWatermarkSize)

        return scaledWatermark

    def setOpacity(self, value):
        pass
