# Custom Exceptions

__all__ = ['UnauthorisedException', 'JsonDecodeException', 'UnexpectedArgumentException']

# What if create general EMnifySDK error and inherit other errors from it. So that users can catch specific error if they need.
class UnauthorisedException(Exception):
    """Custom error for unauthorised response"""


class JsonDecodeException(Exception):
    """Custom error for json parse exception"""


class UnexpectedArgumentException(Exception):
    """Custom error for unexpected arguments"""
