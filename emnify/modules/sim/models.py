import typing
import datetime
from pydantic import BaseModel, Field, types
from emnify.modules.api.models import RetrieveSIMlistresponse, Endpoint, Sim1, Status


class SimDevice(BaseModel):
    """
    Sim list response Device  model
    """
    id: int = None
    name: str = None
    ip_address: str = None
    created: datetime.datetime = None
    last_updated: datetime.datetime = None


class IdModel(BaseModel):
    """
    BaseModel for objects with single id field
    """
    id: int


class SimStatus(BaseModel):
    id: int
    description: str = None


class SimList(RetrieveSIMlistresponse):
    """
    Inherited generated model for sim list
    """
    status: SimStatus = None
    device: typing.Optional[SimDevice] = Field(alias='endpoint')


class SimUpdate(BaseModel):
    """
    Model for sim partial update
    """
    status: SimStatus = None
    issuer_organisation: IdModel = None
    reseller_organisation: IdModel = None
    customer_organisation: IdModel = None


class SimFilter(BaseModel):
    id: int = None
    issuer_org: int = None
    reseller_org: int = None
    customer_org: int = None
    iccid: str = None
    status: id = None
    production_date: types.date = None
    imsi: str = None
    msisdn: str = None
    model: int = None
