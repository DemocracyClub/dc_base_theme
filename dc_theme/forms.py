import datetime

from django.core.exceptions import ValidationError

from django import forms
from . import widgets


class DCHeaderField(forms.Field):
    """
    A field that is just rendered as a heading.
    """

    def __init__(self, *args, **kwargs):
        kwargs["required"] = False
        super().__init__(*args, **kwargs)


class DCDateField(forms.MultiValueField):

    widget = widgets.DayMonthYearWidget

    def __init__(self, *args, **kwargs):
        # Define one message for all fields.
        error_messages = {
            "incomplete": "Enter a country calling code and a phone number.",
        }

        fields = (
            forms.CharField(),
            forms.CharField(),
            forms.CharField(),
        )

        super().__init__(
            error_messages=error_messages,
            fields=fields,
            require_all_fields=True,
            *args,
            **kwargs
        )
        self.field_class = "form-date"

    def compress(self, data_list):
        data_list = list(data_list)
        data_list.reverse()
        return datetime.datetime(*map(int, data_list))

    def clean(self, *args, **kwargs):
        try:
            super().clean(*args, **kwargs)
            return self.compress(*args)
        except ValueError as e:
            raise ValidationError(e)
