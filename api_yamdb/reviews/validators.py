from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils import timezone

latin_alphanumeric_validator = RegexValidator(
    r'^[-a-zA-Z0-9_]+$',
    'Символы латинского алфавита, дефис, цифры и знак подчёркивания'
)


def year_validator(value):
    if value > timezone.now().year:
        raise ValidationError(
            'Год выпуска не может быть больше текущего'
        )
