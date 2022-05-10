import pytest
import random
import string
import vcr
import os

from unittest import TestCase
from emnify.emnify import EMnify as emnify_client
from emnify import constants as emnify_const
from emnify import errors as emnify_errors

should_skip = 'TOKEN' not in os.environ
if not should_skip:
    TOKEN = os.environ['TOKEN']
TOKEN = 'test'

@pytest.fixture(scope='module')
def vcr_cassette_dir(request):
    return os.path.join('tests/fixtures', 'cassettes')


class EMnifyTest(TestCase):
    def setUp(self) -> None:
        self.token = 'token'

    @vcr.use_cassette('tests/fixtures/cassettes/get_all_devices.yaml')
    def test_get_devices_list(self):
        emnify = emnify_client(app_token=self.token)
        devices = [i for i in emnify.devices.get_devices_list()]
        self.assertGreater(len(devices), 0)
        self.assertIsInstance(devices[0], emnify.devices.device_model)

    @vcr.use_cassette('tests/fixtures/cassettes/device_events.yaml')
    def test_get_device_events_list(self):
        emnify = emnify_client(app_token=self.token)
        devices = [i for i in emnify.devices.get_devices_list()]
        device_events = [i for i in emnify.devices.get_device_events_list(devices[3])]
        self.assertGreater(len(device_events), 0)
        self.assertIsInstance(device_events[0], emnify.devices.event_model)

    @vcr.use_cassette('tests/fixtures/cassettes/create_device.yaml')
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

    @vcr.use_cassette('tests/fixtures/cassettes/send_sms_to_device.yaml')
    def test_send_sms(self):
        emnify = emnify_client(app_token=self.token)
        devices = [i for i in emnify.devices.get_devices_list()]
        sms = emnify.devices.sms_create_model(payload='sample_test_payload')
        emnify.devices.send_sms(device=devices[0], sms=sms)

    @vcr.use_cassette('tests/fixtures/cassettes/get_all_device_sms.yaml')
    def test_get_device_sms_list(self):
        emnify = emnify_client(app_token=self.token)
        devices = [i for i in emnify.devices.get_devices_list()]
        self.assertGreater(len(devices), 0)
        sms_instances = [i for i in emnify.devices.get_device_sms_list(device=devices[3])]
        self.assertGreater(len(sms_instances), 0)
        self.assertIsInstance(sms_instances[0], emnify.devices.list_sms_model)

    @vcr.use_cassette('tests/fixtures/cassettes/get_sim_list.yaml')
    def test_get_sim_list(self):
        emnify = emnify_client(app_token=self.token)
        sims = [i for i in emnify.sim.get_sim_list()]
        if sims:
            self.assertIsInstance(sims[0], emnify.sim.sim_list_model)

    @vcr.use_cassette('tests/fixtures/cassettes/activate_sim_by_bic_200.yaml')
    def test_activate_sim_by_one_size_batch_bic_200(self):
        bics = [  # BIC CODES
            'valid_bic_code',
            'invalid_bic_code'
            ]
        emnify = emnify_client(app_token=self.token)
        bic = bics[0]
        response = emnify.sim.register_sim(bic=bic)
        self.assertIsInstance(response, emnify.sim.sim_list_model)

    @vcr.use_cassette('tests/fixtures/cassettes/activate_sim_by_bic_422.yaml')
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

    @vcr.use_cassette('tests/fixtures/cassettes/create_device_with_sim.yaml')
    def test_create_device_with_sim(self):
        emnify = emnify_client(app_token=self.token)
        sims = [i for i in emnify.sim.get_sim_list()]
        if sims:
            self.assertIsInstance(sims[0], emnify.sim.sim_list_model)
        devices = [i for i in emnify.devices.get_devices_list()]

        name = ''.join(  # send any name current example are random
            random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(20)
        )

        status = emnify.devices.status_model(id=devices[0].status.id)
        tariff_profile = emnify.devices.tariff_profile_model(id=devices[0].tariff_profile.id)
        service_profile = emnify.devices.service_profile_model(id=devices[0].service_profile.id)
        sim_status = emnify.devices.status_model(id=1, description="Activated")
        sim = emnify.sim.sim_list_model(id=sims[0].id, status=sim_status)
        device = emnify.devices.device_create_model(
            name=name, tariff_profile=tariff_profile, status=status, service_profile=service_profile, sim=sim
        )

        response = emnify.devices.create_device(device=device)
        self.assertIs(response, True)

    @vcr.use_cassette('tests/fixtures/cassettes/test_activate_disactivate_device.yaml')
    def test_activate_disactivate_device(self):
        emnify = emnify_client(app_token=self.token)
        devices = [i for i in emnify.devices.get_devices_list()]
        active_device_with_sim = [
            i for i in devices if i.sim and i.status.id == emnify_const.DeviceStatuses.ENABLED_ID.value
        ][0]
        emnify.devices.change_status(active_device_with_sim.id, disable=True)

    @vcr.use_cassette('tests/fixtures/cassettes/test_update_device.yaml')
    def test_update_device(self):
        emnify = emnify_client(app_token=self.token)
        device = [i for i in emnify.devices.get_devices_list()][0]
        new_device_name = device.name + 'new'
        device_model_for_update = emnify.devices.device_update_model(name=new_device_name)
        emnify.devices.update_device(device_id=device.id, device=device_model_for_update)
        updated_device = emnify.devices.retrieve_device(device_id=device.id)
        self.assertNotEqual(device.name, updated_device.name)
