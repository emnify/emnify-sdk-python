from emnify.modules.sim.models import SimList
from emnify.modules.sim.api_call_manager import SimListApi, SimActivateApi


class SimManager:
    def __init__(self, client):
        self.client = client

    @property
    def SimListModel(self):
        return SimList

    def get_sim_list(self):
        sim_response = SimListApi().call_api(client=self.client)
        for sim in sim_response:
            yield self.SimListModel(**sim)

    def activate_sim_by_bic(self, bic: str):
        data = {
                  "sim_status": {
                    "id": 1
                  }
                }
        sim_response = SimActivateApi().call_api(client=self.client, data=data, path_params={'bic': bic})
        if isinstance(sim_response, dict):
            return self.SimListModel(**sim_response)
        return [self.SimListModel(**sim) for sim in sim_response]

