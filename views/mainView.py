import customtkinter as ctk
from PIL import Image

ICON_PATH = "./assets/images/images_icon.png"
FONT = "Rubik"


class MainView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)

        self.controller = controller
        self._fg_color = "transparent"
        self._set_appearance_mode("system")
        self.imgMainIcon = ctk.CTkImage(
            light_image=Image.open(ICON_PATH),
            dark_image=Image.open(ICON_PATH),
            size=(200, 200),
        )

        self.labelWelcome = ctk.CTkLabel(
            self,
            text="Welcome to the Wautomarker",
            font=("Rubik bold", 26),
        )

        self.labelMainIcon = ctk.CTkLabel(
            self,
            image=self.imgMainIcon,
            text="",
        )

        self.selectImgBtn = ctk.CTkButton(
            self,
            text="Select here",
            width=240,
            height=50,
            font=(FONT, 18),
            command=self.controller.selectImgs,
        )

        self.labelWelcome.pack()
        self.labelMainIcon.pack()
        self.selectImgBtn.pack()

        self.pack(expand=True)
