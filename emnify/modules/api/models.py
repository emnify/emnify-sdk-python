# api by datamodel-codegen:
#   filename:  new_enterprise.yaml
#   timestamp: 2022-01-11T23:18:41+00:00

from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field, SecretStr, conint, constr


class Authentication(BaseModel):
    application_token: Optional[str] = None
    username: Optional[str] = None
    password: Optional[SecretStr] = None
    refresh_token: Optional[str] = None


class AuthenticationResponse(BaseModel):
    auth_token: Optional[str] = None
    refresh_token: Optional[str] = None


class Auth404Response(BaseModel):
    error_code: Optional[float] = None
    error_token: Optional[str] = None
    message: Optional[str] = None


class Field40xResponse(BaseModel):
    error_code: Optional[int] = None
    error_token: Optional[str] = None
    message: Optional[str] = None


class ChangeQuota422Response(BaseModel):
    message: Optional[str] = None


class Status(BaseModel):
    id: Optional[float] = None
    description: Optional[str] = None


class Type(BaseModel):
    id: Optional[float] = None
    description: Optional[str] = None


class CreateMFAResponse(BaseModel):
    id: Optional[float] = None
    status: Optional[Status] = None
    type: Optional[Type] = None
    secret_key: Optional[str] = None
    otpauth: Optional[str] = None
    creation_date: Optional[str] = None


class Status1(BaseModel):
    id: Optional[float] = None
    code: Optional[float] = None


class ActivateMFAKeyRequest(BaseModel):
    status: Optional[Status1] = None


class Country(BaseModel):
    name: Optional[str] = None
    country_code: Optional[int] = None
    mcc: Optional[str] = None
    iso_code: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    id: Optional[int] = None


class Error(BaseModel):
    code: str
    message: str


class SimpleError(BaseModel):
    message: str


class APICallback(BaseModel):
    organisation_id: Optional[str] = None
    url: Optional[str] = None
    created: Optional[datetime] = None
    purpose: Optional[str] = None
    id: Optional[int] = None


class CallbackSecret(BaseModel):
    organisation_id: Optional[str] = None
    purpose: Optional[str] = None
    id: Optional[int] = None


class ApiType(BaseModel):
    description: Optional[str] = None
    id: Optional[int] = None


class DataStreamType(BaseModel):
    description: Optional[str] = None
    id: Optional[int] = None


class DataStream(BaseModel):
    last_traffic_log_id: Optional[int] = None
    last_event_id: Optional[str] = None
    last_dispatched_timestamp: Optional[datetime] = None
    last_result_code: Optional[str] = None
    active: Optional[int] = None
    running: Optional[int] = None
    id: Optional[int] = None
    api_callback: Optional[str] = None
    api_type: Optional[ApiType] = None
    data_stream_type: Optional[DataStreamType] = None


class DataStreamType1(BaseModel):
    description: Optional[str] = None
    id: Optional[int] = None


class ApiType1(BaseModel):
    description: Optional[str] = None
    id: Optional[int] = None
    route: Optional[str] = None
    reqParams: Optional[str] = None
    fromServer: Optional[bool] = None
    parentResource: Optional[str] = None
    restangularCollection: Optional[bool] = None


class ApiCallback(BaseModel):
    organisation_id: Optional[str] = None
    url: Optional[str] = None
    created: Optional[datetime] = None
    purpose: Optional[str] = None
    id: Optional[int] = None
    route: Optional[str] = None
    reqParams: Optional[str] = None
    fromServer: Optional[bool] = None
    parentResource: Optional[str] = None
    restangularCollection: Optional[bool] = None


class CreateDataStream(BaseModel):
    stream_historic_data: Optional[int] = None
    data_stream_type: Optional[DataStreamType1] = None
    api_type: Optional[ApiType1] = None
    api_callback: Optional[ApiCallback] = None
    event_stream: Optional[str] = None
    api_username: Optional[str] = None
    api_password: Optional[str] = None
    api_parameter: Optional[str] = None


class TrafficType(BaseModel):
    description: Optional[str] = None
    unit: Optional[str] = None
    id: Optional[float] = None


class Currency(BaseModel):
    code: Optional[str] = None
    symbol: Optional[str] = None
    id: Optional[float] = None


class Data(BaseModel):
    sim_id: Optional[float] = None
    month: Optional[date] = None
    volume: Optional[float] = None
    volume_tx: Optional[float] = None
    volume_rx: Optional[float] = None
    traffic_type_id: Optional[float] = None
    last_updated: Optional[datetime] = None
    cost: Optional[float] = None
    currency_id: Optional[float] = None
    id: Optional[float] = None
    traffic_type: Optional[TrafficType] = None
    currency: Optional[Currency] = Field(None, title='Currency')


class TrafficType1(BaseModel):
    description: Optional[str] = None
    unit: Optional[str] = None
    id: Optional[float] = None


class Currency1(BaseModel):
    code: Optional[str] = None
    symbol: Optional[str] = None
    id: Optional[float] = None


class Sms(BaseModel):
    sim_id: Optional[float] = None
    month: Optional[date] = None
    volume: Optional[float] = None
    volume_tx: Optional[float] = None
    volume_rx: Optional[float] = None
    traffic_type_id: Optional[float] = None
    last_updated: Optional[datetime] = None
    cost: Optional[float] = None
    currency_id: Optional[float] = None
    id: Optional[float] = None
    traffic_type: Optional[TrafficType1] = None
    currency: Optional[Currency1] = Field(None, title='Currency')


class LastMonth(BaseModel):
    data: Optional[Data] = None
    sms: Optional[Sms] = None


class SIMStatsResponseObject(BaseModel):
    last_month: LastMonth
    current_month: Dict[str, Any]
    last_hour: Dict[str, Any]


class TrafficType2(BaseModel):
    description: Optional[str] = None
    unit: Optional[str] = None
    id: Optional[float] = None


class Currency2(BaseModel):
    code: Optional[str] = None
    symbol: Optional[str] = None
    id: Optional[float] = None


class Sms1(BaseModel):
    sim_id: Optional[float] = None
    month: Optional[date] = None
    volume: Optional[float] = None
    volume_tx: Optional[float] = None
    volume_rx: Optional[float] = None
    traffic_type_id: Optional[float] = None
    last_updated: Optional[datetime] = None
    cost: Optional[float] = None
    currency_id: Optional[float] = None
    id: Optional[float] = None
    traffic_type: Optional[TrafficType2] = None
    currency: Optional[Currency2] = Field(None, title='Currency')


class StatsResponseObject(BaseModel):
    date: Optional[str] = None
    data: Optional[Dict[str, Any]] = None
    sms: Optional[Sms1] = None


class TrafficType3(BaseModel):
    description: Optional[str] = None
    unit: Optional[str] = None
    id: Optional[float] = None


class Currency3(BaseModel):
    code: Optional[str] = None
    symbol: Optional[str] = None
    id: Optional[float] = None


class Data1(BaseModel):
    sim_id: Optional[float] = None
    month: Optional[date] = None
    volume: Optional[float] = None
    volume_tx: Optional[float] = None
    volume_rx: Optional[float] = None
    traffic_type_id: Optional[float] = None
    last_updated: Optional[datetime] = None
    cost: Optional[float] = None
    currency_id: Optional[float] = None
    id: Optional[float] = None
    traffic_type: Optional[TrafficType3] = None
    currency: Optional[Currency3] = Field(None, title='Currency')


class TrafficType4(BaseModel):
    description: Optional[str] = None
    unit: Optional[str] = None
    id: Optional[float] = None


class Currency4(BaseModel):
    code: Optional[str] = None
    symbol: Optional[str] = None
    id: Optional[float] = None


class Sms2(BaseModel):
    sim_id: Optional[float] = None
    month: Optional[date] = None
    volume: Optional[float] = None
    volume_tx: Optional[float] = None
    volume_rx: Optional[float] = None
    traffic_type_id: Optional[float] = None
    last_updated: Optional[datetime] = None
    cost: Optional[float] = None
    currency_id: Optional[float] = None
    id: Optional[float] = None
    traffic_type: Optional[TrafficType4] = None
    currency: Optional[Currency4] = Field(None, title='Currency')


class SIMStatsDataObject(BaseModel):
    data: Optional[Data1] = None
    sms: Optional[Sms2] = None


class TrafficType5(BaseModel):
    description: Optional[str] = None
    unit: Optional[str] = None
    id: Optional[float] = None


class Currency5(BaseModel):
    code: Optional[str] = None
    symbol: Optional[str] = None
    id: Optional[float] = None


class TrafficStatsObject(BaseModel):
    sim_id: Optional[float] = None
    month: Optional[date] = None
    volume: Optional[float] = None
    volume_tx: Optional[float] = None
    volume_rx: Optional[float] = None
    traffic_type_id: Optional[float] = None
    last_updated: Optional[datetime] = None
    cost: Optional[float] = None
    currency_id: Optional[float] = None
    id: Optional[float] = None
    traffic_type: Optional[TrafficType5] = None
    currency: Optional[Currency5] = Field(None, title='Currency')


class TrafficTypeObject(BaseModel):
    description: Optional[str] = None
    unit: Optional[str] = None
    id: Optional[float] = None


class CurrencyObject(BaseModel):
    code: Optional[str] = None
    symbol: Optional[str] = None
    id: Optional[float] = None


class TrafficType6(BaseModel):
    description: Optional[str] = None
    unit: Optional[str] = None
    id: Optional[float] = None


class Data2(BaseModel):
    volume: Optional[float] = None
    volume_tx: Optional[float] = None
    volume_rx: Optional[float] = None
    cost: Optional[float] = None
    traffic_type: Optional[TrafficType6] = None
    currency: Optional[str] = None


class TrafficType7(BaseModel):
    description: Optional[str] = None
    unit: Optional[str] = None
    id: Optional[float] = None


class Sms3(BaseModel):
    volume: Optional[float] = None
    volume_tx: Optional[float] = None
    volume_rx: Optional[float] = None
    cost: Optional[float] = None
    traffic_type: Optional[TrafficType7] = None
    currency: Optional[str] = None


class StatsObjectItem(BaseModel):
    date: Optional[date] = None
    data: Optional[Data2] = None
    sms: Optional[Sms3] = None


class StatsObject(BaseModel):
    __root__: List[StatsObjectItem] = Field(
        ..., title='Response schema for Endpoint and Organisation Statistics'
    )


class TrafficType8(BaseModel):
    description: Optional[str] = None
    unit: Optional[str] = None
    id: Optional[float] = None


class VolumeObject(BaseModel):
    volume: Optional[float] = None
    volume_tx: Optional[float] = None
    volume_rx: Optional[float] = None
    cost: Optional[float] = None
    traffic_type: Optional[TrafficType8] = None
    currency: Optional[str] = None


class Country1(BaseModel):
    name: Optional[str] = None
    country_code: Optional[int] = None
    mcc: Optional[float] = None
    iso_code: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    id: Optional[int] = None


class SmppBind(BaseModel):
    system_id: Optional[str] = None
    smpp_bind_status_id: Optional[str] = None
    id: Optional[int] = None


class Country2(BaseModel):
    name: Optional[str] = None
    country_code: Optional[int] = None
    mcc: Optional[float] = None
    iso_code: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    id: Optional[int] = None


class Operator(BaseModel):
    country_id: Optional[str] = None
    name: Optional[str] = None
    country_name: Optional[str] = None
    id: Optional[int] = None
    country: Optional[Country2] = None
    tapcodes: Optional[str] = None
    mncs: Optional[str] = None


class MsisdnPool(BaseModel):
    resource_provider_id: Optional[str] = None
    description: Optional[str] = None
    id: Optional[int] = None


class GtConfig(BaseModel):
    imsi_prefix: Optional[str] = None
    calling_party: Optional[str] = None
    called_party_tt: Optional[str] = None
    id: Optional[int] = None


class SccpCalledPartyPrefix(BaseModel):
    prefix: Optional[str] = None
    tt: Optional[str] = None
    id: Optional[int] = None


class SmsRoutingData(BaseModel):
    id: Optional[float] = None
    sms_routing_id: Optional[str] = None
    country: Optional[Country1] = None
    smpp_bind: Optional[SmppBind] = None
    operator: Optional[Operator] = None
    msisdn_pool: Optional[MsisdnPool] = None
    gt_config: Optional[GtConfig] = None
    sccp_called_party_prefix: Optional[SccpCalledPartyPrefix] = None


class RatType(BaseModel):
    id: Optional[float] = None
    description: Optional[str] = None


class ListofSMSresponse(BaseModel):
    submit_date: Optional[str] = Field(None, example='10/5/2019 1:56:59 PM')
    delivery_date: Optional[str] = Field(None, example='10/5/2019 1:56:59 PM')
    expiry_date: Optional[str] = Field(None, example='10/6/2019 1:56:59 PM')
    final_date: Optional[str] = Field(None, example='10/5/2019 1:57:03 PM')
    retry_date: Optional[str] = None
    last_delivery_attempt: Optional[str] = Field(None, example='10/5/2019 1:57:00 PM')
    retry_count: Optional[str] = Field(None, example=0)
    gsm_map_error: Optional[str] = None
    dcs: Optional[int] = Field(None, example=0)
    pid: Optional[int] = Field(None, example=0)
    source_address: Optional[str] = Field(None, example=1234567890)
    endpoint: Optional[Dict[str, Any]] = Field(
        None, example={'id': 166, 'name': 'Your Endpoint'}
    )
    sim_id: Optional[str] = Field(None, example=625)
    iccid: Optional[str] = Field(None, example=8988303000000001000)
    msisdn: Optional[str] = Field(None, example='883XXXXXXXXXXXX')
    imsi: Optional[str] = Field(None, example='901XXXXXXXXXXXX')
    msc: Optional[str] = Field(None, example=491600190000)
    udh: Optional[str] = None
    payload: Optional[str] = Field(None, example='test')
    id: Optional[int] = Field(None, example=590)
    status: Optional[Dict[str, Any]] = Field(
        None, example={'description': 'DELIVERED', 'id': 4}
    )
    sms_type: Optional[Dict[str, Any]] = Field(
        None, example={'description': 'MT', 'id': 1}
    )
    source_address_type: Optional[Dict[str, Any]] = Field(
        None, example={'description': 'National', 'id': 161}
    )


class SubmitMTSMSrequest(BaseModel):
    source_address: str
    payload: str


class GetdetailsofSMSresponse(BaseModel):
    submit_date: Optional[str] = None
    delivery_date: Optional[str] = None
    expiry_date: Optional[str] = None
    final_date: Optional[str] = None
    retry_date: Optional[str] = None
    last_delivery_attempt: Optional[str] = None
    retry_count: Optional[str] = None
    gsm_map_error: Optional[str] = None
    dcs: Optional[int] = None
    pid: Optional[int] = None
    source_address: Optional[str] = None
    endpoint: Optional[Dict[str, Any]] = None
    sim_id: Optional[str] = None
    iccid: Optional[str] = None
    msisdn: Optional[str] = None
    imsi: Optional[str] = None
    msc: Optional[str] = None
    udh: Optional[str] = None
    payload: Optional[str] = None
    id: Optional[int] = None
    status: Optional[Dict[str, Any]] = None
    sms_type: Optional[Dict[str, Any]] = None
    source_address_type: Optional[Dict[str, Any]] = None


class RetrieveConnectivityInformationresponse(BaseModel):
    ussd_info: Optional[Dict[str, Any]] = None
    subscriber_info: Optional[Dict[str, Any]] = None
    request_timestamp: Optional[str] = None
    reply_timestamp: Optional[str] = None


class OperatorPatchRequest(BaseModel):
    __root__: Any = Field(
        ...,
        example={'name': 'Zulu, New Operator Name'},
        title='Example request body to update Operator details',
    )


class OperatorDataPostRequest(BaseModel):
    __root__: Any = Field(
        ...,
        example={'mnc': '99'},
        title='Example request body to update Operator Related Data',
    )


class RetrieveOperatorBlacklistresponse(BaseModel):
    id: Optional[int] = Field(None, example=1)
    name: Optional[str] = Field(None, example='Telekom')
    country: Optional[Dict[str, Any]] = Field(
        None,
        example={
            'id': 74,
            'name': 'Germany',
            'country_code': 49,
            'mcc': 262,
            'iso_code': 'de',
        },
    )
    tapcode: Optional[List[Dict[str, Any]]] = Field(None, description='')
    mnc: Optional[List[Dict[str, Any]]] = Field(None, description='')


class RetrievePrepaidBalanceresponse(BaseModel):
    amount: Optional[float] = None
    currency: Optional[Dict[str, Any]] = None
    last_updated: Optional[str] = None
    expiry_date: Optional[str] = None


class UpdatePrepaidBalanceresponse(BaseModel):
    amount: Optional[int] = None
    currency: Optional[Dict[str, Any]] = None
    expiry_date: Optional[str] = None


class Description(Enum):
    EXHAUSTED = 'EXHAUSTED'
    ACTIVE = 'ACTIVE'
    EXPIRED = 'EXPIRED'


class Id(Enum):
    integer_1 = 1
    integer_2 = 2
    integer_3 = 3


class Status2(BaseModel):
    description: Optional[Description] = None
    id: Id


class Id1(Enum):
    integer_1 = 1
    integer_2 = 2


class Description1(Enum):
    Throttle = 'Throttle'
    Block = 'Block'


class ActionOnExhaustion(BaseModel):
    id: Id1
    description: Optional[Description1] = None
    peak_throughput: Optional[int] = None


class EndpointQuota(BaseModel):
    last_volume_added: Optional[float] = None
    last_status_change_date: Optional[
        constr(regex=r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$')
    ] = None
    auto_refill: Optional[int] = None
    threshold_volume: Optional[float] = None
    threshold_percentage: Optional[float] = None
    status: Status2 = Field(..., title='QuotaStatus')
    volume: float
    expiry_date: constr(regex=r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$')
    action_on_exhaustion: ActionOnExhaustion = Field(..., title='ActionOnExhaustion')
    peak_throughput: Optional[int] = None


class ThrottleCutoffVolume(BaseModel):
    id: float
    volume: Optional[float] = None


class Id2(Enum):
    integer_1 = 1
    integer_2 = 2


class Description2(Enum):
    Throttle = 'Throttle'
    Block = 'Block'


class ActionOnExhaustion1(BaseModel):
    id: Id2
    description: Optional[Description2] = None
    peak_throughput: Optional[int] = None


class Description3(Enum):
    EXHAUSTED = 'EXHAUSTED'
    ACTIVE = 'ACTIVE'
    EXPIRED = 'EXPIRED'


class Id3(Enum):
    integer_1 = 1
    integer_2 = 2
    integer_3 = 3


class QuotaStatus(BaseModel):
    description: Optional[Description3] = None
    id: Id3


class SMSQuota(BaseModel):
    volume: float
    expiry_date: datetime
    last_volume_added: Optional[float] = None
    last_status_change_date: Optional[datetime] = None
    auto_refill: Optional[bool] = None
    threshold_percentage: float
    threshold_volume: Optional[float] = None
    status: QuotaStatus
    action_on_exhaustion: Optional[ActionOnExhaustion1] = None


class RetrieveEventsresponse(BaseModel):
    timestamp: Optional[str] = Field(None, example='2020-03-01T12:07:09.000Z')
    alert: Optional[bool] = Field(None, example=True)
    description: Optional[str] = Field(None, example='PDP Context deleted.')
    id: Optional[int] = Field(None, example=69535)
    event_type: Optional[Dict[str, Any]] = Field(
        None, example={'description': 'Delete PDP Context', 'id': 4}
    )
    event_source: Optional[Dict[str, Any]] = Field(
        None, example={'name': 'Network', 'id': 0}
    )
    event_severity: Optional[Dict[str, Any]] = Field(
        None, example={'description': 'INFO', 'id': 0}
    )
    organisation: Optional[Dict[str, Any]] = Field(
        None, example={'name': 'Organisation_Name', 'id': 2}
    )
    endpoint: Optional[Dict[str, Any]] = Field(
        None,
        example={
            'name': 'Monitoring201',
            'tags': 'Monitoring',
            'ip_address': '0.0.0.0',
            'imei': None,
            'id': 1,
        },
    )
    sim: Optional[Dict[str, Any]] = Field(
        None,
        example={
            'iccid': 10000000000,
            'production_date': '2019-12-17T13:26:13.000Z',
            'id': 1,
        },
    )
    imsi: Optional[Dict[str, Any]] = Field(
        None,
        example={
            'imsi': 100000000000000,
            'import_date': '2019-12-17T13:26:08.000Z',
            'id': 110,
        },
    )


class StartingaUSSDDialogrequest(BaseModel):
    ussd_begin: Dict[str, Any] = Field(..., alias='ussd-begin')


class StartingaUSSDDialogresponse(BaseModel):
    session_id: Optional[str] = Field(None, alias='session-id')


class RetrieveOrganisationListresponse(BaseModel):
    id: int = Field(..., example=12)
    name: str = Field(..., example='Tele17')
    class_: Dict[str, Any] = Field(
        ..., alias='class', example={'id': 0, 'description': 'Commercial'}
    )
    type: Dict[str, Any] = Field(..., example={'id': 1, 'description': 'Provider'})
    country: Dict[str, Any] = Field(
        ...,
        example={
            'id': 74,
            'name': 'Germany',
            'mcc': 262,
            'country_code': 49,
            'isocode': 'de',
        },
    )
    status: Dict[str, Any] = Field(..., example={'id': 0, 'description': 'Enabled'})
    relation: Dict[str, Any] = Field(
        ..., example={'id': 17, 'type': {'id': 2, 'description': 'Roaming Partner'}}
    )
    monthly_cost_limit: int = Field(..., example=1000)
    currency: Dict[str, Any] = Field(
        ..., example={'id': 1, 'code': 'EUR'}
    )
    created: str = Field(..., example='2/3/2019 12:00:00 AM')
    verification_type: Dict[str, Any] = Field(
        ..., example={'id': 1, 'description': 'Business registration number'}
    )
    verification: str = Field(..., example=123456789)


class CreateanOrganisationrequest(BaseModel):
    name: str
    class_: Dict[str, Any] = Field(..., alias='class')
    type: Dict[str, Any]
    country: Dict[str, Any]
    status: Dict[str, Any]
    relation: Dict[str, Any]
    currency: Dict[str, Any]
    verification_type: Dict[str, Any]
    verification: str
    ext_reference: str
    monthly_cost_limit: int


class RetrieveaSingleOrganisationresponse(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    class_: Optional[Dict[str, Any]] = Field(None, alias='class')
    type: Optional[Dict[str, Any]] = None
    country: Optional[Dict[str, Any]] = None
    status: Optional[Dict[str, Any]] = None
    relation: Optional[Dict[str, Any]] = None
    monthly_cost_limit: Optional[int] = None
    currency: Optional[Dict[str, Any]] = None
    created: Optional[str] = None
    verification_type: Optional[Dict[str, Any]] = None
    verification: Optional[str] = None


class UpdateOrganisationrequest(BaseModel):
    name: str
    class_: Dict[str, Any] = Field(..., alias='class')
    type: Dict[str, Any]
    country: Dict[str, Any]
    status: Dict[str, Any]
    ext_reference: str
    monthly_cost_limit: int
    currency: Dict[str, Any]
    verification_type: Dict[str, Any]
    verification: str


class RetrieveOrganisationStatusesresponse(BaseModel):
    id: Optional[int] = Field(None, example=0)
    description: Optional[str] = Field(None, example='Enabled')


class RetrieveAvailableOrganisationTypesresponse(BaseModel):
    id: Optional[int] = Field(None, example=1)
    description: Optional[str] = Field(None, example='Mobile Network Operator')


class RetrieveAvailableOrganisationRelationTypesresponse(BaseModel):
    id: Optional[int] = Field(None, example=0)
    description: Optional[str] = Field(None, example='Customer of')


class RetrieveAvailableOrganisationVerificationTypesresponse(BaseModel):
    id: Optional[int] = Field(None, example=1)
    description: Optional[str] = Field(None, example='Business registration number')


class RetrieveContactsforanOrganisationresponse(BaseModel):
    id: Optional[int] = Field(None, example=1)
    organisation: Optional[Dict[str, Any]] = Field(
        None, example={'id': 124, 'name': 'Tele17 Austria'}
    )
    type: Optional[Dict[str, Any]] = Field(
        None, example={'id': 1, 'description': 'Commercial'}
    )
    name: Optional[str] = Field(None, example='Marc Muller')
    title: Optional[str] = Field(None, example='Ing')
    department: Optional[str] = Field(None, example='Sales')
    street: Optional[str] = Field(None, example='1st street')
    zipcode: Optional[str] = Field(None, example=10224)
    city: Optional[str] = Field(None, example='Berlin')
    country: Optional[Dict[str, Any]] = Field(
        None, example={'id': 1, 'name': 'Germany'}
    )
    email: Optional[str] = Field(None, example='user@domain.com')
    phone: Optional[str] = Field(None, example='+497 554 776 653')
    mobile: Optional[str] = Field(None, example='+497 554 776 653')
    state: Optional[str] = None
    secondary_address: Optional[str] = None


class CreateaContactforanOrganisationrequest(BaseModel):
    type: Dict[str, Any]
    name: str
    title: str
    department: str
    street: str
    zipcode: str
    city: str
    country: Dict[str, Any]
    email: str
    phone: str
    mobile: str
    state: Optional[str] = None
    secondary_address: Optional[str] = None


class RetrieveaSingleContactresponse(BaseModel):
    id: Optional[int] = None
    organisation: Optional[Dict[str, Any]] = None
    type: Optional[Dict[str, Any]] = None
    name: Optional[str] = None
    title: Optional[str] = None
    department: Optional[str] = None
    street: Optional[str] = None
    zipcode: Optional[str] = None
    city: Optional[str] = None
    country: Optional[Dict[str, Any]] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    mobile: Optional[str] = None
    state: Optional[str] = None
    secondary_address: Optional[str] = None


class UpdateaSingleContactresponse(BaseModel):
    type: Optional[Dict[str, Any]] = None
    name: Optional[str] = None
    title: Optional[str] = None
    department: Optional[str] = None
    street: Optional[str] = None
    zipcode: Optional[str] = None
    city: Optional[str] = None
    country: Optional[Dict[str, Any]] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    mobile: Optional[str] = None


class Retrievelistofassignedtariffsforanorganisationresponse(BaseModel):
    id: Optional[int] = Field(None, example=3)
    name: Optional[str] = Field(None, example='Tariff for M2M Europe')
    description: Optional[str] = Field(None, example='M2M Europe: Data+SMS')
    created: Optional[str] = Field(None, example='2019-01-10T09:36:58.000Z')
    default_sms_mt_rate: Optional[float] = Field(None, example=0.5)
    default_sms_mo_rate: Optional[float] = Field(None, example=0.4)
    sim_issued_rate: Optional[float] = Field(None, example=0.1)
    sim_activated_rate: Optional[float] = Field(None, example=0.2)
    sim_suspended_rate: Optional[float] = Field(None, example=0.3)
    sim_activation_rate: Optional[float] = Field(None, example=0.6)
    sim_reactivation_rate: Optional[float] = Field(None, example=0.8)
    sim_suspension_rate: Optional[float] = Field(None, example=0.7)
    sim_termination_rate: Optional[float] = Field(None, example=0.5)
    status: Optional[Dict[str, Any]] = Field(
        None, example={'description': 'Active', 'id': 1}
    )
    currency: Optional[Dict[str, Any]] = Field(
        None, example={'id': 1, 'code': 'EUR', 'symbol': '�'}
    )
    data_blocksize: Optional[Dict[str, Any]] = Field(
        None, example={'id': 10, 'octets': 1, 'description': 'exact'}
    )
    data_throttle: Optional[Dict[str, Any]] = Field(
        None, example={'id': 9, 'octets': 256000, 'description': '256 kbit/s'}
    )
    pdp_context_definition: Optional[List[Dict[str, Any]]] = Field(None, description='')


class RetrieveBillingPeriodsresponse(BaseModel):
    id: Optional[int] = Field(None, example=201810)
    description: Optional[str] = Field(None, example='October 2018')


class RetrieveBillingDataByPeriodResponse(BaseModel):
    __root__: Any = Field(
        ...,
        example={
            'mrc': {
                'data_packages': {
                    'data': [
                        {
                            'tariff': {'id': 64, 'name': 'Global Pro I'},
                            'ratezone': {'id': 84, 'name': 'Europe_II'},
                            'currency': {'id': 1, 'code': 'EUR', 'symbol': '�'},
                            'id': 83,
                            'volume': 500,
                            'rate': 112.81,
                            'description': 'Monthly Payment',
                        },
                        {
                            'tariff': {'id': 64, 'name': 'Global Pro I'},
                            'ratezone': {'id': 83, 'name': 'Europe_I'},
                            'currency': {'id': 1, 'code': 'EUR', 'symbol': '�'},
                            'id': 115,
                            'volume': 700,
                            'rate': 146.25,
                            'description': 'Monthly Payment',
                        },
                    ],
                    'total': {
                        'cost': 259.06,
                        'volume': 1200,
                        'currency': {'id': 1, 'code': 'EUR', 'symbol': '�'},
                    },
                }
            },
            'sim_items': {
                'total': {
                    'number_of_active_sims_chargeable': 48,
                    'sim_hosting_fees': 0,
                    'cost': 0,
                },
                'data': [],
            },
            'traffic': {
                'data': {
                    'tariff': [
                        {
                            'volume': '30.209802',
                            'cost': 0,
                            'currency': {'code': 'EUR'},
                            'id': 64,
                            'name': 'Global Pro I',
                            'ratezone': [
                                {
                                    'countries': [
                                        {
                                            'volume': '30.209802',
                                            'cost': '7.5524505000',
                                            'ratezone': 'Europe_I',
                                            'ratezone_id': '83',
                                            'rate': '0.250000',
                                            'currency': {'code': 'EUR'},
                                            'country': {'name': 'Germany'},
                                        }
                                    ],
                                    'volume': '30.209802',
                                    'data_package_volume': 700,
                                    'cost': 0,
                                    'name': 'Europe_I',
                                    'id': 83,
                                    'tariff': 'Global Pro I',
                                    'rate': '0.250000',
                                    'currency': {'code': 'EUR'},
                                    'inclusive_volume': 0,
                                }
                            ],
                        },
                        {
                            'volume': 171.843168,
                            'cost': 343.686336,
                            'currency': {'code': 'EUR'},
                            'id': 48,
                            'name': 'Test Tariff multi APN',
                            'ratezone': [
                                {
                                    'countries': [
                                        {
                                            'volume': '171.843168',
                                            'cost': '343.6863360000',
                                            'ratezone': 'Telekom Germany Zone',
                                            'ratezone_id': '61',
                                            'rate': '2.000000',
                                            'currency': {'code': 'EUR'},
                                            'country': {'name': 'Germany'},
                                        }
                                    ],
                                    'volume': 171.843168,
                                    'cost': 343.686336,
                                    'name': 'Telekom Germany Zone',
                                    'id': 61,
                                    'tariff': 'Test Tariff multi APN',
                                    'rate': '2.000000',
                                    'currency': {'code': 'EUR'},
                                    'data_package_volume': 0,
                                    'inclusive_volume': 0,
                                }
                            ],
                        },
                    ],
                    'total': {
                        'volume': 202.05297,
                        'cost': 343.686336,
                        'currency': {'code': 'EUR'},
                    },
                },
                'sms': {
                    'tariff': [
                        {
                            'volume': 338,
                            'cost': 22.06,
                            'currency': {'code': 'EUR'},
                            'id': 1,
                            'name': 'Tariff 1',
                            'ratezone': [
                                {
                                    'countries': [
                                        {
                                            'volume': '338.000000',
                                            'cost': '22.0600000000',
                                            'ratezone': 'Zone 1',
                                            'ratezone_id': '1',
                                            'tariff': 'Tariff 1',
                                            'tariff_id': '1',
                                            'country': {'name': 'Germany'},
                                            'currency': {'code': 'EUR'},
                                        }
                                    ],
                                    'volume': 338,
                                    'cost': 22.06,
                                    'name': 'Zone 1',
                                    'id': 1,
                                    'tariff': 'Tariff 1',
                                    'currency': {'code': 'EUR'},
                                }
                            ],
                        }
                    ],
                    'total': {
                        'volume': 338,
                        'cost': 22.06,
                        'currency': {'code': 'EUR'},
                    },
                },
            },
            'customer_org': {
                'name': 'Max Muster Self-Signup',
                'organisation_type_id': '4',
                'ext_reference': 'MG ',
                'id': 112,
                'invoice_address': {
                    'name': 'Max Musterman',
                    'title': None,
                    'department': None,
                    'street': 'Alexanderst 15',
                    'zipcode': '1337',
                    'city': 'Berlin',
                    'country_id': '14',
                    'email': None,
                    'phone': '+491757280819',
                    'mobile': None,
                    'country': {
                        'name': 'Australia',
                        'country_code': '61',
                        'mcc': '505',
                        'iso_code': 'au',
                        'latitude': '-27.000000',
                        'longitude': '133.000000',
                        'id': 14,
                    },
                },
            },
            'issuer_org': {
                'name': '{{site.brand.api_name}} GmbH',
                'organisation_type_id': '0',
                'ext_reference': '',
                'monthly_cost_limit': None,
                'id': 2,
                'company_address': {
                    'contact_id': '2',
                    'organisation_id': '2',
                    'contact_type_id': '5',
                    'name': '{{site.brand.api_name}} GmbH',
                    'title': None,
                    'department': None,
                    'street': 'Alexanderst. 15',
                    'zipcode': '1337',
                    'city': 'Berlin',
                    'country_id': '74',
                    'email': 'support@demo-org.com',
                    'phone': '+4993149739270',
                    'mobile': None,
                    'country': {
                        'name': 'Germany',
                        'country_code': '49',
                        'mcc': '262',
                        'iso_code': 'de',
                        'latitude': '51.000000',
                        'longitude': '9.000000',
                        'id': 74,
                    },
                },
                'bank_account': {
                    'bank_account_id': '1',
                    'organisation_id': '2',
                    'name': "Fuerstlich Castell'sche Bank",
                    'iban': 'DE78790300011001678800',
                    'bic': 'FUCEDE77',
                    'country_id': '74',
                    'country': {
                        'name': 'Germany',
                        'country_code': '49',
                        'mcc': '262',
                        'iso_code': 'de',
                        'latitude': '51.000000',
                        'longitude': '9.000000',
                        'id': 74,
                    },
                },
                'billing_config': {
                    'billing_config_id': '8',
                    'organisation_id': '2',
                    'charging_model_id': '0',
                    'payment_term_id': '1',
                    'vatin': 'DE294242646',
                    'invoice_issuer_info': 'Director\nMax Muster\nCompany Registration\nRegister Court Berlin\nHRB 1337',
                },
            },
            'vat': {
                'rate': '19.000000',
                'cost': 118.71320384,
                'currency': {'code': 'EUR'},
            },
            'sub_total': {'cost': 624.806336, 'currency': {'code': 'EUR'}},
            'total': {'cost': 743.51953984, 'currency': {'code': 'EUR'}},
            'period': 'October 1 - October 31, 2017',
        },
    )


class RetrieveSIMlistresponse(BaseModel):
    id: Optional[int] = Field(None, example=788)
    iccid: Optional[str] = Field(None, example=736826736473829800000)
    production_date: Optional[str] = Field(None, example='8/1/2019 8:47:00 AM')
    activation_date: Optional[str] = Field(None, example='8/21/2019 6:17:00 PM')
    status: Optional[Dict[str, Any]] = Field(
        None, example={'id': 1, 'description': 'Active'}
    )
    customer_org: Optional[Dict[str, Any]] = Field(
        None,
        example={
            'id': 13,
            'name': 'Enterprise',
            'country': {'id': 205, 'name': 'United Kingdom'},
        },
    )
    issuer_org: Optional[Dict[str, Any]] = Field(
        None,
        example={
            'id': 11,
            'name': 'MNO',
            'country': {'id': 205, 'name': 'United Kingdom'},
        },
    )
    endpoint: Optional[Dict[str, Any]] = Field(
        None,
        example={
            'id': 1,
            'name': 'arduino01',
            'imei': None,
            'imei_lock': False,
            'created': '2019-03-19T08:45:41.000Z',
            'last_updated': '2020-03-01T08:45:41.000Z',
            'organisation_id': 13,
            'service_profile_id': 1,
            'tariff_profile_id': 1,
            'tags': None,
            'ip_address': '10.1.1.9',
        },
    )
    imsi: Optional[str] = Field(None, example=123451234567890)
    msisdn: Optional[str] = Field(None, example=88563748761)
    model: Optional[Dict[str, Any]] = Field(
        None,
        example={
            'id': 1,
            'description': 'Java smartcard',
            'memory_size': 64,
            'formfactor': {'id': 1, 'name': '2FF', 'image': '2ff.jpg'},
            'manufacturer': {'id': 1, 'name': 'Motorola'},
        },
    )
    reseller_org: Optional[Dict[str, Any]] = Field(
        None,
        example={
            'id': 22,
            'name': 'Reseller',
            'country': {'id': 205, 'name': 'United Kingdom'},
        },
    )


class SIMResource(BaseModel):
    id: Optional[int] = Field(None, example=788)
    iccid: Optional[str] = Field(None, example=736826736473829800000)
    production_date: Optional[str] = Field(None, example='8/1/2019 8:47:00 AM')
    activation_date: Optional[str] = Field(None, example='8/21/2019 6:17:00 PM')
    status: Optional[Dict[str, Any]] = Field(
        None, example={'id': 1, 'description': 'Active'}
    )
    customer_org: Optional[Dict[str, Any]] = Field(
        None,
        example={
            'id': 13,
            'name': 'Enterprise',
            'country': {'id': 205, 'name': 'United Kingdom'},
        },
    )
    issuer_org: Optional[Dict[str, Any]] = Field(
        None,
        example={
            'id': 11,
            'name': 'MNO',
            'country': {'id': 205, 'name': 'United Kingdom'},
        },
    )
    endpoint: Optional[Dict[str, Any]] = None
    imsi: Optional[str] = Field(None, example=123451234567890)
    msisdn: Optional[str] = Field(None, example=88563748761)
    model: Optional[Dict[str, Any]] = None
    reseller_org: Optional[Dict[str, Any]] = None


class UpdateSIMrequest(BaseModel):
    issuer_org: Dict[str, Any]
    reseller_org: Dict[str, Any]
    customer_org: Dict[str, Any]
    status: Dict[str, Any]


class ListofAllAvailableSIMStatusesresponse(BaseModel):
    id: Optional[int] = Field(None, example=0)
    description: Optional[str] = Field(None, example='Issued')


class ListofIMSIsresponse(BaseModel):
    id: Optional[int] = Field(None, example=17)
    imsi: Optional[str] = Field(None, example=112201234567008)
    import_date: Optional[str] = Field(None, example='3/25/2019 1:12:39 PM')
    status: Optional[Dict[str, Any]] = Field(
        None, example={'id': 0, 'description': 'Enabled'}
    )
    imsi_pool: Optional[Dict[str, Any]] = Field(
        None,
        example={
            'id': 7,
            'description': 'MNO 1 Pool',
            'network_coverage_id': 2,
            'resource_provider': {
                'id': 3,
                'status_id': 0,
                'organisation_id': 4,
                'organisation_name': 'MNO 1',
            },
        },
    )
    type: Optional[Dict[str, Any]] = Field(
        None, example={'id': 0, 'description': 'Root IMSI'}
    )
    sim: Optional[Dict[str, Any]] = Field(
        None,
        example={
            'id': 20,
            'iccid': 6660000000000000000,
            'production_date': None,
            'status_id': 0,
            'sim_model_id': 3,
            'customer_org': {
                'id': 11,
                'name': 'Reseller 3 C5',
                'type_id': 3,
                'country_id': 14,
                'status_id': 0,
                'ext_reference': None,
            },
            'issuer_org': {
                'id': 5,
                'name': 'Service Provider 1',
                'type_id': 2,
                'country_id': 205,
                'status_id': 0,
                'ext_reference': None,
            },
        },
    )


class RetrieveIMSIByIDresponse(BaseModel):
    id: Optional[int] = None
    imsi: Optional[str] = None
    import_date: Optional[str] = None
    status: Optional[Dict[str, Any]] = None
    imsi_pool: Optional[Dict[str, Any]] = None
    type: Optional[Dict[str, Any]] = None
    sim: Optional[Dict[str, Any]] = None


class UpdateIMSIrequest(BaseModel):
    status: Dict[str, Any]


class ListofallavailableIMSIstatusesresponse(BaseModel):
    id: Optional[int] = Field(None, example=0)
    description: Optional[str] = Field(None, example='Enabled')


class ListofTariffsresponse(BaseModel):
    id: Optional[int] = Field(None, example=3)
    name: Optional[str] = Field(None, example='Tariff for M2M Europe')
    description: Optional[str] = Field(None, example='M2M Europe: Data+SMS')
    created: Optional[str] = Field(None, example='2019-01-10T09:36:58.000Z')
    default_sms_mt_rate: Optional[float] = Field(None, example=0.5)
    default_sms_mo_rate: Optional[float] = Field(None, example=0.4)
    sim_issued_rate: Optional[float] = Field(None, example=0.1)
    sim_activated_rate: Optional[float] = Field(None, example=0.2)
    sim_suspended_rate: Optional[float] = Field(None, example=0.3)
    sim_activation_rate: Optional[float] = Field(None, example=0.6)
    sim_reactivation_rate: Optional[float] = Field(None, example=0.8)
    sim_suspension_rate: Optional[float] = Field(None, example=0.7)
    sim_termination_rate: Optional[float] = Field(None, example=0.5)
    used_count: Optional[int] = Field(None, example=2)
    assigned_count: Optional[int] = Field(None, example=1)
    status: Optional[Dict[str, Any]] = Field(
        None, example={'description': 'Active', 'id': 1}
    )
    currency: Optional[Dict[str, Any]] = Field(
        None, example={'code': 'EUR', 'symbol': '�', 'id': 1}
    )
    data_blocksize: Optional[Dict[str, Any]] = Field(
        None, example={'id': 10, 'octets': 1, 'description': 'exact'}
    )
    data_throttle: Optional[Dict[str, Any]] = Field(
        None, example={'id': 9, 'octets': 256000, 'description': '256 kbit/s'}
    )
    pdp_context_definition: Optional[List[Dict[str, Any]]] = Field(None, description='')


class CreateTariffrequest(BaseModel):
    name: str
    description: Optional[str] = None
    default_sms_mt_rate: Optional[float] = None
    default_sms_mo_rate: Optional[float] = None
    sim_issued_rate: Optional[float] = None
    sim_activated_rate: Optional[float] = None
    sim_suspended_rate: Optional[float] = None
    sim_activation_rate: Optional[float] = None
    sim_reactivation_rate: Optional[float] = None
    sim_suspension_rate: Optional[float] = None
    sim_termination_rate: Optional[float] = None
    currency: Optional[Dict[str, Any]] = None
    data_blocksize: Optional[Dict[str, Any]] = None
    data_throttle: Optional[Dict[str, Any]] = None


class TariffCategory(BaseModel):
    id: Optional[int] = None
    name: str
    used_by: Optional[int] = None


class RetrieveTariffresponse(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    created: Optional[str] = None
    default_sms_mt_rate: Optional[float] = None
    default_sms_mo_rate: Optional[float] = None
    sim_issued_rate: Optional[float] = None
    sim_activated_rate: Optional[float] = None
    sim_suspended_rate: Optional[float] = None
    sim_activation_rate: Optional[float] = None
    sim_reactivation_rate: Optional[float] = None
    sim_suspension_rate: Optional[float] = None
    sim_termination_rate: Optional[float] = None
    used_count: Optional[int] = None
    assigned_count: Optional[int] = None
    status: Optional[Dict[str, Any]] = None
    currency: Optional[Dict[str, Any]] = None
    data_blocksize: Optional[Dict[str, Any]] = None
    data_throttle: Optional[Dict[str, Any]] = None
    pdp_context_definition: Optional[List[Dict[str, Any]]] = Field(None, description='')
    public: Optional[bool] = None
    tariff_category: Optional[TariffCategory] = Field(None, title='TariffCategory')


class PatchTariffrequest(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    default_sms_mt_rate: Optional[float] = None
    default_sms_mo_rate: Optional[float] = None
    sim_issued_rate: Optional[float] = None
    sim_activated_rate: Optional[float] = None
    sim_suspended_rate: Optional[float] = None
    sim_activation_rate: Optional[float] = None
    sim_reactivation_rate: Optional[float] = None
    sim_suspension_rate: Optional[float] = None
    sim_termination_rate: Optional[float] = None
    status: Optional[Dict[str, Any]] = None
    currency: Optional[Dict[str, Any]] = None
    data_blocksize: Optional[Dict[str, Any]] = None
    data_throttle: Optional[Dict[str, Any]] = None


class ListofavailableTariffstatusesresponse(BaseModel):
    id: Optional[int] = Field(None, example=0)
    description: Optional[str] = Field(None, example='Staging')


class ListofRatezonesresponse(BaseModel):
    id: Optional[int] = Field(None, example=4)
    name: Optional[str] = Field(None, example='Zone 1')
    status: Optional[Dict[str, Any]] = Field(
        None, example={'id': 0, 'description': 'Staging'}
    )
    valid_from: Optional[str] = Field(None, example='2020-01-01T00:00:00.000Z')
    valid_until: Optional[str] = None
    coverage: Optional[List[Dict[str, Any]]] = Field(None, description='')
    rate: Optional[List[Dict[str, Any]]] = Field(None, description='')


class AddRatezonetoTariffrequest(BaseModel):
    name: str
    valid_from: str
    valid_until: str


class PatchRatezonerequest(BaseModel):
    name: str
    status: Dict[str, Any]
    valid_from: str
    valid_until: str


class Listofavailableratezonestatusesresponse(BaseModel):
    id: Optional[int] = Field(None, example=0)
    description: Optional[str] = Field(None, example='Staging')


class AddRatetoaRatezonerequest(BaseModel):
    rate: float
    volume: int
    currency: Dict[str, Any]
    service: Dict[str, Any]
    valid_from: str
    valid_until: str


class UpdateRateofaRatezonerequest(BaseModel):
    valid_from: str
    valid_until: str


class ListofTariffProfilesresponse(BaseModel):
    id: Optional[int] = Field(None, example=1)
    name: Optional[str] = Field(None, example='Tariff Profile 1')
    description: Optional[str] = Field(
        None, example='This Tariff Profile is for testing.'
    )
    used_count: Optional[int] = Field(None, example=56)
    tariff: Optional[Dict[str, Any]] = Field(
        None,
        example={
            'id': 1,
            'name': 'Tariff 1',
            'description': 'Tariff only for testing.',
            'created': '2019-10-20T00:00:00.000Z',
            'default_sms_mt_rate': 0.06,
            'default_sms_mo_rate': 0.06,
            'sim_issued_rate': 0,
            'sim_activated_rate': 1,
            'sim_suspended_rate': 0,
            'sim_activation_rate': 0,
            'sim_reactivation_rate': 0.5,
            'sim_suspension_rate': 0.5,
            'sim_termination_rate': 0,
            'currency': {'id': 1, 'code': 'EUR', 'symbol': '�'},
            'data_blocksize': {'id': 1, 'description': 'exact', 'octets': 1},
            'data_throttle': {'id': 1, 'description': '256 kbit/s', 'octets': 256000},
            'pdp_context_definition': [
                {'id': 12, 'apn': 'internet.test.com', 'default': True}
            ],
        },
    )


class CreateTariffProfilerequest(BaseModel):
    name: str
    description: str
    tariff: Dict[str, Any]


class RetrieveTariffProfileresponse(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    used_count: Optional[int] = None
    tariff: Optional[Dict[str, Any]] = None
    ratezone: Optional[List[Dict[str, Any]]] = Field(None, description='')


class PatchTariffProfilerequest(BaseModel):
    name: str
    description: str
    tariff: Dict[str, Any]


class RetrieveCoverageresponse(BaseModel):
    country: Optional[Dict[str, Any]] = Field(
        None, example={'id': 1, 'name': 'Germany'}
    )
    redundancy_count: Optional[int] = Field(None, example=2)


class Retrievesingleselectionsresponse(BaseModel):
    id: Optional[int] = None
    tariff_plan: Optional[Dict[str, Any]] = None
    status: Optional[Dict[str, Any]] = None
    start_date: Optional[str] = None
    expiry_date: Optional[str] = None
    selection_date: Optional[str] = None
    payment: Optional[List[Dict[str, Any]]] = Field(None, description='')


class RetrieveServiceProfileListresponse(BaseModel):
    id: Optional[int] = Field(None, example=232)
    name: Optional[str] = Field(None, example='Smart meter')
    description: Optional[str] = Field(None, example='Data + SMS - 1G limit')
    used_count: Optional[str] = Field(None, example=2)
    allowed_3g: Optional[bool] = Field(None, example=True)
    allowed_4g: Optional[bool] = Field(None, example=False)
    allowed_nb_iot: Optional[bool] = Field(None, example=False)
    apply_sms_quota: Optional[bool] = Field(None, example=False)
    apply_data_quota: Optional[bool] = Field(None, example=False)


class CreateaServiceProfilerequest(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    allowed_3g: Optional[bool] = None
    allowed_4g: Optional[bool] = None
    allowed_nb_iot: Optional[bool] = None
    apply_sms_quota: Optional[bool] = None
    apply_data_quota: Optional[bool] = None
    retail: Optional[bool] = None
    sms_p2p_int: Optional[bool] = None
    sms_p2p_ext: Optional[bool] = None
    prepaid: Optional[bool] = None
    nipdp: Optional[bool] = None
    api_callback: Optional[Dict[str, Any]] = None
    api_secret: Optional[Dict[str, Any]] = None
    moc_callback: Optional[Dict[str, Any]] = None
    esme_interface_type: Optional[Dict[str, Any]] = None
    breakout_region: Optional[Dict[str, Any]] = None
    dns: Optional[Dict[str, Any]] = None


class RetrieveaSingleServiceProfileresponse(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    allowed_3g: Optional[bool] = None
    allowed_4g: Optional[bool] = None
    allowed_nb_iot: Optional[bool] = None
    apply_sms_quota: Optional[bool] = None
    apply_data_quota: Optional[bool] = None
    retail: Optional[bool] = None
    sms_p2p_int: Optional[bool] = None
    sms_p2p_ext: Optional[bool] = None
    prepaid: Optional[bool] = None
    nipdp: Optional[bool] = None
    used_count: Optional[int] = None
    api_callback: Optional[Dict[str, Any]] = None
    api_secret: Optional[Dict[str, Any]] = None
    moc_callback: Optional[Dict[str, Any]] = None
    esme_interface_type: Optional[Dict[str, Any]] = None
    breakout_region: Optional[Dict[str, Any]] = None
    service: Optional[List[Dict[str, Any]]] = Field(None, description='')


class UpdateServiceProfilerequest(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    allowed_3g: Optional[bool] = None
    allowed_4g: Optional[bool] = None
    allowed_nb_iot: Optional[bool] = None
    apply_sms_quota: Optional[bool] = None
    apply_data_quota: Optional[bool] = None
    retail: Optional[bool] = None
    sms_p2p_int: Optional[bool] = None
    sms_p2p_ext: Optional[bool] = None
    prepaid: Optional[bool] = None
    nipdp: Optional[bool] = None
    api_callback: Optional[Dict[str, Any]] = None
    api_secret: Optional[Dict[str, Any]] = None
    moc_callback: Optional[Dict[str, Any]] = None
    esme_interface_type: Optional[Dict[str, Any]] = None
    breakout_region: Optional[Dict[str, Any]] = None
    dns: Optional[Dict[str, Any]] = None


class RetrieveAvailableServicesresponse(BaseModel):
    id: Optional[int] = Field(None, example=232)
    description: Optional[str] = Field(None, example='Data')
    teleservice_code: Optional[int] = Field(None, example=767)
    used_with_vlr: Optional[bool] = Field(None, example=True)
    used_with_sgsn: Optional[bool] = Field(None, example=True)
    traffic_type: Optional[Dict[str, Any]] = Field(
        None, example={'id': 1, 'description': 'Data', 'unit': 'MB'}
    )


class RetrieveavailableTrafficLimitsresponse(BaseModel):
    id: Optional[int] = Field(None, example=111)
    service: Optional[Dict[str, Any]] = Field(
        None, example={'id': 123, 'description': 'data'}
    )
    volume: Optional[int] = Field(None, example=64)
    period: Optional[Dict[str, Any]] = Field(
        None, example={'id': 33, 'time_units': 5, 'unit': 'Days'}
    )


class CreateTrafficLimitrequest(BaseModel):
    service: List[Dict[str, Any]] = Field(..., description='')
    volume: int
    period: Dict[str, Any]


class Period(BaseModel):
    id: Optional[int] = None
    time_units: Optional[int] = None
    unit: Optional[str] = Field(None, example='Days')


class ServiceTrafficLimitsResponseItem(BaseModel):
    id: Optional[int] = None
    volume: Optional[int] = None
    period: Optional[Period] = None


class ServiceTrafficLimitsResponse(BaseModel):
    __root__: List[ServiceTrafficLimitsResponseItem] = Field(
        ...,
        example=[
            {
                'id': 111,
                'volume': 64,
                'period': {'id': 33, 'time_units': 5, 'unit': 'Days'},
            },
            {
                'id': 234,
                'volume': 128,
                'period': {'id': 35, 'time_units': 1, 'unit': 'Months'},
            },
        ],
        title='Service Traffic Limit',
    )


class RetrieveDNSlistresponseItem(BaseModel):
    id: Optional[int] = None
    primary: Optional[str] = None
    secondary: Optional[str] = None
    ip_address_version: Optional[int] = None


class RetrieveDNSlistresponse(BaseModel):
    __root__: List[RetrieveDNSlistresponseItem] = Field(
        ..., title='RetrieveDNSlistresponse'
    )


class CreateaDNSentryrequest(BaseModel):
    primary: str
    secondary: str
    ip_address_version: int


class Status3(BaseModel):
    id: Optional[float] = Field(None, example=2)
    description: Optional[str] = Field(None, example='Suspended')


class Organisation(BaseModel):
    id: Optional[float] = Field(None, example=42)
    name: Optional[str] = Field(None, example='Example Org')


class User(BaseModel):
    id: Optional[int] = Field(None, example=42)
    username: Optional[str] = Field(None, example='user@example.com')
    name: Optional[str] = Field(None, example='Douglas Adams')
    created: Optional[str] = Field(None, example='10/12/2019 8:00:00 AM')
    status: Optional[Status3] = None
    organisation: Optional[Organisation] = None


class CreateUserrequest(BaseModel):
    username: str
    name: str
    organisation: Dict[str, Any]
    roles: List[Dict[str, Any]] = Field(..., description='')


class RetrievetheUserresponse(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    name: Optional[str] = None
    created: Optional[str] = None
    status: Optional[Dict[str, Any]] = None
    organisation: Optional[Dict[str, Any]] = None
    roles: Optional[List[Dict[str, Any]]] = Field(None, description='')
    mfa: Optional[List[Dict[str, Any]]] = Field(None, description='')


class UpdateUserrequest(BaseModel):
    username: str
    name: str
    status: Dict[str, Any]


class RetrieveUserByUsernameresponse(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    name: Optional[str] = None
    created: Optional[str] = None
    status: Optional[Dict[str, Any]] = None
    organisation: Optional[Dict[str, Any]] = None


class RetrieveAvailableUserStatusesresponse(BaseModel):
    id: Optional[int] = Field(None, example=0)
    description: Optional[str] = Field(None, example='Activation Pending')


class EventType(BaseModel):
    id: Optional[float] = Field(None, example=10)
    description: Optional[str] = Field(None, example='User authentication failed')


class EventSource(BaseModel):
    id: Optional[float] = Field(None, example=2)
    description: Optional[str] = Field(None, example='API')


class EventSeverity(BaseModel):
    id: Optional[float] = Field(None, example=1)
    description: Optional[str] = Field(None, example='Warning')


class Organisation1(BaseModel):
    id: Optional[float] = Field(None, example=42)
    name: Optional[str] = Field(None, example='Example Org')


class User1(BaseModel):
    id: Optional[float] = Field(None, example=10)
    username: Optional[str] = Field(None, example='admin@example.com')
    name: Optional[str] = Field(None, example='Ford Prefect')


class Event(BaseModel):
    id: Optional[int] = Field(None, example=11)
    alert: Optional[bool] = None
    description: Optional[str] = Field(
        None,
        example="Failed authentication request from 'admin@example.com', Reason: invalid password from IP 1.2.3.4",
    )
    timestamp: Optional[str] = Field(None, example='5/8/2017 10:56:25 AM')
    event_type: Optional[EventType] = None
    event_source: Optional[EventSource] = None
    event_severity: Optional[EventSeverity] = None
    organisation: Optional[Organisation1] = None
    user: Optional[User1] = None


class RetrieveEventsresponse4(BaseModel):
    id: int = Field(..., example=11)
    alert: bool = Field(..., example=False)
    description: str = Field(
        ...,
        example=" Failed authentication request from 'ford.prefect@hitchhikerguide.net', Reason: invalid passwort from IP 1.2.3.4",
    )
    timestamp: str = Field(..., example='5/8/2017 10:56:25 AM')
    event_type: Dict[str, Any] = Field(
        ..., example={'id': 6, 'description': 'User authentication failed'}
    )
    event_source: Dict[str, Any] = Field(..., example={'id': 2, 'description': 'API'})
    event_severity: Dict[str, Any] = Field(
        ..., example={'id': 1, 'description': 'Warn'}
    )
    organisation: Dict[str, Any] = Field(
        ..., example={'id': 123, 'name': 'Seeley & Co.'}
    )
    user: Dict[str, Any] = Field(
        ...,
        example={
            'id': 42,
            'username': 'ford.prefect@hitchhikerguide.net',
            'name': 'Ford Prefect',
        },
    )


class AccountActivationrequest(BaseModel):
    activationKey: str
    password: str


class ReSendActivationMailrequest(BaseModel):
    username: str
    g_recaptcha_response: str = Field(..., alias='g-recaptcha-response')


class Id4(Enum):
    number_0 = 0
    number_1 = 1


class Status4(BaseModel):
    id: Optional[Id4] = Field(None, description='`0` - disabled\n`1` - enabled\n')


class CoverageUpdateVPLMNStatusPatch(BaseModel):
    status: Optional[Status4] = None


class ChangePasswordrequest(BaseModel):
    old_password: str
    new_password: str


class ChangePassword422response(BaseModel):
    error_code: Optional[int] = None
    error_token: Optional[str] = None
    message: Optional[str] = None
    errors: Optional[List[Dict[str, Any]]] = Field(None, description='')


class RetrieveownIPAddressSpacesresponse(BaseModel):
    id: Optional[int] = Field(None, example=1)
    ip_address_space: Optional[str] = Field(None, example='10.199.128.0/18')
    ip_address_version: Optional[int] = Field(None, example=4)
    used_count: Optional[int] = Field(None, example=2)
    available_count: Optional[int] = Field(None, example=16380)


class RetrieveAvailableAddressSpacesresponse(BaseModel):
    id: Optional[int] = Field(None, example=1)
    ip_address_space: Optional[str] = Field(None, example='10.199.128.0/18')
    ip_address_version: Optional[int] = Field(None, example=4)


class Field204Response(BaseModel):
    __root__: Any = Field(
        ...,
        description='The server has successfully fulfilled the request and that there is no additional content to send in the response payload body.',
        title='204 Response',
    )


class RetrieveEventsresponse5(BaseModel):
    id: int = Field(..., example=14)
    alert: bool = Field(..., example=False)
    description: str = Field(
        ...,
        example="MFA key with Id '1' of Type 'Time-Based One-Time Password' deleted for user 'root@localhost'",
    )
    timestamp: str = Field(..., example='5/5/2017 12:00:30 PM')
    event_type: Dict[str, Any] = Field(
        ..., example={'id': 14, 'description': 'Multi-factor Authentication'}
    )
    event_source: Dict[str, Any] = Field(..., example={'id': 2, 'description': 'API'})
    event_severity: Dict[str, Any] = Field(
        ..., example={'id': 0, 'description': 'Info'}
    )
    organisation: Dict[str, Any] = Field(..., example={'id': 4, 'name': 'MNO 1'})
    user: Optional[Dict[str, Any]] = Field(
        None,
        example={'id': 2, 'username': 'eabbot@flatland.org', 'name': 'Edwin Abbot'},
    )
    endpoint: Optional[Dict[str, Any]] = Field(
        None,
        example={
            'name': 'Monitoring201',
            'tags': 'Monitoring',
            'ip_address': '10.199.6.39',
            'imei': None,
            'id': 69,
        },
    )
    sim: Optional[Dict[str, Any]] = Field(
        None,
        example={
            'iccid': 8988317000000000000,
            'production_date': '2019-12-17T13:26:13.000Z',
            'id': 110,
        },
    )
    imsi: Optional[Dict[str, Any]] = Field(
        None,
        example={
            'imsi': 901430000000114,
            'import_date': '2019-12-17T13:26:08.000Z',
            'id': 110,
        },
    )
    detail: Optional[Dict[str, Any]] = Field(
        None,
        example={
            'id': 2,
            'name': 'Telekom',
            'country': {
                'id': 74,
                'name': 'Germany',
                'country_code': 49,
                'mcc': 262,
                'iso_code': 'de',
            },
            'tapcode': [{'id': 1, 'tapcode': 'DEUD1'}],
            'mnc': [{'id': 2, 'mnc': 1}],
        },
    )


class RetrieveEventTypesresponse(BaseModel):
    id: Optional[int] = Field(None, example=0)
    description: Optional[str] = Field(None, example='Generic')


class RetrieveAvailableCountriesresponse(BaseModel):
    id: Optional[int] = Field(None, example=1)
    name: Optional[str] = Field(None, example='Germany')
    country_code: Optional[str] = Field(None, example=49)
    mcc: Optional[str] = Field(None, example=262)
    iso_code: Optional[str] = Field(None, example='de')


class RetrieveAvailableCurrenciesresponse(BaseModel):
    id: Optional[int] = Field(None, example=1)
    code: Optional[str] = Field(None, example='EUR')
    symbol: Optional[str] = Field(None, example='�')


class RetrieveAvailableDataBlocksizesresponse(BaseModel):
    id: Optional[int] = Field(None, example=1)
    octets: Optional[str] = Field(None, example=1)
    description: Optional[str] = Field(None, example='exact')


class RetrieveAvailableDataThrottlesresponse(BaseModel):
    id: Optional[int] = Field(None, example=1)
    octets: Optional[str] = Field(None, example=128000)
    description: Optional[str] = Field(None, example='128 kbit/s')


class RetrieveAvailableOperatorsresponse(BaseModel):
    id: Optional[int] = Field(None, example=2)
    name: Optional[str] = Field(None, example='Telekom')
    country: Optional[Dict[str, Any]] = Field(
        None,
        example={
            'id': 74,
            'name': 'Germany',
            'country_code': 49,
            'mcc': 262,
            'iso_code': 'de',
        },
    )
    tapcode: Optional[List[Dict[str, Any]]] = Field(None, description='')
    mnc: Optional[List[Dict[str, Any]]] = Field(None, description='')


class RetrieveAvailableBreakoutRegionsresponse(BaseModel):
    id: Optional[int] = Field(None, example=2)
    name: Optional[str] = Field(None, example='eu-west')
    ip_address: Optional[str] = Field(None, example='1.2.3.4')


class TariffPlanStatusesGetResponse(BaseModel):
    __root__: Any = Field(
        ...,
        example=[
            {
                'id': 0,
                'name': 'Staging',
                'description': 'under construction and therefore not ready to be used; any changes of the configuration are allowed',
            },
            {
                'id': 1,
                'name': 'Active',
                'description': 'deployed and may be in use; changes to the configuration are limited',
            },
            {
                'id': 2,
                'name': 'Deprecated',
                'description': 'not assignable anymore but remains valid for current assignments and therefore may be still in use; changes to the configuration are limited',
            },
            {
                'id': 3,
                'name': 'Deleted',
                'description': 'not visible to maintainers and users, but is displayed in history view, no changes to the configuration are allowed',
            },
        ],
    )


class TariffPlanConfigGetResponse(BaseModel):
    __root__: Any = Field(
        ...,
        example=[
            {
                'id': 24,
                'name': 'Data Flat',
                'description': 'Unlimited Data Usage, ...',
                'status': {'id': 1, 'name': 'Active'},
                'public_for_child_organisations': False,
                'owner_organisation': {'id': 1, 'name': 'Own Organisation'},
                'min_runtime': {
                    'id': 18,
                    'number_of_units': 18,
                    'unit': {'id': 1, 'name': 'month'},
                },
                'deprecation_date': '2018-05-20T00:00:00.000Z',
                'payment': [
                    {
                        'id': 2,
                        'interval': {'id': 1, 'name': 'month'},
                        'amount': 29.99,
                        'currency': {'id': 1, 'symbol': '�'},
                    },
                    {
                        'id': 5,
                        'interval': {'id': 2, 'name': 'contract term'},
                        'amount': 450,
                        'currency': {'id': 1, 'symbol': '�'},
                    },
                ],
                'elements': [
                    {
                        'id': 3,
                        'name': 'max. active SIMs per month',
                        'status': {
                            'id': 1,
                            'name': 'Active',
                            'description': 'deployed and may be in use; changes to the configuration are limited',
                        },
                        'optional': False,
                    },
                    {
                        'id': 13,
                        'name': 'additional SIM package',
                        'status': {
                            'id': 1,
                            'name': 'Active',
                            'description': 'deployed and may be in use; changes to the configuration are limited',
                        },
                        'optional': True,
                    },
                ],
            },
            {
                'id': 28,
                'name': 'Data Flat & SMS Flat',
                'description': 'Unlimited Data Usage and SMS Flat ...',
                'status': {'id': 1, 'name': 'Active'},
                'public_for_child_organisations': True,
                'owner_organisation': {'id': 2, 'name': 'Child Organisation'},
                'min_runtime': {
                    'id': 24,
                    'number_of_units': 24,
                    'unit': {'id': 1, 'name': 'month'},
                },
                'payment': [
                    {
                        'id': 2,
                        'interval': {'id': 1, 'name': 'month'},
                        'amount': 39.99,
                        'currency': {'id': 1, 'symbol': '�'},
                    },
                    {
                        'id': 5,
                        'interval': {'id': 2, 'name': 'contract term'},
                        'amount': 800,
                        'currency': {'id': 1, 'symbol': '�'},
                    },
                ],
                'elements': [
                    {
                        'id': 8,
                        'name': '100 additional active sims',
                        'status': {
                            'id': 1,
                            'name': 'Active',
                            'description': 'deployed and may be in use; changes to the configuration are limited',
                        },
                        'optional': True,
                    }
                ],
            },
        ],
    )


class RetrieveAvailableESMEInterfaceTypesresponse(BaseModel):
    id: int = Field(..., example=1)
    description: str = Field(..., example='SMPP')


class PDPContextDefinitionsGetResponse(BaseModel):
    pass


class Organisation2(BaseModel):
    name: Optional[str] = None
    organisation_type_id: Optional[str] = None
    country_id: Optional[str] = None
    organisation_status_id: Optional[str] = None
    ext_reference: Optional[str] = None
    monthly_cost_limit: Optional[str] = None
    currency_id: Optional[int] = None
    organisation_class_id: Optional[int] = None
    created: Optional[datetime] = None
    verification_type_id: Optional[str] = None
    verification: Optional[str] = None
    brand_id: Optional[str] = None
    default_sms_routing_id: Optional[str] = None
    id: Optional[int] = None


class PDPContextDefinitionsCreateUpdate(BaseModel):
    apn: Optional[str] = None
    organisation: Optional[Organisation2] = None
    auto_assign: Optional[float] = None
    qos_subscribed: Optional[str] = None
    ext_qos_subscribed: Optional[str] = None
    ext2_qos_subscribed: Optional[str] = None
    ext3_qos_subscribed: Optional[str] = None
    ext4_qos_subscribed: Optional[str] = None


class PDPContextDefinitionsCreateResponse(BaseModel):
    id: Optional[float] = None


class RatType1(BaseModel):
    id: Optional[int] = None


class QoSDefinitionCreateRequest(BaseModel):
    rat_type: Optional[RatType1] = Field(None, example={'id': 23211}, title='HasId')
    max_bandwidth_dl: Optional[conint(ge=0, le=4294967295)] = None
    max_bandwidth_ul: Optional[conint(ge=0, le=4294967295)] = None


class RatType2(BaseModel):
    id: Optional[float] = None
    description: Optional[str] = None


class QoSDefinitionGetResponse(BaseModel):
    rat_type: Optional[RatType2] = Field(None, title='RAT Type')
    max_bandwidth_dl: Optional[int] = None
    max_bandwidth_ul: Optional[int] = None


class QoSDefinitionPatchRequest(BaseModel):
    max_bandwidth_dl: Optional[conint(ge=0, le=4294967295)] = None
    max_bandwidth_ul: Optional[conint(ge=0, le=4294967295)] = None


class NetworkCoverage(BaseModel):
    id: Optional[int] = None


class TrafficType9(BaseModel):
    id: Optional[int] = None


class Currency6(BaseModel):
    id: Optional[int] = None


class IOTCreate(BaseModel):
    mnc: Optional[int] = None
    mcc: Optional[int] = None
    network_coverage: Optional[NetworkCoverage] = Field(
        None, example={'id': 23211}, title='HasId'
    )
    traffic_type: Optional[TrafficType9] = Field(
        None, example={'id': 23211}, title='HasId'
    )
    currency: Optional[Currency6] = Field(None, example={'id': 23211}, title='HasId')
    rate: Optional[float] = None
    volume: Optional[int] = None
    blocksize: Optional[int] = None
    valid_from: Optional[datetime] = None


class HasId(BaseModel):
    id: Optional[int] = None


class LocalDate(BaseModel):
    __root__: constr(regex=r'^\d{4}-\d{2}-\d{2}$') = Field(
        ...,
        description='Local date in format YYYY-MM-DD without a time',
        example='2049-01-01T00:00:00.000Z',
        title='Local Date without Time',
    )


class LocalDateTime(BaseModel):
    __root__: constr(regex=r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\{2}$') = Field(
        ...,
        description='Local date in format YYYY-MM-DD HH:mm:ss with a time.\nUsually interpreted in UTC Timezone, but generally unbound.\n',
        example='2049-01-01T12:11:33.000Z',
        title='Local Date with Time',
    )


class Currency7(BaseModel):
    code: Optional[str] = None
    symbol: Optional[str] = None
    id: Optional[int] = None


class GtConfig1(BaseModel):
    imsi_prefix: Optional[str] = None
    calling_party: Optional[str] = None
    called_party_tt: Optional[str] = None
    id: Optional[int] = None


class MsisdnPool1(BaseModel):
    resource_provider_id: Optional[str] = None
    description: Optional[str] = None
    id: Optional[int] = None


class Country3(BaseModel):
    name: Optional[str] = None
    country_code: Optional[int] = None
    mcc: Optional[float] = None
    iso_code: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    id: Optional[int] = None


class Operator1(BaseModel):
    country_id: Optional[str] = None
    name: Optional[str] = None
    country_name: Optional[str] = None
    id: Optional[int] = None
    country: Optional[Country3] = None
    tapcodes: Optional[str] = None
    mncs: Optional[str] = None


class Organisation3(BaseModel):
    name: Optional[str] = None
    organisation_type_id: Optional[str] = None
    country_id: Optional[str] = None
    organisation_status_id: Optional[str] = None
    ext_reference: Optional[str] = None
    monthly_cost_limit: Optional[str] = None
    currency_id: Optional[int] = None
    organisation_class_id: Optional[int] = None
    created: Optional[datetime] = None
    verification_type_id: Optional[str] = None
    verification: Optional[str] = None
    brand_id: Optional[str] = None
    default_sms_routing_id: Optional[str] = None
    id: Optional[int] = None


class PaymentOption(BaseModel):
    id: Optional[float] = None


class Type1(BaseModel):
    id: Optional[float] = None


class OrgPrepaidBalance(BaseModel):
    amount: Optional[float] = None
    external_payment_identifier: Optional[str] = None
    payment_option: Optional[PaymentOption] = None
    type: Optional[Type1] = None


class SmppBind1(BaseModel):
    system_id: Optional[str] = None
    smpp_bind_status_id: Optional[str] = None
    id: Optional[int] = None


class SmsRoutingListItem(BaseModel):
    id: Optional[float] = None
    description: Optional[str] = None
    organisation: Optional[Dict[str, Any]] = None


class SmsRoutingList1(BaseModel):
    name: Optional[str] = None
    organisation_type_id: Optional[str] = None
    country_id: Optional[str] = None
    organisation_status_id: Optional[str] = None
    ext_reference: Optional[str] = None
    monthly_cost_limit: Optional[str] = None
    currency_id: Optional[int] = None
    organisation_class_id: Optional[int] = None
    created: Optional[datetime] = None
    verification_type_id: Optional[str] = None
    verification: Optional[str] = None
    brand_id: Optional[str] = None
    default_sms_routing_id: Optional[str] = None
    id: Optional[int] = Field(
        None,
        example={
            'description': 'Test Routing Entry',
            'id': 39,
            'organisation': {
                'name': 'org2',
                'organisation_type_id': '0',
                'country_id': '219',
                'organisation_status_id': '0',
                'ext_reference': '--',
                'monthly_cost_limit': None,
                'currency_id': '1',
                'organisation_class_id': '0',
                'created': '2020-02-01T00:00:00.000Z',
                'verification_type_id': None,
                'verification': '',
                'brand_id': '1',
                'default_sms_routing_id': None,
                'id': 2,
            },
        },
    )


class SmsRoutingList(BaseModel):
    __root__: Union[List[SmsRoutingListItem], SmsRoutingList1]


class Organisation4(BaseModel):
    name: Optional[str] = None
    organisation_type_id: Optional[str] = None
    country_id: Optional[str] = None
    organisation_status_id: Optional[str] = None
    ext_reference: Optional[str] = None
    monthly_cost_limit: Optional[str] = None
    currency_id: Optional[int] = None
    organisation_class_id: Optional[int] = None
    created: Optional[datetime] = None
    verification_type_id: Optional[str] = None
    verification: Optional[str] = None
    brand_id: Optional[str] = None
    default_sms_routing_id: Optional[str] = None
    id: Optional[int] = None


class SmsRoutingEntry(BaseModel):
    id: Optional[float] = None
    description: Optional[str] = None
    organisation: Optional[Organisation4] = None


class SccpCalledPartyPrefix1(BaseModel):
    prefix: Optional[str] = None
    tt: Optional[str] = None
    id: Optional[int] = None


class Country4(BaseModel):
    name: Optional[str] = None
    country_code: Optional[int] = None
    mcc: Optional[float] = None
    iso_code: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    id: Optional[int] = None


class SmppBind2(BaseModel):
    system_id: Optional[str] = None
    smpp_bind_status_id: Optional[str] = None
    id: Optional[int] = None


class Country5(BaseModel):
    name: Optional[str] = None
    country_code: Optional[int] = None
    mcc: Optional[float] = None
    iso_code: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    id: Optional[int] = None


class Operator2(BaseModel):
    country_id: Optional[str] = None
    name: Optional[str] = None
    country_name: Optional[str] = None
    id: Optional[int] = None
    country: Optional[Country5] = None
    tapcodes: Optional[str] = None
    mncs: Optional[str] = None


class MsisdnPool2(BaseModel):
    resource_provider_id: Optional[str] = None
    description: Optional[str] = None
    id: Optional[int] = None


class GtConfig2(BaseModel):
    imsi_prefix: Optional[str] = None
    calling_party: Optional[str] = None
    called_party_tt: Optional[str] = None
    id: Optional[int] = None


class SccpCalledPartyPrefix2(BaseModel):
    prefix: Optional[str] = None
    tt: Optional[str] = None
    id: Optional[int] = None


class SmsRoutingDataCreateUpdateRequest(BaseModel):
    id: Optional[float] = None
    sms_routing_id: Optional[str] = None
    country: Optional[Country4] = None
    smpp_bind: Optional[SmppBind2] = None
    operator: Optional[Operator2] = None
    msisdn_pool: Optional[MsisdnPool2] = None
    gt_config: Optional[GtConfig2] = None
    sccp_called_party_prefix: Optional[SccpCalledPartyPrefix2] = None


class GetEntryPoints(BaseModel):
    method: str = Field(..., example='GET')
    uri: str = Field(..., example='/api/v1/endpoint/:id')
    description: str = Field(..., example='Retrieve single Endpoint details by id')


class OperatorPostRequest(BaseModel):
    name: str
    country: Optional[Dict[str, Any]] = None
    id: Optional[float] = None


class CreateMFAKeyresponse(BaseModel):
    id: Optional[int] = None
    status: Optional[Dict[str, Any]] = None
    type: Optional[Dict[str, Any]] = None
    secret_key: Optional[str] = None
    otpauth: Optional[str] = None
    creation_date: Optional[str] = None


class ActivateMFAKeyrequest(BaseModel):
    status: Dict[str, Any]
    code: str


class MFAKeyStatusLookupresponse(BaseModel):
    id: Optional[int] = Field(None, example=0)
    description: Optional[str] = Field(None, example='Activation Pending')


class MFAKeyTypeLookupresponse(BaseModel):
    id: Optional[int] = Field(None, example=0)
    description: Optional[str] = Field(None, example='Time-Based One-Time Password')


class Listoftrusteddevicesresponse(BaseModel):
    id: Optional[int] = Field(None, example=16)
    operating_system: Optional[str] = Field(None, example='Ubuntu 16.04.2 LTS (Xenial)')
    browser: Optional[str] = Field(None, example='Mozilla Firefox')
    activation_date: Optional[str] = Field(None, example='2020-02-20T10:00:00.000Z')


class ListofApplicationTokensresponse(BaseModel):
    id: Optional[int] = Field(None, example=1)
    description: Optional[str] = Field(None, example='App Test Token')
    created: Optional[str] = Field(None, example='2020-02-20T10:00:00.000Z')
    status: Optional[Dict[str, Any]] = Field(
        None, example={'id': 0, 'description': 'Activated'}
    )
    expiry_date: Optional[str] = Field(None, example='2020-02-20T10:00:00.000Z')
    ip: Optional[str] = Field(None, example='10.88.0.139/32')
    creator: Optional[Dict[str, Any]] = Field(
        None, example={'id': 6, 'name': 'Master User', 'username': 'org-owner@org.com'}
    )


class CreateApplicationTokenrequest(BaseModel):
    description: Optional[str] = None
    expiry_date: Optional[str] = None
    ip: Optional[str] = None


class CreateApplicationTokenresponse(BaseModel):
    application_token: Optional[str] = None


class ApplicationToken(BaseModel):
    description: Optional[str] = None
    status: Optional[Dict[str, Any]] = None


class EndpointStatus(BaseModel):
    id: int
    description: Optional[str] = None


class ServiceProfile(BaseModel):
    id: int
    name: Optional[str] = None


class TariffProfile(BaseModel):
    id: int
    name: Optional[str] = None


class Sim(BaseModel):
    id: int
    iccid: Optional[str] = None
    msisdn: Optional[str] = None
    imsi: Optional[str] = None


class IpAddressSpace(BaseModel):
    id: int


class Status5(BaseModel):
    id: int
    description: Optional[str] = None


class ServiceProfile1(BaseModel):
    id: int
    name: Optional[str] = None


class TariffProfile1(BaseModel):
    id: int
    name: Optional[str] = None


class IpAddressSpace1(BaseModel):
    id: int


class Sim1(BaseModel):
    id: int
    iccid: Optional[str] = None
    msisdn: Optional[str] = None
    imsi: Optional[str] = None


class Endpoint(BaseModel):
    id: Optional[int] = None
    name: str
    tags: Optional[str] = None
    service_profile: ServiceProfile1 = Field(..., title='ServiceProfile')
    tariff_profile: TariffProfile1 = Field(..., title='TariffProfile')
    ip_address: Optional[str] = None
    ip_address_space: Optional[IpAddressSpace1] = Field(None, title='IpAddressSpace')
    sim: Optional[Sim1] = Field(None, title='Sim')
    imei: Optional[str] = None
    imei_lock: Optional[bool] = None
    created: Optional[datetime] = None
    last_updated: Optional[datetime] = None
    status: Status5 = Field(..., title='EndpointStatus')


class RetrieveSingleEndpointresponse(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    tags: Optional[str] = None
    created: Optional[str] = None
    last_updated: Optional[str] = None
    status: Optional[Dict[str, Any]] = None
    service_profile: Optional[Dict[str, Any]] = None
    tariff_profile: Optional[Dict[str, Any]] = None
    sim: Optional[Dict[str, Any]] = None
    imei: Optional[str] = None
    imei_lock: Optional[bool] = None
    ip_address: Optional[str] = None
    ip_address_space: Optional[Dict[str, Any]] = None
    runtime_data: Optional[Dict[str, Any]] = None


class UpdateEndpointrequest(BaseModel):
    tags: str
    status: Dict[str, Any]
    service_profile: Dict[str, Any]
    tariff_profile: Dict[str, Any]
    ip_address: str
    ip_address_space: Dict[str, Any]
    sim: Dict[str, Any]
    imei: str
    imei_lock: bool


class RetrieveEndpointConnectivityStatusresponse(BaseModel):
    status: Optional[Dict[str, Any]] = None
    location: Optional[Dict[str, Any]] = None
    pdp_context: Optional[Dict[str, Any]] = None
    services: Optional[List[str]] = Field(None, description='')


class GetEndpointLocationByIdResponse(BaseModel):
    gcid_cache_id: Optional[str] = None
    gcid: Optional[str] = None
    create_date: Optional[str] = None
    lat: Optional[str] = None
    lng: Optional[str] = None
    accuracy: Optional[str] = None


class RetrieveEndpointStatisticsresponse(BaseModel):
    last_month: Optional[Dict[str, Any]] = None
    current_month: Optional[Dict[str, Any]] = None
    last_hour: Optional[Dict[str, Any]] = None


class Status6(BaseModel):
    id: Optional[float] = None
    description: Optional[str] = None


class Type2(BaseModel):
    id: Optional[float] = None
    description: Optional[str] = None


class CloudConnectAttachment(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    user_id: Optional[int] = None
    creation_date: Optional[str] = Field(
        None, description='The date this attachment was created in UTC'
    )
    accept_attachment_expiry_date: Optional[str] = Field(
        None,
        description='The expiry date of the accept attachment state in UTC.\nThis will only be returned if the breakout is of type `Transit Gateway (type_id: 1)` and in Status `Pending AWS Actvation (status_id: 2)`\n',
    )
    termination_date: Optional[str] = None
    aws_transit_gateway_attachment_id: Optional[str] = None
    aws_vpn_connection_id: Optional[str] = Field(
        None, description='This is only set when the breakout is a VPN attachment'
    )
    status: Optional[Status6] = None
    type: Optional[Type2] = None
    region: Optional[str] = Field(
        None, description='The customer region that this attachment belongs to'
    )


class Status7(BaseModel):
    id: Optional[float] = None
    description: Optional[str] = None


class Type3(BaseModel):
    id: Optional[float] = None
    description: Optional[str] = None


class GetCloudConnectAttachmentsResponseItem(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    user_id: Optional[int] = None
    creation_date: Optional[str] = Field(
        None, description='The date this attachment was created in UTC'
    )
    accept_attachment_expiry_date: Optional[str] = Field(
        None,
        description='The expiry date of the accept attachment state in UTC.\nThis will only be returned if the breakout is of type `Transit Gateway (type_id: 1)` and in Status `Pending AWS Actvation (status_id: 2)`\n',
    )
    termination_date: Optional[str] = None
    aws_transit_gateway_attachment_id: Optional[str] = None
    aws_vpn_connection_id: Optional[str] = Field(
        None, description='This is only set when the breakout is a VPN attachment'
    )
    status: Optional[Status7] = None
    type: Optional[Type3] = None
    region: Optional[str] = Field(
        None, description='The customer region that this attachment belongs to'
    )


class GetCloudConnectAttachmentsResponse(BaseModel):
    __root__: List[GetCloudConnectAttachmentsResponseItem] = Field(
        ..., title='GetCloudConnectAttachmentsResponse'
    )


class CloudConnectBreakoutType(BaseModel):
    id: Optional[float] = None
    description: Optional[str] = None


class GetCloudConnectBreakoutTypesResponseItem(BaseModel):
    id: Optional[float] = None
    description: Optional[str] = None


class GetCloudConnectBreakoutTypesResponse(BaseModel):
    __root__: List[GetCloudConnectBreakoutTypesResponseItem] = Field(
        ..., title='GetCloudConnectBreakoutTypesResponse'
    )


class Status8(BaseModel):
    id: Optional[float] = None
    description: Optional[str] = None


class Metrics(BaseModel):
    tunnel_state: Optional[str] = None
    bytes_in: Optional[Dict[str, float]] = None
    bytes_out: Optional[Dict[str, float]] = None


class TunnelInformation(BaseModel):
    outside_address: Optional[str] = None
    inside_cidr: Optional[str] = None
    metrics: Optional[Metrics] = None
    asn: Optional[float] = None
    public_ip: Optional[str] = None


class GetCloudConnectAttachmentByIdResponseItem(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    user_id: Optional[int] = None
    creation_date: Optional[str] = Field(
        None, description='The date this attachment was created in UTC'
    )
    accept_attachment_expiry_date: Optional[str] = Field(
        None,
        description='The expiry date of the accept attachment state in UTC.\nThis will only be returned if the breakout is of type `Transit Gateway (type_id: 1)` and in Status `Pending AWS Actvation (status_id: 2)`\n',
    )
    termination_date: Optional[str] = None
    aws_transit_gateway_attachment_id: Optional[str] = None
    aws_vpn_connection_id: Optional[str] = Field(
        None, description='This is only set when the breakout is a VPN attachment'
    )
    status: Optional[Status8] = None
    id: Optional[float] = None
    description: Optional[str] = None
    tunnel_information: Optional[TunnelInformation] = None


class GetCloudConnectAttachmentByIdResponse(BaseModel):
    __root__: List[GetCloudConnectAttachmentByIdResponseItem] = Field(
        ..., title='GetCloudConnectAttachmentByIdResponse'
    )


class Type4(Enum):
    integer_1 = 1


class CreateCloudConnectTGWRequest(BaseModel):
    type: Type4
    name: str
    description: Optional[str] = None
    vpc_cidr: List[str]
    region: str = Field(
        ..., description='the region that this attachment should be established to'
    )
    aws_account_id: constr(regex=r'^\d{12}$') = Field(
        ..., description='12-digit identifier of the own AWS Account'
    )


class Type5(Enum):
    integer_2 = 2
    integer_3 = 3


class CreateCloudConnectVPNRequest(BaseModel):
    type: Type5
    name: str
    description: Optional[str] = None
    region: Optional[str] = None
    public_ip: str = Field(
        ..., description='the public ip of the VPN server to attach to'
    )
    psk: Optional[str] = Field(
        None,
        description='the PSK for the connection, if left empty it is generated by aws',
    )
    asn: Optional[int] = Field(
        None,
        description='if type = `3` is selected, this parameter must be specified and denotes the autonomous system number',
    )
    premise_cidr: List[str]
    inside_cidr: Optional[List[str]] = Field(
        None,
        description='up to 3 private ip address ranges denoting the BGP routers CIDR. if left empty, these are generated',
    )


class Currency8(BaseModel):
    id: Optional[int] = None


class CloudConnectCharge(BaseModel):
    id: Optional[int] = None
    breakout_type_id: Optional[int] = None
    amount: Optional[float] = None
    currency: Optional[Currency8] = None


class Currency9(BaseModel):
    id: Optional[int] = None


class ListCloudConnectPricesResponseItem(BaseModel):
    id: Optional[int] = None
    breakout_type_id: Optional[int] = None
    amount: Optional[float] = None
    currency: Optional[Currency9] = None


class ListCloudConnectPricesResponse(BaseModel):
    __root__: List[ListCloudConnectPricesResponseItem] = Field(
        ..., title='ListCloudConnectCustomResponse'
    )


class BreakoutTypeId(Enum):
    integer_1 = 1
    integer_2 = 2
    integer_3 = 3
    integer_4 = 4
    integer_5 = 5
    integer_6 = 6


class Currency10(BaseModel):
    id: Optional[int] = None


class CloudConnectCustomPriceRequest(BaseModel):
    breakout_type_id: BreakoutTypeId
    amount: float
    currency: Optional[Currency10] = None


class Region(BaseModel):
    Id: Optional[float] = None
    Name: Optional[str] = None
    Description: Optional[str] = None


class GetCloudConnectTransitGatewaysResponseItem(BaseModel):
    id: Optional[float] = None
    name: Optional[str] = None
    aws_transit_gateway_id: Optional[str] = None
    active: Optional[bool] = None
    organisation_id: Optional[float] = None
    region: Optional[Region] = None


class GetCloudConnectTransitGatewaysResponse(BaseModel):
    __root__: List[GetCloudConnectTransitGatewaysResponseItem] = Field(
        ..., title='GetCloudConnectTransitGatewaysResponse'
    )


class CreateCloudConnectTransitGatewaysRequest(BaseModel):
    name: Optional[str] = None
    region: Optional[str] = None
    aws_transit_gateway_id: Optional[str] = None
    active: Optional[bool] = None
    organisation_id: Optional[float] = None


class UpdateCloudConnectTransitGatewayByIdRequest(BaseModel):
    active: Optional[bool] = None


class GetCloudConnectBreakoutTypeWhitelistResponseItem(BaseModel):
    organisation_id: Optional[float] = None
    breakout_type_id: Optional[float] = None
    organisation_name: Optional[str] = None


class GetCloudConnectBreakoutTypeWhitelistResponse(BaseModel):
    __root__: List[GetCloudConnectBreakoutTypeWhitelistResponseItem] = Field(
        ..., title='GetCloudConnectBreakoutTypeWhitelistResponse'
    )


class Formfactor(BaseModel):
    name: Optional[str] = None
    id: Optional[float] = None


class SimModel(BaseModel):
    sim_type_id: Optional[str] = None
    description: Optional[str] = None
    sim_manufacturer_id: Optional[str] = None
    sim_formfactor_id: Optional[str] = None
    memory_size: Optional[str] = None
    formfactor: Optional[Formfactor] = None
