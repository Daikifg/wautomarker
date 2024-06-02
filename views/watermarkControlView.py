import customtkinter as ctk


class WatermarkControlView(ctk.CTkFrame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)
        self.controller = controller
        self._fg_color = "blue"
        self._set_appearance_mode("system")
        self.grid(column=2, row=0, sticky="nsew")


# TODO  ADD SIZE, OPACITY AND POSITION HANDLERS
# TODO  CREACTE SAVE ALL BTN
