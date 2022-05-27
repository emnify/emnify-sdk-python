from emnify.modules.operator import models as operator_models
from emnify.modules.operator import api_call_manager as operator_api_manager


class OperatorManager:
    """
    Manager that allows to get a list of operators
    """
    def __init__(self, client):
        self.client = client

    def get_operators(self):
        for operator in operator_api_manager.GetOperatorList().call_api(client=self.client):
            yield operator_models.Operator(**operator)
