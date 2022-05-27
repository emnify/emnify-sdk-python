# Custom Exceptions

__all__ = [
    'EMnifyBaseException',
    'UnauthorisedException',
    'JsonDecodeException',
    'UnexpectedArgumentException',
    'ValidationErrorException'
]


class EMnifyBaseException(Exception):
    """Cumstom base error class"""


class UnauthorisedException(EMnifyBaseException):
    """Custom error for unauthorised response"""


class JsonDecodeException(EMnifyBaseException):
    """Custom error for json parse exception"""


class UnexpectedArgumentException(EMnifyBaseException):
    """Custom error for unexpected arguments"""


class ValidationErrorException(EMnifyBaseException):
    """Custom error for validation errors"""


class UnknownStatusCodeException(EMnifyBaseException):
    """Custom error for unknown response errors"""
