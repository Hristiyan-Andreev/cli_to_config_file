from PyInquirer import Validator, ValidationError
import ipaddress as ip
import regex as re


class AvDurValidator(Validator):
    def validate(self, document):
        try:
            float(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number (float or int)',
                cursor_position=len(document.text)
                )

class IpValidator(Validator):
    def validate(self, document):
        # ip_regex = re.compile(r'(\d){1,3}\.(\d){1,3}\.(\d){1,3}\.(\d){1,3}')
        # ip_pattern = '^(\d){1,3}\.(\d){1,3}\.(\d){1,3}\.(\d){1,3}$'
        # ip_pattern = '^([0-9]|[0-5]|[0-5]){1,3}\.([0-255]){1,3}\.([0-255]){1,3}\.([0-255]){1,3}$'
        # ip_ok = re.match(ip_pattern, document.text)
        
        try:
            ip.ip_address(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a valid IP address',
                cursor_position=len(document.text))  # Move cursor to end
