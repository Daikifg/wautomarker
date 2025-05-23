import customtkinter as ctk
from PIL import Image

from utils.config import FONT_FAMILY

ICON_PATH = "./assets/images/watermark_icon.png"


class WatermarkView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self._fg_color = "transparent"
        self._set_appearance_mode("system")

        self.imgWatermarkIcon = ctk.CTkImage(
            light_image=Image.open(ICON_PATH),
            dark_image=Image.open(ICON_PATH),
            size=(200, 200),
        )

        self.labelSelectWatermark = ctk.CTkLabel(
            self,
            text="Select your Watermark",
            font=(f"{FONT_FAMILY} bold", 26),
        )

        self.labelWatermarkIcon = ctk.CTkLabel(
            self,
            image=self.imgWatermarkIcon,
            text="",
        )

        self.selectWatermakBtn = ctk.CTkButton(
            self,
            text="Select here",
            width=240,
            height=50,
            font=(FONT_FAMILY, 18),
            command=self.controller.selectWatermark,
        )

        self.labelSelectWatermark.pack()
        self.labelWatermarkIcon.pack()
        self.selectWatermakBtn.pack()
