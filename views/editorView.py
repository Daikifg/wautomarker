import customtkinter as ctk
from PIL import Image

from utils.helpers import calcNewHeightImg

FONT = "Rubik"


class EditorView(ctk.CTkFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)
        self.controller = controller
        self._fg_color = "#97BE5A"
        self._set_appearance_mode("system")

        self.titleLabel = ctk.CTkLabel(
            master=self, text="Welcome to editor", font=(FONT, 24), text_color="#FF0000"
        )

        self.leftSide = LeftSideView(master, controller, height=600, width=250)

        self.titleLabel.pack()
        self.grid(column=1, row=0)


class LeftSideView(ctk.CTkScrollableFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)
        self.controller = controller
        self._fg_color = "#FF0000"
        self._set_appearance_mode("system")

        self.imgs = [Image.open(img) for img in self.controller.model.imgs]

        self.imgsList = [
            ctk.CTkImage(img, size=(250, calcNewHeightImg(img.size, width=250)))
            for img in self.imgs
        ]

        self.imgsListButtons = [
            ctk.CTkButton(master=self, image=img, text="", fg_color="#333333")
            for img in self.imgsList
        ]

        for img in self.imgsListButtons:
            img.pack(pady=10)

        self.grid(column=0, row=0)
