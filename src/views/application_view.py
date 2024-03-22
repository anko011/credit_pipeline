class ApplicationView:
    def __init__(self, model, printer):
        self.__printer = printer
        self.__model = model

    def init(self):
        ...
