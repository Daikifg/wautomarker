import customtkinter as ctk

from utils.config import MINIATURE_IMG_CONTAINER_SIZE
from utils.helpers import calcAspectRatioImg, resizeToSquareImg


class LeftSideEditorView(ctk.CTkScrollableFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)
        self.controller = controller

        self.imgsList = [
            ctk.CTkImage(
                img.img,
                size=(
                    resizeToSquareImg(
                        calcAspectRatioImg(img.img.size),
                        MINIATURE_IMG_CONTAINER_SIZE,
                    )
                ),
            )
            for img in self.controller.model.imgsAndWatermark
        ]

        self.imgsListButtons = []

        for x in range(0, len(self.imgsList)):
            btn = ctk.CTkButton(
                master=self,
                image=self.imgsList[x],
                text="",
                fg_color="#333333",
                command=lambda x=x: self.controller.displaySelectedImg(
                    self.controller.model.imgsAndWatermark[x]
                ),
            )

            self.imgsListButtons.append(btn)

        for img in self.imgsListButtons:
            img.pack(pady=10)

        self.grid(column=0, row=0, sticky="nsew")


# TODO  Crop img overflow for make 250x100 miniatures
