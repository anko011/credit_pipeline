from src.bank.bank import Bank
from src.printer import DOCXPrinter
from src.scoring import ScoringModel
from src.views import ApplicationView


def init_project():
    printer = DOCXPrinter()
    model = ScoringModel()
    bank = Bank(model, printer)

    view = ApplicationView(bank)
    view.init()
