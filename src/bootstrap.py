from src.printer import DOCXPrinter
from src.scoring import ScoringModel
from src.views import ApplicationView


def init_project():
    printer = DOCXPrinter()
    model = ScoringModel()

    view = ApplicationView(model, printer)
    view.init()
