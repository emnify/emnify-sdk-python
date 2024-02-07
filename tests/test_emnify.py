import pytest
import random
import string
import vcr
import os

from unittest import TestCase
from emnify.emnify import EMnify as emnify_client
from emnify import constants as emnify_const
from emnify import errors as emnify_errors


@pytest.fixture(scope='module')
def vcr_cassette_dir(request):
    return os.path.join('tests/fixtures', 'cassettes')


vcr_shared_parameters = {
    'filter_headers': ['authorization'],
    'filter_post_data_parameters': ['application_token', 'username', 'password'],
}

class EMnifyTest(TestCase):
    def setUp(self) -> None:
        self.token = os.environ.get('EMNIFY_SDK_APPLICATION_TOKEN', 'test_token')

    @vcr.use_cassette('tests/fixtures/cassettes/get_all_devices.yaml', **vcr_shared_parameters)
    def test_get_devices_list(self):
        emnify = emnify_client(app_token=self.token)
        devices = [i for i in emnify.devices.get_devices_list()]
        self.assertGreater(len(devices), 0)
        self.assertIsInstance(devices[0], emnify.devices.device_model)

    @vcr.use_cassette('tests/fixtures/cassettes/device_events.yaml', **vcr_shared_parameters)
    def test_get_device_events_list(self):
        emnify = emnify_client(app_token=self.token)
        devices = [i for i in emnify.devices.get_devices_list()]
        device_events = [i for i in emnify.devices.get_device_events_list(devices[3])]
        self.assertGreater(len(device_events), 0)
        self.assertIsInstance(device_events[0], emnify.devices.event_model)

    @vcr.use_cassette('tests/fixtures/cassettes/create_device.yaml', **vcr_shared_parameters)
    def test_create_device(self):
        emnify = emnify_client(app_token=self.token)
        for _ in range(0, 2):
            devices = [i for i in emnify.devices.get_devices_list()]

            name = ''.join(  # send any name current example are random
                random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(20)
            )

            status = emnify.devices.status_model(id=devices[0].status.id)
            tariff_profile = emnify.devices.tariff_profile_model(id=devices[0].tariff_profile.id)
            service_profile = emnify.devices.service_profile_model(id=devices[0].service_profile.id)

            device = emnify.devices.device_create_model(
                name=name, tariff_profile=tariff_profile, status=status, service_profile=service_profile
            )

            prev_devices_count = len([i for i in emnify.devices.get_devices_list()])
            emnify.devices.create_device(device=device)
            current_devices_count = len([i for i in emnify.devices.get_devices_list()])

        self.assertNotEqual(prev_devices_count, current_devices_count)
        self.assertGreater(current_devices_count, prev_devices_count)

    @vcr.use_cassette('tests/fixtures/cassettes/send_sms_to_device.yaml', **vcr_shared_parameters)
    def test_send_sms(self):
        emnify = emnify_client(app_token=self.token)
        devices = [i for i in emnify.devices.get_devices_list()]
        sms = emnify.devices.sms_create_model(payload='sample_test_payload')
        emnify.devices.send_sms(device=devices[0], sms=sms)

    @vcr.use_cassette('tests/fixtures/cassettes/get_all_device_sms.yaml', **vcr_shared_parameters)
    def test_get_device_sms_list(self):
        emnify = emnify_client(app_token=self.token)
        sms_instances = [i for i in emnify.devices.get_device_sms_list(device=11379224)]
        self.assertGreater(len(sms_instances), 0)
        self.assertIsInstance(sms_instances[0], emnify.devices.list_sms_model)

    @vcr.use_cassette('tests/fixtures/cassettes/get_sim_list.yaml', **vcr_shared_parameters)
    def test_get_sim_list(self):
        emnify = emnify_client(app_token=self.token)
        sims = [i for i in emnify.sim.get_sim_list()]
        if sims:
            self.assertIsInstance(sims[0], emnify.sim.get_sim_list_model)

    @vcr.use_cassette('tests/fixtures/cassettes/activate_sim_by_bic_200.yaml', **vcr_shared_parameters)
    def test_activate_sim_by_one_size_batch_bic_200(self):
        bics = [  # BIC CODES
            'valid_bic_code',
            'invalid_bic_code'
            ]
        emnify = emnify_client(app_token=self.token)
        bic = bics[0]
        response = emnify.sim.register_sim(bic=bic)
        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], emnify.sim.get_sim_list_model)

    @vcr.use_cassette('tests/fixtures/cassettes/activate_sim_by_bic_422.yaml', **vcr_shared_parameters)
    def test_activate_sim_by_one_size_batch_bic_422(self):
        bics = [  # BIC CODES
            'valid_bic_code',
            'invalid_bic_code'
        ]
        emnify = emnify_client(app_token=self.token)
        bic = bics[1]
        try:
            emnify.sim.register_sim(bic=bic)
        except emnify_errors.ValidationErrorException as e:
            self.assertEqual(str(e), 'Invalid bic number')

    @vcr.use_cassette('tests/fixtures/cassettes/create_device_with_sim.yaml', **vcr_shared_parameters)
    def test_create_device_with_sim(self):
        emnify = emnify_client(app_token=self.token)
        sims = [i for i in emnify.sim.get_sim_list()]
        if sims:
            self.assertIsInstance(sims[0], emnify.sim.get_sim_list_model)
        devices = [i for i in emnify.devices.get_devices_list()]

        name = ''.join(  # send any name current example are random
            random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(20)
        )

        status = emnify.devices.status_model(id=devices[0].status.id)
        tariff_profile = emnify.devices.tariff_profile_model(id=devices[0].tariff_profile.id)
        service_profile = emnify.devices.service_profile_model(id=devices[0].service_profile.id)
        sim_status = emnify.devices.status_model(id=1, description="Activated")
        sim = emnify.sim.get_sim_list_model(id=sims[0].id, status=sim_status)
        device = emnify.devices.device_create_model(
            name=name, tariff_profile=tariff_profile, status=status, service_profile=service_profile, sim=sim
        )

        response = emnify.devices.create_device(device=device)
        self.assertEqual(response, 11380016)

    @vcr.use_cassette('tests/fixtures/cassettes/test_activate_disactivate_device.yaml', **vcr_shared_parameters)
    def test_activate_disactivate_device(self):
        emnify = emnify_client(app_token=self.token)
        devices = [i for i in emnify.devices.get_devices_list()]
        active_device_with_sim = [
            i for i in devices if i.sim and i.status.id == emnify_const.DeviceStatuses.ENABLED_ID.value
        ][0]
        emnify.devices.change_status(active_device_with_sim.id, disable=True)

    @vcr.use_cassette('tests/fixtures/cassettes/test_update_device.yaml', **vcr_shared_parameters)
    def test_update_device(self):
        emnify = emnify_client(app_token=self.token)
        device = [i for i in emnify.devices.get_devices_list()][0]
        new_device_name = device.name + 'new'
        device_model_for_update = emnify.devices.device_update_model(name=new_device_name)
        emnify.devices.update_device(device_id=device.id, device=device_model_for_update)
        updated_device = emnify.devices.retrieve_device(device_id=device.id)
        self.assertNotEqual(device.name, updated_device.name)

    @vcr.use_cassette('tests/fixtures/cassettes/test_delete_device.yaml', **vcr_shared_parameters)
    def test_delete_device(self):
        emnify = emnify_client(app_token=self.token)
        all_devices = [i for i in emnify.devices.get_devices_list()]
        len_before_delete = len(all_devices)
        device = emnify.devices.retrieve_device(device_id=11380016)
        sim_id = device.sim.id
        self.assertTrue(device.sim)
        self.assertEqual(device.sim.status.description, 'Activated')

        emnify.devices.delete_device(device_id=device.id)
        changed_sim = emnify.sim.retrieve_sim(sim_id=sim_id)
        len_after_delete = len([i for i in emnify.devices.get_devices_list()])
        self.assertEqual(changed_sim.status.description, 'Suspended')
        self.assertGreater(len_before_delete, len_after_delete)

    @vcr.use_cassette('tests/fixtures/cassettes/test_list_device_blacklist.yaml', **vcr_shared_parameters)
    def test_list_device_blacklist(self):
        emnify = emnify_client(app_token=self.token)
        device_id = 11380018
        operators = [i for i in emnify.devices.get_device_operator_blacklist(device_id=device_id)]
        self.assertGreater(len(operators), 0)
        self.assertEqual(operators[0].country.name, 'Albania')

    @vcr.use_cassette('tests/fixtures/cassettes/test_delete_blacklist_operator.yaml', **vcr_shared_parameters)
    def test_delete_blacklist_operator(self):
        emnify = emnify_client(app_token=self.token)
        device_id = 11380018
        previous_operators_list = [i for i in emnify.devices.get_device_operator_blacklist(device_id=device_id)]
        emnify.devices.delete_device_blacklist_operator(device_id=device_id, operator_id=previous_operators_list[0].id)
        updated_operators_list = [i for i in emnify.devices.get_device_operator_blacklist(device_id=device_id)]

        self.assertGreater(len(previous_operators_list), len(updated_operators_list))

    @vcr.use_cassette('tests/fixtures/cassettes/test_add_blacklist_operator.yaml', **vcr_shared_parameters)
    def test_add_blacklist_operator(self):
        emnify = emnify_client(app_token=self.token)
        device_id = 11380018
        operator_id = 553
        previous_operators_list = [i for i in emnify.devices.get_device_operator_blacklist(device_id=device_id)]
        emnify.devices.add_device_blacklist_operator(device_id=device_id, operator_id=operator_id)
        updated_operators_list = [i for i in emnify.devices.get_device_operator_blacklist(device_id=device_id)]
        self.assertGreater(len(updated_operators_list), len(previous_operators_list))

    @vcr.use_cassette('tests/fixtures/cassettes/test_add_blacklist_operator_error.yaml', **vcr_shared_parameters)
    def test_add_blacklist_operator_error(self):
        emnify = emnify_client(app_token=self.token)
        device_id = 11380018
        operator_id = 553
        try:
            emnify.devices.add_device_blacklist_operator(device_id=device_id, operator_id=operator_id)
        except emnify_errors.ValidationErrorException:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    @vcr.use_cassette('tests/fixtures/cassettes/test_operator_list.yaml', **vcr_shared_parameters)
    def test_operator_list(self):
        emnify = emnify_client(app_token=self.token)
        operators = [i for i in emnify.operator.get_operators()]
        self.assertGreater(len(operators), 0)

    @vcr.use_cassette('tests/fixtures/cassettes/test_reset_connectivity.yaml', **vcr_shared_parameters)
    def test_reset_connectivity(self):
        emnify = emnify_client(app_token=self.token)
        device_id = 12132821
        self.assertTrue(emnify.devices.reset_connectivity_data(device_id=device_id))

    @vcr.use_cassette('tests/fixtures/cassettes/test_reset_connectivity_network.yaml', **vcr_shared_parameters)
    def test_reset_connectivity_network(self):
        emnify = emnify_client(app_token=self.token)
        device_id = 12132821
        self.assertTrue(emnify.devices.reset_connectivity_network(device_id=device_id))

    @vcr.use_cassette('tests/fixtures/cassettes/test_get_device_connectivity.yaml', **vcr_shared_parameters)
    def test_get_device_connectivity_data(self):
        emnify = emnify_client(app_token=self.token)
        device_id = 12132821
        connectivity_data = emnify.devices.get_device_connectivity_status(device_id=device_id)
        self.assertEqual(connectivity_data.status.description, 'OFFLINE')
