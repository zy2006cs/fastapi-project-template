import os
import importlib.util
from fastapi import FastAPI
from typing import Optional
def register_router(router,app:FastAPI,root:str,directory:str,router_path)->FastAPI:

    relative_dir = os.path.relpath(root, directory)
    if relative_dir != ".":
        full_router_path = os.path.join(router_path, relative_dir.replace(os.sep, "/"))
    else:
        full_router_path = router_path
    app.include_router(router, prefix=f"/{full_router_path.strip('/')}".replace('\\', '/'))
    return app

def auto_register_routes(app: FastAPI, router_path: Optional[str]=None, directory: str='src/'):
    if router_path is None:
        router_path=directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                module_path = os.path.join(root, file)
                module_name = os.path.splitext(os.path.relpath(module_path, directory))[0].replace(os.sep, ".")
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                if hasattr(module, "router"):
                    router = module.router
                    app=register_router(router,app,root,directory,router_path)
                if hasattr(module,'router_data'):
                    router_data = module.router_data
                    for router in router_data:
                        register_router(router,app,root,directory,router_path)
    return app