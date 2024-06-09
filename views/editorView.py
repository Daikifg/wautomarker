import customtkinter as ctk

from utils.config import FG_COLOR, HEIGHT_PANEL, WIDTH_PANEL
from utils.helpers import calcAspectRatioImg, resizeToSquareImg
from views.leftSideEditorView import LeftSideEditorView
from views.watermarkControlView import WatermarkControlView


class EditorView(ctk.CTkFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)
        self.controller = controller
        self._fg_color = "transparent"
        self._set_appearance_mode("system")
        self.mainImg = ctk.CTkLabel(self, text="")

        self.leftSide = LeftSideEditorView(
            self,
            controller,
            height=HEIGHT_PANEL,
            width=WIDTH_PANEL,
            corner_radius=0,
            fg_color=FG_COLOR,
        )

        self.watermarkControlPanel = WatermarkControlView(
            self, controller=controller, height=HEIGHT_PANEL, width=WIDTH_PANEL
        )

        self.columnconfigure(1, weight=1)
        self.grid(column=0, row=0, sticky="nsew")
