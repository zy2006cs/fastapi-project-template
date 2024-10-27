from fastapi import Request
from starlette.exceptions import HTTPException
from core.res import response_data
from core.setting import conf
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")
async def General_Error_View(request: Request, exc: HTTPException):
    try:
        if exc.status_code in conf.GENERAL_STATUS_CODE_DATA:
            return templates.TemplateResponse("error/index.html", {"request": request, "status_code":exc.status_code,'url':conf.INDEX_URL})
    except AttributeError:
        return response_data(code=500,message=str(exc))