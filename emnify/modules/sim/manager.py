import typing

from emnify.modules.sim import models as sim_models
from emnify.modules.sim.api_call_manager import SimListApi, SimActivateApi, SimUpdateApi, SimRetrieveApi
from emnify import constants as emnify_const


class SimManager:
    def __init__(self, client):
        self.client = client

    @property
    def get_sim_list_model(self):
        return sim_models.SimList

    @property
    def get_sim_update_model(self):
        return sim_models.SimUpdate

    @property
    def get_sim_filter_model(self):
        return sim_models.SimFilter

    @property
    def get_sim_sort_enum(self):
        return emnify_const.SimSort

    def get_sim_list(
            self,
            without_device: bool = None,
            filter_model: sim_models.SimFilter = None,
            sort_enum: emnify_const.SimSort = None
    ):
        """
        :param without_device: Allows to add a filter for request to find all SIM`s without device
        :param filter_model: Model for request`s filtering
        :param sort_enum: Model for request`s sorting
        """
        query_params = self.__transform_sim_filter_params(
            without_device=without_device, filter_model=filter_model, sort_enum=sort_enum
        )

        sim_response = SimListApi().call_api(client=self.client, query_params=query_params)
        for sim in sim_response:
            yield self.get_sim_list_model(**sim)

    def retrieve_sim(self, sim_id: int):
        """
        Method for retrieving details of single sim by id
        """
        return sim_models.SimList(**SimRetrieveApi().call_api(client=self.client, path_params={'sim': sim_id}))

    def register_sim(self, bic: str) -> typing.Union[typing.List[sim_models.SimList], sim_models.SimList]:
        """
         :param bic: BIC number of sim/batch sims for registration
        """
        data = emnify_const.SimStatusesDict.ACTIVATED_DICT.value
        sim_response = SimActivateApi().call_api(client=self.client, data=data, path_params={'bic': bic})
        if isinstance(sim_response, dict):
            if sim_response.get('sim'):
                return [self.get_sim_list_model(**data) for data in sim_response['sim']]
            return self.get_sim_list_model(**sim_response)
        return [self.get_sim_list_model(**sim) for sim in sim_response]

    def update_sim(self, sim_id: int, sim: sim_models.SimUpdate) -> bool:
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

    @staticmethod
    def __transform_sim_filter_params(
            filter_model: sim_models.SimFilter = None,
            sort_enum: emnify_const.SimSort = None,
            without_device: bool = None

    ) -> dict:
        query_filter = {}
        if filter_model:
            filter_dict = filter_model.dict(exclude_none=True)
            query_filter['q'] = ','.join([f'{key}:{filter_dict[key]}' for key in filter_dict])
        if sort_enum:
            query_filter['sort'] = sort_enum
        if without_device is not None and without_device:
            if query_filter.get('q'):
                query_filter['q'] = query_filter['q']+'endpoint:null'
            else:
                query_filter['q'] = 'endpoint:null'
        return query_filter
