from fastapi import APIRouter, Request, Response
from typing import Optional
from core.security import Authentication
from core.res import response_data, res_Model


class ServiceRouter(Authentication):
    auth = Authentication()

    def __init__(self, path: Optional[str] = None, routerInit: bool = True, data: dict = None):
        super().__init__()
        self.description = data.get('description', {}) if data else {}
        self.summary = data.get('summary', {}) if data else {}
        self.router = APIRouter()
        self.path = path
        self.res = response_data
        self.routerInit = routerInit
        self.methods = ['get', 'post', 'put', 'delete']

        if self.path and self.routerInit:
            self.setup_routes()

    def set_desc(self, val: str, key: str = "summary", method: str = 'get', routerInit: bool = False):
        """
        设置指定方法的描述或摘要。
        :param val: 要设置的值
        :param key: 'summary' 或 'description'
        :param method: HTTP 方法
        :param routerInit: 是否重新初始化路由
        """
        if key in ['summary', 'description']:
            current_data = getattr(self, key)
            current_data[method] = val
            setattr(self, key, current_data)

            if routerInit:
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
        for method in self.methods:
            if self.is_method_overridden(method):
                self.router.add_api_route(
                    path=self.path,
                    endpoint=getattr(self, method),
                    response_model=res_Model,
                    description=self.description.get(method),
                    summary=self.summary.get(method),
                    methods=[method.upper()]
                )

    def is_method_overridden(self, method_name: str) -> bool:
        current_method = getattr(self, method_name)
        parent_method = getattr(super(self.__class__, self), method_name, None)
        return current_method != parent_method
