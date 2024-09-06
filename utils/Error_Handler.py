from fastapi import FastAPI
from typing import Callable
def registrer_Error_Handler(app: FastAPI,error_fun:Callable,code_data:list):
    if len(code_data)==0:
        return ;
    i=0
    app.add_exception_handler(code_data[i],error_fun)
    data=code_data.copy()
    del data[i]
    if len(data)==0:
        return app;
    return registrer_Error_Handler(app,error_fun,data)

