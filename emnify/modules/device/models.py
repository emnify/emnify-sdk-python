import datetime
from pydantic import BaseModel, validator
from typing import Optional, List, Dict, Any

from emnify.modules.api.models import Endpoint, Event, TariffProfile1, ServiceProfile1, Status, RetrieveEventsresponse5,\
    SubmitMTSMSrequest, RetrieveSingleEndpointresponse, UpdateEndpointrequest

from emnify.const import DeviceSortEnum


class Device(Endpoint):
    """
    Renamed generated model
    """


class CreateDevice(Device):
    """
    Custom class for validation of Device on creation
    """

    @validator("status")
    @classmethod
    def validate_status(cls, field_value, values, field, config):
        if values.get("sim") and getattr(values["sim"], "status") and values["sim"].status['id'] == 1:
            return field_value
        if field_value.id == 0:
            # If user will try activate device without sim card
            field_value.id = 1
            field_value.description = "Disabled"
        return field_value


class SmsCreateModel(SubmitMTSMSrequest):
    """
    Renamed generated model
    """
    source_address: Optional[str] = None
    source_address_type: Optional[Dict[str, Any]] = None
    expiry_date: Optional[str] = None
    udh: Optional[str] = None
    dcs: Optional[int] = None


class ListSms(RetrieveEventsresponse5):
    """
    Renamed generated model
    """


class TariffProfile(TariffProfile1):
    """
    Renamed generated model
    """


class ServiceProfile(ServiceProfile1):
    """
    Renamed generated model
    """


class DeviceStatus(Status):
    """
    Renamed generated model
    """


class DeviceIdRequired(Device):
    id: int


class QFilterDeviceListQueryParam(BaseModel):
    status: Optional[int] = None
    last_updated: Optional[datetime.datetime] = None
    created: Optional[datetime.datetime] = None
    name: Optional[str] = None
    tags: Optional[str] = None
    ip_address: Optional[str] = None
    imei: Optional[int] = None
    sim_status: Optional[int] = None


class ListQFilterDeviceListQueryParam(BaseModel):
    __root__: List[QFilterDeviceListQueryParam]


class GetDeviceFilterSet(BaseModel):
    sort: Optional[List[DeviceSortEnum]] = None
    q: Optional[ListQFilterDeviceListQueryParam] = None

    class Config:
        use_enum_values = True


class DeviceEvent(Event):
    """
    class inherited from generated Event
    """


class RetrieveDevice(RetrieveSingleEndpointresponse):
    """
    class inherited from generated model for retrieve device response
    """


class UpdateDevice(UpdateEndpointrequest):
    """
    class inherited from generated model for update device request
    """
