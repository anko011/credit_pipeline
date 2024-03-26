from dataclasses import dataclass


@dataclass
class PredictionDto:
    age: int  # возраст
    occupation: str  # должность
    interest_rate: int  # кредитная ставка
    annual_income: float  # годовой доход
    monthly_inhand_salary: float  # заработная плата
    num_bank_accounts: int  # количество банковских аккаунтов
    num_credit_card: int  # количество кредитных карт
    num_of_loan: int  # количество существующих кредитов
    outstanding_debt: float  # невыплаченный кредит (сумма деняг)
    credit_history_age: int  # кредитная история (количество месяцев)
    num_of_delayed_payment: int  # общее количество просроченных платежей
