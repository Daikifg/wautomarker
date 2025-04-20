import customtkinter as ctk

from controllers.mainController import MainController


def main():
    root = ctk.CTk(fg_color="#333333")
    root.title("Wautomarker")
    root.geometry("700x400")
    root.resizable(False, False)

    app = MainController(root)

    root.mainloop()


if __name__ == "__main__":
    main()

# STABLE VERSION REQUIREMENTS:
# TODO  Display window for select the path to save img, choose a name and the extension ✅
# TODO  Center elements in Save Dialog. ✅
# TODO  Support to .png watermarks XD ✅

# TO IMROVE THE PROJECT:
# TODO  Change enter to release when change a set ✅
# TODO  Resize img preview to improve the performance
# TODO  Make a function to "back" for select or change another watermark, add or remove img from stack
# TODO  Change display miniature in the left side and make that update with the watermark too
# TODO  Save all images with same settings (create a check).
