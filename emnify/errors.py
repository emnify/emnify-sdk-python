# Custom Exceptions

__all__ = ['UnauthorisedException', 'JsonDecodeException', 'UnexpectedArgumentException']


class UnauthorisedException(Exception):
    """Custom error for unauthorised response"""


class JsonDecodeException(Exception):
    """Custom error for json parse exception"""


class UnexpectedArgumentException(Exception):
    """Custom error for unexpected arguments"""
