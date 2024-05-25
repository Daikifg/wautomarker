import customtkinter as ctk
from PIL import Image

from utils.config import BIG_IMG_CONTAINER_SIZE
from utils.helpers import calcAspectRatioImg, resizeToSquareImg
from views.leftSideEditorView import LeftSideEditorView

FONT = "Rubik"


class EditorView(ctk.CTkFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)
        self.controller = controller
        self._fg_color = "transparent"
        self._set_appearance_mode("system")

        self.leftSide = LeftSideEditorView(
            master,
            controller,
            height=600,
            width=250,
        )

        openImg = Image.open(self.controller.model.imgs[0])
        aspectRatio = calcAspectRatioImg(openImg.size)
        ctkImage = ctk.CTkImage(
            openImg, size=(resizeToSquareImg(aspectRatio, BIG_IMG_CONTAINER_SIZE))
        )

        self.bigImg = ctk.CTkLabel(self, image=ctkImage, text="")

        self.bigImg.pack(expand=True, fill="both")
        self.grid(column=1, row=0)
