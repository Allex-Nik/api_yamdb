from django.core.validators import RegexValidator

latin_alphanumeric_validator = RegexValidator(
    r'^[-a-zA-Z0-9_]+$',
    'Символы латинского алфавита, дефис, цифры и знак подчёркивания'
)
