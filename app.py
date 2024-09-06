from fastapi import FastAPI,Request
from core.setting import conf
from middleware.middleware import MutilAMiddleware,LogMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from core.router import auto_register_routes
from core.fastapi_init_content import init,shutdown
from handlers.except_view import General_Error_View
from fastapi.staticfiles import StaticFiles
app=FastAPI()
app.add_middleware(MutilAMiddleware)
app.add_middleware(GZipMiddleware,minimum_size=conf.MINIMUM_SIZE)
app.add_middleware(LogMiddleware)
app.add_event_handler('startup', init)
app.add_event_handler('shutdown', shutdown)
for i in conf.GENERAL_STATUS_CODE_DATA:
   app.add_exception_handler(i,General_Error_View)

app.mount("/static", StaticFiles(directory="static"), name="static")
auto_register_routes(app,directory='src/api',router_path='/api')
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host=conf.HOST, port=conf.PORT)