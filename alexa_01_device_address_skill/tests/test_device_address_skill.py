import logging
import json
from test_alexa_skill_base import TestAlexaSkillBase
from ask_amy.core.skill_factory import SkillFactory
import warnings
from pprint import pformat, pprint

logger = logging.getLogger()


class DeviceAddressTest(TestAlexaSkillBase):
    def setUp(self):
        BASE_DIR = ".."
        CONFIG = BASE_DIR + "/amy_dialog_model.json"
        self.dialog = SkillFactory.build(CONFIG)
        # boto3 does not close resources waits for gc cleanup
        warnings.filterwarnings("ignore", category=ResourceWarning)
        # self.dynamo_db = DynamoDB("Bolus", "http://localhost:8000")

    def test_open_device_addrees(self):
        self.logger.debug("DeviceAddressTest.test_open_device_addrees")
        # To Alexa: open device address
        request_dict, response_dict = self.get_request_response('test_open.json')
        dialog_response = self.dialog.begin(request_dict)
        pprint(dialog_response)


    def test_get_address_intent(self):
        self.logger.debug("DeviceAddressTest.test_get_address_intent")
        # To Alexa: ask what is my address
        request_dict, response_dict = self.get_request_response('test_get_address_intent.json')
        dialog_response = self.dialog.begin(request_dict)
        print(dialog_response)
