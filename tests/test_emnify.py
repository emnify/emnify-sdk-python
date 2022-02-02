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

    def test_device_list(self):
        emnify = emnify_client(app_token=self.token)
        devices = [i for i in emnify.devices.get_all_devices()]
        self.assertGreater(len(devices), 0)
        self.assertIsInstance(devices[0], emnify.devices.device_model)

    def test_device_endpoints_list(self):
        emnify = emnify_client(app_token=self.token)
        devices = [i for i in emnify.devices.get_all_devices()]
        device_events = [i for i in emnify.devices.get_device_events(devices[0])]
        self.assertGreater(len(device_events), 0)
        self.assertIsInstance(device_events[0], emnify.devices.event_model)

    def test_device_create(self):
        emnify = emnify_client(app_token=self.token)
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
