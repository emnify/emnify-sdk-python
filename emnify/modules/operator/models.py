import pydantic
import typing
from emnify.modules.api import models as generated_models


class TapCode(pydantic.BaseModel):
    id: int
    tapcode: str


class Mnc(pydantic.BaseModel):
    id: int
    mnc: str


class Operator(pydantic.BaseModel):
    id: int
    name: str = None
    country: generated_models.Country = None
    tapcode: typing.List[TapCode] = None
    mnc: typing.List[Mnc] = None
