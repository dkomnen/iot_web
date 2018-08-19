import sys
import os

sys.path.append(os.path.abspath(os.pardir))
import unittest
from mongoengine import connect
from services import VikingService, DeviceService, UserService
from models.DeviceStatusModel import DeviceStatus
import time

mongodb_settings = {
    "db": "test_heimdall",
    "username": "",
    "password": "",
    "host": "127.0.0.1",
    "port": 27017
}

connect(mongodb_settings["db"], host=mongodb_settings["host"], port=mongodb_settings["port"])


class ServicesTest(unittest.TestCase):
    def test_viking_service_get_all(self):
        viking_service = VikingService.VikingService()
        test_object = viking_service.model(serial_number="test_SN", sensor_reading="test_SR", sensor_type="test_Type",
                                           unit="C",
                                           timestamp=time.time())
        test_object.save()
        results = viking_service.get_all()
        self.assertTrue(results[0].serial_number == "test_SN")
        # --tear down test
        test_object.delete()

    def test_viking_service_get_by_id(self):
        viking_service = VikingService.VikingService()
        test_object = viking_service.model(serial_number="test_SN", sensor_reading="test_SR", sensor_type="test_Type",
                                           unit="C",
                                           timestamp=time.time())
        test_object.save()
        results = viking_service.get_by_id(test_object.id)

        self.assertTrue(results.serial_number == "test_SN")
        # --tear down test
        test_object.delete()

    def test_device_service_get_all(self):
        service = DeviceService.DeviceService()
        test_object = service.model(serial_number="test_SN", name="test_name", device_type="test_type",
                                    status="test_status")
        test_object.save()
        results = service.get_all()
        self.assertTrue(results[0].serial_number == "test_SN")
        # --tear down test
        test_object.delete()

    def test_device_service_get_by_id(self):
        service = DeviceService.DeviceService()
        test_object = service.model(serial_number="test_SN", name="test_name", device_type="test_type",
                                    status="test_status")
        test_object.save()
        results = service.get_by_id(test_object.id)
        self.assertTrue(results.serial_number == "test_SN")
        # --tear down test
        test_object.delete()

    def test_device_service_update(self):
        service = DeviceService.DeviceService()
        test_object = service.model(serial_number="test_SN", name="test_name", device_type="test_type",
                                    status="test_status")
        test_object.save()
        results = service.update(device_id=test_object.id,
                                 data={"serial_number": "new_test_SN", "name": "new_test_name",
                                       "device_type": "new_test_type"})
        updated_object = service.model.objects(pk=test_object.id)[0]
        print updated_object
        self.assertTrue(updated_object.serial_number == "new_test_SN")
        # --tear down test
        test_object.delete()

    def test_device_get_status(self):
        test_object = DeviceStatus(status=True, serial_number="test_SN")
        test_object.save()
        results = VikingService.VikingService().get_devices_status()
        self.assertTrue(results[0]["status"] is True)
        # --tear down test
        test_object.delete()

    def test_user_service_get_all(self):
        service = UserService.UserService()
        test_object = service.model(email="testemail@email.com", password="testpass", active=True, roles=[], devices=[])
        test_object.save()
        results = service.get_all()
        self.assertTrue(results[0].email == "testemail@email.com")
        # --tear down test
        test_object.delete()

    def test_user_service_get_by_id(self):
        service = UserService.UserService()
        test_object = service.model(email="testemail@email.com", password="testpass", active=True, roles=[], devices=[])

        test_object.save()
        results = service.get_by_id(test_object.id)
        self.assertTrue(results.email == "testemail@email.com")
        # --tear down test
        test_object.delete()


if __name__ == '__main__':
    unittest.main()
