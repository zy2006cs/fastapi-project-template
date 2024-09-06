from fastapi import APIRouter, Request, Response
from typing import Optional
from core.res import response_data, res_Model
class ServiceRouter:
    def __init__(self, path: Optional[str] = None):
        self.router = APIRouter()
        self.path = path
        self.res=response_data
        if self.path:
            self.setup_routes()
    def get(self):
        return Response(content="1")
    def post(self):
        return Response(content="1")
    def delete(self):
        return Response(content="1")
    def put(self):
        return Response(content="1")
    def setup_routes(self):
        methods = ['get', 'post', 'put', 'delete']
        for method in methods:
            if self.is_method_overridden(method):
                self.router.add_api_route(
                    path=self.path,
                    endpoint=getattr(self, method),
                    response_model=res_Model,
                    methods=[method.upper()]
                )
    def is_method_overridden(self, method_name: str) -> bool:
        """
        检查指定方法是否在子类中被重写。
        :param method_name: 要检查的方法名称。
        :return: 如果子类重写了该方法，则返回 True；否则返回 False。
        """
        current_method = getattr(self, method_name)
        parent_method = getattr(super(self.__class__, self), method_name, None)
        return current_method != parent_method
