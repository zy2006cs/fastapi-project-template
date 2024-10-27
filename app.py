from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn
from middleware.middleware import MutilAMiddleware, LogMiddleware
from core.router import auto_register_routes
from core.fastapi_init_content import init, shutdown
from handlers.except_view import General_Error_View
from core.security import conf
def create_app() -> FastAPI:
    app = FastAPI(docs_url=conf.DOCS_URL if conf.DOCS_URL is not None else None)
    setup_middlewares(app)
    setup_event_handlers(app)
    setup_exception_handlers(app)
    setup_static_files(app)
    register_routes(app)
    return app
def setup_middlewares(app: FastAPI):
    app.add_middleware(MutilAMiddleware)
    app.add_middleware(GZipMiddleware, minimum_size=conf.MINIMUM_SIZE)
    app.add_middleware(LogMiddleware)
def setup_event_handlers(app: FastAPI):
    app.add_event_handler('startup', init)
    app.add_event_handler('shutdown', shutdown)
def setup_exception_handlers(app: FastAPI):
    for status_code in conf.GENERAL_STATUS_CODE_DATA:
        app.add_exception_handler(status_code, General_Error_View)
def setup_static_files(app: FastAPI):
    app.mount("/static", StaticFiles(directory="static"), name="static")
def register_routes(app: FastAPI):
    auto_register_routes(app, directory='src/api', router_path='/api')
app = create_app()

if __name__ == '__main__':
    uvicorn.run(app, host=conf.HOST, port=conf.PORT)
