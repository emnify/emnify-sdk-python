from emnify.modules.sim.models import SimList, SimUpdate
from emnify.modules.sim.api_call_manager import SimListApi, SimActivateApi, SimUpdateApi, SimRetrieveApi
from emnify import constants as emnify_const


class SimManager:
    def __init__(self, client):
        self.client = client

    @property
    def sim_list_model(self):
        return SimList

    @property
    def sim_update_model(self):
        return SimUpdate

    def get_sim_list(self):
        sim_response = SimListApi().call_api(client=self.client)
        for sim in sim_response:
            yield self.sim_list_model(**sim)

    def retrieve_sim(self, sim_id: int):
        """
        Method for retrieving details of single sim by id
        """
        return SimList(**SimRetrieveApi().call_api(client=self.client, path_params={'sim': sim_id}))

    def register_sim(self, bic: str):
        data = emnify_const.SimStatusesDict.ACTIVATED_DICT.value
        sim_response = SimActivateApi().call_api(client=self.client, data=data, path_params={'bic': bic})
        if isinstance(sim_response, dict):
            return self.sim_list_model(**sim_response)
        return [self.sim_list_model(**sim) for sim in sim_response]

    def update_sim(self, sim_id: int, sim: SimUpdate) -> bool:
        """
        Method for updating sim`s
        :param sim_id: int of sim to update
        :param sim: filled sim update model
        """
        return SimUpdateApi()\
            .call_api(client=self.client, data=sim.dict(exclude_none=True), path_params={'sim': sim_id})

    def activate_sim(self, sim_id: int):
        """
        Method for activating sim - changing status to 'active'
        :param sim_id: int of sim to update
        """
        return SimUpdateApi() \
            .call_api(
            client=self.client, data={'status': emnify_const.SimStatusesDict.ACTIVATED_DICT.value},
            path_params={'sim': sim_id}
        )

    def suspend_sim(self, sim_id: int):
        """
        Method for activating sim - changing status to 'active'
        :param sim_id: int of sim to update
        """
        return SimUpdateApi() \
            .call_api(
            client=self.client, data={'status': emnify_const.SimStatusesDict.SUSPENDED_DICT.value},
            path_params={'sim': sim_id}
        )

    def issue_sim(self, sim_id: int):
        """
        Method for activating sim - changing status to 'active'
        :param sim_id: int of sim to update
        """
        return SimUpdateApi() \
            .call_api(
            client=self.client, data={'status': emnify_const.SimStatusesDict.ISSUED_DICT.value},
            path_params={'sim': sim_id}
        )
