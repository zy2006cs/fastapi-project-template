import importlib.util,os
from fastapi import FastAPI
from typing import Optional
from utils.service import ServiceRouter
'''
1.3 增加了ServiceRouter的支持
'''
def register_router(router, app: FastAPI, root: str, directory: str, router_path) -> FastAPI:
    relative_dir = os.path.relpath(root, directory)
    full_router_path = router_path
    if relative_dir != ".":
        full_router_path = os.path.join(router_path, relative_dir.replace(os.sep, "/"))

    app.include_router(router, prefix=f"/{full_router_path.strip('/')}".replace('\\', '/'))
    return app

def auto_register_routes(app: FastAPI, router_path: Optional[str]=None, directory: str='src/'):
    if router_path is None:
        router_path = directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                module_path = os.path.join(root, file)
                module_name = os.path.splitext(os.path.relpath(module_path, directory))[0].replace(os.sep, ".")
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                for attr in dir(module):
                    cls = getattr(module, attr)
                    if isinstance(cls, type) and issubclass(cls, ServiceRouter) and cls is not ServiceRouter:
                        instance = cls()
                        register_router(instance.router,app,root,directory,router_path)
                if hasattr(module, "router"):
                    router = module.router
                    if isinstance(router,ServiceRouter):
                        continue
                    app = register_router(router, app, root, directory, router_path)
    return app
