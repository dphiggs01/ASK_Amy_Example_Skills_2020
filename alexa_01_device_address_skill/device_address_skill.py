from ask_amy.state_mgr.stack_dialog_mgr import StackDialogManager
from ask_amy.core.reply import Reply
from ask_amy.services.address_service import AddressService
from ask_amy.utilities.us_states import USSateNamesUtility
import logging
import json
logger = logging.getLogger()

class DeviceAddressSkill(StackDialogManager):
    def launch_request(self):
        logger.debug("**************** entering {}.launch_request".format(self.__class__.__name__))
        self._intent_name = 'welcome_request'
        reply_dialog = self.reply_dialog[self.intent_name]
        reply = Reply.build(reply_dialog, self.event)
        # logger.debug("Reply=={}".format(json.dumps(reply, sort_keys=True, indent=4)))
        return reply

    def get_address_intent(self):
        logger.debug("**************** entering {}.{}".format(self.__class__.__name__, self.intent_name))
        permissions = self.context.system.consent_token
        if not permissions:
            # The app does not have permissions
            condition = 'no_permissions'
        else:
            address_service = AddressService()
            address_response = address_service.get_full_address(self.context.system.api_endpoint,
                                                                self.context.system.device_id,
                                                                self.context.system.api_access_token)
            if address_response['status_cd'] == 200:
                address = address_response['body']

                # We should check if we have all the data we need
                if 'addressLine1' in address and address['addressLine1'] is not None:
                    condition = 'address_found'
                    self.request.attributes['address_line1'] = address['addressLine1']
                    self.request.attributes['city'] = address['city']
                    state_nm = USSateNamesUtility.state_nm_for_cd(address['stateOrRegion'])
                    self.request.attributes['state'] = state_nm
                else:
                    condition = 'address_found_with_no_data'
            else:
                condition = 'address_not_found'
                self.session.attributes['status_cd'] = address_response['status_cd']
                self.session.attributes['reason'] = address_response['reason']


        reply_dialog = self.reply_dialog[self.intent_name]['conditions'][condition]

        return Reply.build(reply_dialog, self.event)

    def navigate_home_intent(self):
        logger.debug("**************** entering {}.{}".format(self.__class__.__name__, self.intent_name))
        return self.handle_default_intent()

