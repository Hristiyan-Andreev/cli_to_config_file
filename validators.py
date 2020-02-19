from PyInquirer import Validator, ValidationError
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
        ip_regex = re.compile(r'(\d){1,3}.(\d){1,3}.(\d){1,3}.(\d){1,3}')
        # ip_regex = re.compile(r'\d')
        ip_ok = ip_regex.search(document.text)
        if not ip_ok:
            raise ValidationError(
                message='Please enter a valid IP address',
                cursor_position=len(document.text))  # Move cursor to end
