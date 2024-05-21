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
