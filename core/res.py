from fastapi.responses import Response
from typing import Optional, Union, Dict, List
from models.responseModel import Res as res_Model
from datetime import datetime
def response_data(
        data: Optional[Union[Dict, List]]=None,
        code: int = 200,
        message: str = 'success',
        mimetype: str = 'application/json',
        cache_bool: bool = False,
        ck_data: Optional[Dict] = None,
        response:Optional[Response]=None,

) -> Response:
    if response is not None:
        return response
    res_content = res_Model(
        message=message,
        data=data,
        code=code,
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M"),
    )
    if res_content.code !=200:
        res_content.error=res_content.message
        res_content.message=None
    content=res_content.json()
    response = Response(
        content=content,
        status_code=code,
        media_type=mimetype
    )
    if ck_data is not None:
        keys=ck_data.keys()
        for key in keys:
            response.set_cookie(key, ck_data[key])
    if (cache_bool):
        response.headers['cache'] = 'hsdhfsd'
    return response
