from pydantic import BaseModel
from emnify.modules.api.models import RetrieveSIMlistresponse


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


class SimUpdate(BaseModel):
    """
    Model for sim partial update
    """
    status: SimStatus = None
    issuer_organisation: IdModel = None
    reseller_organisation: IdModel = None
    customer_organisation: IdModel = None
