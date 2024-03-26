import os
import pickle

from .predict_dto import PredictionDto

cwd = os.getcwd()


class ScoringModel:
    __model_path = os.path.join(os.sep, cwd, 'src', 'scoring', 'model.pkl')
    __occupations = ['Администратор', 'Архитектор', 'Бухгалтер', 'Доктор', 'Журналист', 'Инженер', 'Механик',
                     'Музыкант', 'Писатель', 'Предприниматель', 'Программист', 'Руководитель СМИ', 'Ученый', 'Учитель',
                     'Юрист']

    def __init__(self):
        self.__load_model()

    def __load_model(self):
        with open(self.__model_path, 'rb') as s:
            serializable = pickle.load(s)
            self.__classifier = serializable['classifier']
            self.__scaler = serializable['scaler']

    def predict(self, dto: PredictionDto):
        data = [dto.age,
                dto.annual_income,
                dto.monthly_inhand_salary,
                dto.num_bank_accounts,
                dto.num_credit_card,
                dto.interest_rate,
                dto.num_of_loan,
                dto.num_of_delayed_payment,
                dto.outstanding_debt,
                dto.credit_history_age]

        for occupation in self.__occupations:
            data.append(1 if dto.occupation == occupation else 0)

        scaled = self.__scaler.transform([data])
        return self.__classifier.predict(scaled)
