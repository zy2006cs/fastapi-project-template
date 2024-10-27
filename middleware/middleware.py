from fastapi import  Request
from starlette.middleware.base import BaseHTTPMiddleware
from core.setting import conf
from datetime import datetime
import os,aiofiles,re
class MutilAMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers['Access-Control-Allow-Origin'] = ', '.join(conf.ALLOW_ORIGINS)
        response.headers['Access-Control-Allow-Methods'] = ', '.join(conf.ALLOW_METHODS)
        response.headers['Access-Control-Allow-Headers'] = ', '.join(conf.ALLOW_HEADERS)
        cache=response.headers.get('cache')
        body_size=0
        if cache is not None or body_size >= 1024:
           del response.headers['cache']
           response.headers['Cache-Control'] = conf.CACHE_TIME
        if conf.ALLOW_CREDENTIALS:
             response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response


class LogMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
    async def dispatch(self, request: Request, call_next):
        request_info=f"请求方法: {request.method} \t请求url:{request.url}"
        response = await call_next(request)
        if conf.WRITER_LOG:
            path=os.path.join(os.getcwd(),'log',(datetime.now().strftime('%Y-%m-%d'))+'.log')
            async with aiofiles.open(path,'a',encoding='utf-8') as f:
                await f.write("请求时间:{}\t".format(datetime.now().strftime("%Y-%m-%d, %H:%M:%S"))+request_info+'\t状态码:{}'.format(response.status_code)+'\n')
        return response

