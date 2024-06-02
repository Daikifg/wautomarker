import customtkinter as ctk

from utils.helpers import calcAspectRatioImg, resizeToSquareImg
from views.leftSideEditorView import LeftSideEditorView
from views.watermarkControlView import WatermarkControlView

FONT = "Rubik"


class EditorView(ctk.CTkFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)
        self.controller = controller
        self._fg_color = "transparent"
        self._set_appearance_mode("system")
        self.mainImg = ctk.CTkLabel(self, text="")

        self.leftSide = LeftSideEditorView(self, controller, height=600, width=250)

        self.watermarkControlPanel = WatermarkControlView(
            self, controller=controller, height=600, width=250
        )

        self.columnconfigure(1, weight=1)
        self.grid(column=0, row=0, sticky="nsew")


# TODO  create the control watermark view
