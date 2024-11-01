from pydantic import BaseModel,field_validator
from utils.encrypto import create_sha256
import re
class LoginData(BaseModel):
    username: str
    password: str
    @field_validator('password')
    def validate_password(cls, value):
        value=create_sha256(value)
        return value
    @field_validator('username')
    def validate_username(cls, value):

        return value