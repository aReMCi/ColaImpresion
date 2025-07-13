from models.model import DataModel as Model
from views.view import View

class Controller:
    def __init__(self, model,view):
        self.model = model
        self.view = view