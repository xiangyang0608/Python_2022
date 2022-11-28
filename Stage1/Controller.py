import Model
import GUI.View as View


class Controller(object):
    # initialzie a controller
    def __init__(self, model):
        self.model = model
        self.view = View.View(model.get_data())

    def execute(self):
        self.view.mainpage()
