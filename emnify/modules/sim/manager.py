import typing

from emnify.modules.sim import models as sim_models
from emnify.modules.sim.api_call_manager import SimListApi, SimActivateApi, SimUpdateApi, SimRetrieveApi
from emnify import constants as emnify_const


class SimManager:
    """
    Provides methods for interacting with SIM cards using the EMnify API.

    Args:
        client: An instance of the EMnify class used for making API requests.
    """
    def __init__(self, client):
        self.client = client

    @property
    def get_sim_list_model(self):
        """
        Returns the model for the SIM list.
        """
        return sim_models.SimList

    @property
    def get_sim_update_model(self):
        """
        Returns the model for updating SIM cards.
        """
        return sim_models.SimUpdate

    @property
    def get_sim_filter_model(self):
        """
        Returns the model for filtering SIM cards.
        """
        return sim_models.SimFilter

    @property
    def get_sim_sort_enum(self):
        """
        Returns sim sorting options.
        """
        return emnify_const.SimSort

    def get_sim_list(
            self,
            without_device: bool = None,
            filter_model: sim_models.SimFilter = None,
            sort_enum: emnify_const.SimSort = None
    ) -> typing.Generator[sim_models.SimList, None, None]:
        """
        Retrieve iterable list of SIM`s.
        :param without_device: Allows to add a filter for request to find all SIM`s without device
        :param filter_model: Model for request`s filtering
        :param sort_enum: Model for request`s sorting
        """
        query_params = self.__transform_sim_filter_params(
            without_device=without_device, filter_model=filter_model, sort_enum=sort_enum
        )

        sim_response = SimListApi().call_api(client=self.client, query_params=query_params)

        return (self.get_sim_list_model(**i) for i in sim_response)

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
        Activates `suspended` or `issued` SIM.
        If you want to control both the device and SIM as a whole, it's recommended to use the :class:`DeviceManager.change_status` method if the SIM is assigned to a device.
        Learn more about SIM Lifecycle: https://docs.emnify.com/services/sim-lifecycle-management
        :param sim_id: int of sim to update
        """
        return SimUpdateApi() \
            .call_api(
            client=self.client, data={'status': emnify_const.SimStatusesDict.ACTIVATED_DICT.value},
            path_params={'sim': sim_id}
        )

    def suspend_sim(self, sim_id: int):
        """
        Puts the `active` SIM to `suspended` state.
        If you want to control both the device and SIM as a whole, it's recommended to use the :class:`DeviceManager.change_status` method if the SIM is assigned to a device.
        Learn more about SIM Lifecycle: https://docs.emnify.com/services/sim-lifecycle-management
        :param sim_id: id of sim to update
        """
        return SimUpdateApi() \
            .call_api(
            client=self.client, data={'status': emnify_const.SimStatusesDict.SUSPENDED_DICT.value},
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
