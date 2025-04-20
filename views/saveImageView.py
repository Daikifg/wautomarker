import customtkinter as ctk

from utils.config import FG_COLOR, FONT_FAMILY

LABEL_FONT = (FONT_FAMILY, 16)


class SaveImageView(ctk.CTkToplevel):
    def __init__(self, master, controller, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.configure(fg_color=FG_COLOR)
        self.controller = controller
        self.geometry("600x200")
        self.resizable(False, False)
        self.title("Save to...")

        # SETTING THE GRID
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=1)

        ####
        self.extensionFrame = ctk.CTkFrame(self, fg_color="transparent")
        self.saveFrame = ctk.CTkFrame(self, fg_color="transparent")
        self.pathFrame = ctk.CTkFrame(self, fg_color="transparent")

        self.chooseExtLabel = ctk.CTkLabel(
            self.extensionFrame, text="Choose a extension:", font=LABEL_FONT
        )

        self.extensionOptions = ctk.CTkOptionMenu(
            self.extensionFrame, values=[".png", ".jpg"]
        )

        self.chooseNameLabel = ctk.CTkLabel(
            self.pathFrame, text="Images name:", font=LABEL_FONT
        )
        self.namePathEntry = ctk.CTkEntry(self.pathFrame)
        self.pathBtn = ctk.CTkButton(
            self.pathFrame,
            text="Choose a filepath to save...",
            command=self.controller.chooseAPath,
        )
        self.pathPreviewLabel = ctk.CTkLabel(
            self.pathFrame, text=".example/file/path/image.png"
        )
        self.saveBtn = ctk.CTkButton(
            self.saveFrame,
            text="Save All",
            command=self.controller.saveImgs,
        )

        # DISPLAY
        self.extensionFrame.grid(row=1, column=1, pady=5, sticky="ew")
        self.pathFrame.grid(row=2, column=1, pady=5, sticky="ew")
        self.saveFrame.grid(row=3, column=1, pady=5)

        self.chooseExtLabel.grid(row=0, column=0)
        self.extensionOptions.grid(row=0, column=1)

        self.chooseNameLabel.grid(row=0, column=0)
        self.namePathEntry.grid(row=0, column=1)
        self.pathBtn.grid(row=0, column=2)
        self.pathPreviewLabel.grid(row=2, column=1)
        self.saveBtn.grid(row=0, column=2)

        self.transient(master)

    def getValuesToSave(self):
        return {
            "extension": self.extensionOptions.get(),
            "filename": self.namePathEntry.get(),
            "path": self.controller.savePath,
        }
