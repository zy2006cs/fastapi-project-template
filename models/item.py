from typing import Union,Dict,List,Optional
from pydantic import BaseModel
class Res(BaseModel):
    code:int
    message:str
    data:Union[List,Dict]
    timestamp:str
    error:Optional[str]=None

