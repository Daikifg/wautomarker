import customtkinter as ctk

from utils.config import FG_COLOR, FONT_FAMILY
from utils.helpers import updateEntryValue, updateSliderPosition

WIDTH_LABEL = 80
LABEL_FONT = (FONT_FAMILY, 16)
PADY_MODULES = 20
PADX_MODULES = 10
PADY_WIDGETS = 10


class WatermarkControlView(ctk.CTkFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)
        self.controller = controller
        self._fg_color = FG_COLOR
        self._corner_radius = 0
        self._set_appearance_mode("system")
        self.grid(column=2, row=0, sticky="nsew")

        # Size Handler
        self.sizeFrame = ctk.CTkFrame(self, corner_radius=15)
        self.sizeLabel = ctk.CTkLabel(
            self.sizeFrame,
            text="Size:",
            width=WIDTH_LABEL,
            anchor="w",
            font=LABEL_FONT,
        )
        self.sizeHandler = ctk.CTkSlider(
            self.sizeFrame,
            number_of_steps=100,
            from_=1,
            to=100,
            command=lambda value: updateEntryValue(
                self.controller.setSize, value, self.sizeEntry
            ),
        )
        self.sizeEntry = ctk.CTkEntry(
            self.sizeFrame, width=WIDTH_LABEL - 30, font=LABEL_FONT
        )

        self.sizeEntry.bind(
            "<Return>",
            lambda _: updateSliderPosition(
                self.controller.setSize,
                float(self.sizeEntry.get()),
                self.sizeHandler,
            ),
        )

        self.sizeLabel.grid(column=0, row=0, pady=PADY_WIDGETS)
        self.sizeEntry.grid(column=1, row=0, padx=10)
        self.sizeHandler.grid(column=0, row=1, columnspan=2, pady=PADY_WIDGETS)

        # Opacity Handler
        self.opacityFrame = ctk.CTkFrame(self, corner_radius=15)
        self.opacityLabel = ctk.CTkLabel(
            self.opacityFrame,
            text="Opacity(%):",
            width=WIDTH_LABEL,
            anchor="w",
            font=LABEL_FONT,
        )
        self.opacityHandler = ctk.CTkSlider(
            self.opacityFrame,
            number_of_steps=100,
            from_=0,
            to=100,
            command=lambda value: updateEntryValue(
                self.controller.setOpacity, value, self.opacityEntry
            ),
        )
        self.opacityEntry = ctk.CTkEntry(
            self.opacityFrame, width=WIDTH_LABEL - 30, font=LABEL_FONT
        )
        self.opacityEntry.bind(
            "<Return>",
            lambda _: updateSliderPosition(
                self.controller.setOpacity,
                float(self.opacityEntry.get()),
                self.opacityHandler,
            ),
        )

        self.opacityLabel.grid(column=0, row=0, pady=PADY_WIDGETS)
        self.opacityEntry.grid(column=1, row=0, padx=10)
        self.opacityHandler.grid(column=0, row=1, columnspan=2, pady=PADY_WIDGETS)

        # Position Handler
        self.positionFrame = ctk.CTkFrame(self, corner_radius=15)
        self.positionXLabel = ctk.CTkLabel(
            self.positionFrame,
            text="Position X:",
            width=WIDTH_LABEL,
            anchor="w",
            font=LABEL_FONT,
        )
        self.positionXHandler = ctk.CTkSlider(
            self.positionFrame,
            number_of_steps=100,
            from_=0,
            to=100,
            command=lambda value: updateEntryValue(
                self.controller.setPositionX, value, self.positionXEntry
            ),
        )
        self.positionXEntry = ctk.CTkEntry(
            self.positionFrame, width=WIDTH_LABEL - 30, font=LABEL_FONT
        )

        self.positionXEntry.bind(
            "<Return>",
            lambda _: updateSliderPosition(
                self.controller.setPositionX,
                float(self.positionXEntry.get()),
                self.positionXHandler,
            ),
        )

        self.positionXLabel.grid(column=0, row=0, pady=PADY_WIDGETS)
        self.positionXEntry.grid(column=1, row=0, padx=10)
        self.positionXHandler.grid(column=0, row=1, columnspan=2, pady=PADY_WIDGETS)

        self.positionYLabel = ctk.CTkLabel(
            self.positionFrame,
            text="Position Y:",
            width=WIDTH_LABEL,
            anchor="w",
            font=LABEL_FONT,
        )
        self.positionYHandler = ctk.CTkSlider(
            self.positionFrame,
            number_of_steps=100,
            from_=0,
            to=100,
            command=lambda value: updateEntryValue(
                self.controller.setPositionY, value, self.positionYEntry
            ),
        )

        self.positionYEntry = ctk.CTkEntry(
            self.positionFrame, width=WIDTH_LABEL - 30, font=LABEL_FONT
        )

        self.positionYEntry.bind(
            "<Return>",
            lambda _: updateSliderPosition(
                self.controller.setPositionY,
                float(self.positionYEntry.get()),
                self.positionYHandler,
            ),
        )

        self.positionYLabel.grid(column=0, row=2, pady=PADY_WIDGETS)
        self.positionYEntry.grid(column=1, row=2, padx=10)
        self.positionYHandler.grid(column=0, row=3, columnspan=2, pady=PADY_WIDGETS)

        # Save btn:
        self.saveAllBtn = ctk.CTkButton(
            self, text="Save all", command=self.controller.saveImgs
        )

        # display:
        self.sizeFrame.grid(column=0, row=0, pady=PADY_MODULES, padx=PADX_MODULES)
        self.opacityFrame.grid(column=0, row=1, pady=PADY_MODULES, padx=PADX_MODULES)
        self.positionFrame.grid(column=0, row=2, pady=PADY_MODULES, padx=PADX_MODULES)

        self.saveAllBtn.grid(column=0, row=3)
