import datetime
from pydantic import BaseModel
from typing import Optional, List

from emnify.modules.api.models import Endpoint, Event, TariffProfile1, ServiceProfile1, Status

from emnify.const import DeviceSortEnum


class Device(Endpoint):
    pass


class TariffProfile(TariffProfile1):
    pass


class ServiceProfile(ServiceProfile1):
    pass


class DeviceStatus(Status):
    pass


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
