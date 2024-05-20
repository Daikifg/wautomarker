from models.mainModel import ExampleModel
from views.mainView import MainView


class MainController:
    def __init__(self, root):
        self.root = root
        self.model = ExampleModel()
        self.view = MainView(master=root, controller=self)
