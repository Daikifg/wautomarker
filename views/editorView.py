import customtkinter as ctk

from utils.helpers import calcAspectRatioImg, resizeToSquareImg
from views.leftSideEditorView import LeftSideEditorView

FONT = "Rubik"


class EditorView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self._fg_color = "transparent"
        self._set_appearance_mode("system")
        self.mainImg = ctk.CTkLabel(self, text="")

        self.leftSide = LeftSideEditorView(
            master,
            controller,
            height=600,
            width=250,
        )

        self.grid(column=1, row=0)


# TODO  create the control watermark view
