import dataclasses


@dataclasses.dataclass
class CreditContractDTO:
    client_full_name: str
    client_birth_date: str
    client_address: str
    client_passport_serial: str
    client_passport_number: str
    client_passport_by: str
    contract_number: str
    contract_price: float
    contract_duration: str
    contract_account: str
    contract_interest_rate: float
