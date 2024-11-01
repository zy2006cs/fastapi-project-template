from tortoise.queryset import QuerySetSingle

from typing import Optional,List
from .models import User,Roles,Permissions
def to_dict(model:QuerySetSingle=None,fields_data:Optional[list]=None)->dict:

    model_keys = ['_partial', '_saved_in_db', '_custom_generated_pk', '_await_when_save']
    if fields_data is not None:
        model_keys+=fields_data
    data=model.__dict__
    for i in model_keys:
        del data[i]
    return data
def to_list_dict(modelLIst:List[QuerySetSingle],fields_data:Optional[list]=None)->List[dict]:
    data=[]
    for i in modelLIst:
        data.append(to_dict(i,fields_data=fields_data))
    return data