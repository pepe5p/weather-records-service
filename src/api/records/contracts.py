from pydantic import AwareDatetime, BaseModel


class RecordData(BaseModel):
    when: AwareDatetime
    temperature: float
    pressure: float


class RecordDataWithDeviceId(RecordData):
    device_id: int


class RecordCreateRequest(BaseModel):
    device_id: int
    encrypted_message: str
