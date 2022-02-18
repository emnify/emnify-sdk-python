import pytest
import os
import random
import string
from unittest import TestCase
from emnify.emnify import EMnify as emnify_client


should_skip = 'TOKEN' not in os.environ
if not should_skip:
    TOKEN = os.environ['TOKEN']


@pytest.mark.skipif(should_skip, reason="No environment variables configured")
class EMnifyTest(TestCase):
    def setUp(self) -> None:
        self.token = TOKEN

    def test_get_all_devices(self):
        emnify = emnify_client(app_token=self.token)
        devices = [i for i in emnify.devices.get_all_devices()]
        self.assertGreater(len(devices), 0)
        self.assertIsInstance(devices[0], emnify.devices.device_model)

    def test_get_device_events(self):
        emnify = emnify_client(app_token=self.token)
        devices = [i for i in emnify.devices.get_all_devices()]
        device_events = [i for i in emnify.devices.get_device_events(devices[0])]
        self.assertGreater(len(device_events), 0)
        self.assertIsInstance(device_events[0], emnify.devices.event_model)

    def test_create_device(self):
        emnify = emnify_client(app_token=self.token)
        for _ in range(0, 13):
            devices = [i for i in emnify.devices.get_all_devices()]

            name = ''.join(  # send any name current example are random
                random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(20)
            )

            status = emnify.devices.status_model(id=devices[0].status.id)
            tariff_profile = emnify.devices.tariff_profile_model(id=devices[0].tariff_profile.id)
            service_profile = emnify.devices.service_profile_model(id=devices[0].service_profile.id)

            device = emnify.devices.device_model(
                name=name, tariff_profile=tariff_profile, status=status, service_profile=service_profile
            )

            prev_devices_count = len([i for i in emnify.devices.get_all_devices()])
            emnify.devices.create_device(device=device)
            current_devices_count = len([i for i in emnify.devices.get_all_devices()])

        self.assertNotEqual(prev_devices_count, current_devices_count)
        self.assertGreater(current_devices_count, prev_devices_count)

    def test_send_sms_to_device(self):
        emnify = emnify_client(app_token=self.token)
        devices = [i for i in emnify.devices.get_all_devices()]
        sms = emnify.devices.sms_create_model(payload='sample_test_payload')
        emnify.devices.send_sms_to_device(device=devices[0], sms=sms)

    def test_get_all_device_sms(self):
        emnify = emnify_client(app_token=self.token)
        devices = [i for i in emnify.devices.get_all_devices()]
        self.assertGreater(len(devices), 0)
        sms_instances = [i for i in emnify.devices.get_all_device_sms(device=devices[0])]
        self.assertGreater(len(sms_instances), 0)
        self.assertIsInstance(sms_instances, emnify.devices.list_sms_model)

    def test_get_sim_list(self):
        emnify = emnify_client(app_token=self.token)
        sims = [i for i in emnify.sim.get_sim_list()]
        if sims:
            self.assertIsInstance(sims[0], emnify.sim.SimListModel)

    def test_activate_sim_by_bic(self):
        bics = []
        emnify = emnify_client(app_token=self.token)
        bic = bics[5]
        response = emnify.sim.activate_sim_by_bic(bic=bic)
        self.assertIsInstance(response, emnify.sim.SimListModel)

    def test_create_device_with_sim(self):
        emnify = emnify_client(app_token=self.token)
        sims = [i for i in emnify.sim.get_sim_list()]
        if sims:
            self.assertIsInstance(sims[0], emnify.sim.SimListModel)
        devices = [i for i in emnify.devices.get_all_devices()]

        name = ''.join(  # send any name current example are random
            random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(20)
        )

        status = emnify.devices.status_model(id=devices[-1].status.id)
        tariff_profile = emnify.devices.tariff_profile_model(id=devices[-1].tariff_profile.id)
        service_profile = emnify.devices.service_profile_model(id=devices[-1].service_profile.id)
        sim = emnify.sim.SimListModel(id=sims[-1].id)
        device = emnify.devices.device_model(
            name=name, tariff_profile=tariff_profile, status=status, service_profile=service_profile, sim=sim
        )

        emnify.devices.create_device(device=device)
