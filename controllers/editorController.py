from tkinter import filedialog

import customtkinter as ctk
from PIL import Image

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
        self.editorView = EditorView(master=root, controller=self)

    def displaySelectedImg(self, img):
        self.editorView.bigImg.destroy()
        openImg = Image.open(img)
        aspectRatio = calcAspectRatioImg(openImg.size)
        ctkImage = ctk.CTkImage(
            openImg, size=(resizeToSquareImg(aspectRatio, BIG_IMG_CONTAINER_SIZE))
        )
        self.editorView.bigImg = ctk.CTkLabel(self.editorView, image=ctkImage, text="")
        self.editorView.bigImg.pack()
