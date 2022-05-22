import datetime
from pydantic import BaseModel, validator
from typing import Optional, List, Dict, Any
from emnify.modules.sim.models import SimList
from emnify.modules.api import models as generated_models

from emnify.constants import DeviceSort


class SimDevice(generated_models.Sim1):
    status: Optional[generated_models.Status] = None


class Device(generated_models.Endpoint):
    """
    Renamed generated model
    """
    status: generated_models.Status
    sim: Optional[SimDevice] = None


class CreateDevice(Device):
    """
    Custom class for validation of Device on creation
    """

    @validator("status")
    @classmethod
    def validate_status(cls, field_value, values, field, config):
        if values.get("sim") and getattr(values["sim"], "status") and values["sim"].status.id == 1:
            return field_value
        if field_value.id == 0:
            # If user will try activate device without sim card
            field_value.id = 1
            field_value.description = "Disabled"
        return field_value


class SmsCreateModel(generated_models.SubmitMTSMSrequest):
    """
    Inherited generated model of SubmitMTSMSrequest for extra fields
    """
    source_address: Optional[str] = None
    source_address_type: Optional[Dict[str, Any]] = None
    expiry_date: Optional[str] = None
    udh: Optional[str] = None
    dcs: Optional[int] = None


class ListSms(generated_models.RetrieveEventsresponse5):
    """
    Renamed generated model
    """


class TariffProfile(generated_models.TariffProfile1):
    """
    Renamed generated model
    """


class ServiceProfile(generated_models.ServiceProfile1):
    """
    Renamed generated model
    """


class DeviceStatus(generated_models.Status):
    """
    Renamed generated model
    """


class DeviceIdRequired(Device):
    """
    Changed renamed model of Device for id validation
    """
    id: int


class QFilterDeviceListQueryParam(BaseModel):
    """
    Model for validation of filter query params
    """
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
    """
    Model for device list query params
    """
    sort: Optional[List[DeviceSort]] = None
    q: Optional[ListQFilterDeviceListQueryParam] = None

    class Config:
        use_enum_values = True


class DeviceEvent(generated_models.Event):
    """
    class inherited from generated Event
    """


class RetrieveDevice(Device):
    """
    class inherited from generated model for retrieve device response
    """
    runtime_data: Optional[Dict[str, Any]] = None
    sim: SimList = None


class UpdateDevice(generated_models.UpdateEndpointrequest):
    """
    class inherited from generated model for update device request
    """
    name: str = None
    tags: str = None
    status: generated_models.Status = None
    service_profile: Dict[str, Any] = None
    tariff_profile: Dict[str, Any] = None
    ip_address: str = None
    ip_address_space: Dict[str, Any] = None
    sim: Dict[str, Any] = None
    imei: str = None
    imei_lock: bool = None
