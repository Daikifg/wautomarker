from tkinter import filedialog

import customtkinter as ctk
from PIL import Image

from models.models import IAWModel
from utils.config import BIG_IMG_CONTAINER_SIZE, REFERENCE_SIZE
from utils.helpers import calcAspectRatioImg, resizeToSquareImg
from views.editorView import EditorView
from views.saveImageView import SaveImageView


class EditorController:
    def __init__(self, root, model):
        self.root = root
        self.root.geometry("1200x600")
        self.root.title("Wautomarker - editor")
        self.root.columnconfigure(0, weight=1)

        self.actualIawObj = None
        self.model = model
        self.saveView = None
        self.savePath = None

        for x in range(0, len(self.model.imgsPath)):
            self.model.imgsAndWatermark[x] = IAWModel(
                Image.open(self.model.imgsPath[x]).convert("RGBA"),
                Image.open(self.model.watermarkPath).convert("RGBA"),
                id=x,
            )

        self.editorView = EditorView(master=root, controller=self)

        self.displaySelectedImg(iawObj=self.model.imgsAndWatermark[0])

    def displaySelectedImg(self, iawObj):
        self.actualIawObj = iawObj
        openImg = self.addWatermark(iawObj)
        aspectRatio = calcAspectRatioImg(openImg.size)
        ctkImage = ctk.CTkImage(
            openImg,
            size=(resizeToSquareImg(aspectRatio, BIG_IMG_CONTAINER_SIZE)),
        )
        self.editorView.mainImg.configure(image=ctkImage)
        self.editorView.mainImg.grid(column=1, row=0)

    def addWatermark(self, iawObj):
        """Return a Image Opened object"""
        transparent_layer = Image.new("RGBA", iawObj.img.size, (0, 0, 0, 0))
        resizedWatermark = self.scaleWatermark(iawObj).convert("RGBA")

        orig_mask = resizedWatermark.split()[3]

        alpha = orig_mask.point(lambda a: a * (iawObj.watermark_opacity / 100))
        position = (
            iawObj.watermark_position["x"],
            iawObj.watermark_position["y"],
        )

        transparent_layer.paste(resizedWatermark, position, mask=alpha)
        imgWithWatermark = iawObj.img.copy()
        imgWithWatermark.alpha_composite(im=transparent_layer, dest=(0, 0))
        return imgWithWatermark

    def scaleWatermark(self, iawObj):
        img = iawObj.img.copy()
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
        self.model.imgsAndWatermark[self.actualIawObj.id].set_opacity(value)
        self.displaySelectedImg(
            self.model.imgsAndWatermark[self.actualIawObj.id]
        )

    def setSize(self, value):
        self.model.imgsAndWatermark[self.actualIawObj.id].set_size(value * 10)
        self.displaySelectedImg(
            self.model.imgsAndWatermark[self.actualIawObj.id]
        )

    def setPositionX(self, value, position="x"):
        xValue = (
            (value * self.actualIawObj.img.size[0]) / 100
        ) - self.actualIawObj.watermark_size[0] / 2
        self.model.imgsAndWatermark[self.actualIawObj.id].set_position(
            xValue, position
        )
        self.displaySelectedImg(
            self.model.imgsAndWatermark[self.actualIawObj.id]
        )

    def setPositionY(self, value, position="y"):
        yValue = (
            (value * self.actualIawObj.img.size[1]) / 100
        ) - self.actualIawObj.watermark_size[1] / 2
        self.model.imgsAndWatermark[self.actualIawObj.id].set_position(
            yValue, position
        )
        self.displaySelectedImg(
            self.model.imgsAndWatermark[self.actualIawObj.id]
        )

    def chooseAPath(self):
        self.savePath = filedialog.askdirectory()

    def openSaveDialog(self):
        if self.saveView is None or not self.saveView.winfo_exists():
            self.saveView = SaveImageView(self.root, self)

    def saveImgs(self):
        saveData = self.saveView.getValuesToSave()

        for _, value in self.model.imgsAndWatermark.items():
            self.addWatermark(value).save(
                f"{saveData["path"]}/{value.id}-{saveData["filename"]}{saveData["extension"]}"
            )
            print("img save in", saveData["path"])
