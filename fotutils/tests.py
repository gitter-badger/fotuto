from django.core.exceptions import ValidationError
from django.test import TestCase


class ModelTestHelper(TestCase):
    """Abstract class with helper methods for test models."""

    def check_save_validation(self, model, field_name, error_key='blank'):
        """
        Checks for raise Empty field Validation exception on save model.

        :param model: Model to save
        :param field_name: Model attribute to check empty
        :param error_key: Key in error message
        """
        if error_key == 'unique':
            exception_message = "{'%s': [u'%s with this %s already exists.']}" % (
                field_name, model.__class__.__name__, field_name.capitalize()
            )
        else:
            exception_message = "{'%s': [u'This field cannot be %s.']}" % (field_name, error_key)
        with self.assertRaisesMessage(ValidationError, exception_message):
            model.full_clean()
            model.save()
