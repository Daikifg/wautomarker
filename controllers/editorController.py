from tkinter import filedialog

from models.mainModel import MainModel
from views.editorView import EditorView


class EditorController:
    def __init__(self, root, model):
        self.root = root
        self.root.geometry("1024x600")
        self.model = model
        self.editorView = EditorView(master=root, controller=self, width=774)
