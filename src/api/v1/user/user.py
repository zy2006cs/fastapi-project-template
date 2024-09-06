from fastapi import  Depends
from core.security import auth
from utils.service import ServiceRouter
from utils.redis_cli import get_redis_client,RedisClient
class UserRouter(ServiceRouter):
    def __init__(self):
        super().__init__('/users')

    def get(self,):

        return self.res(data=['成功'])
class UserInfoRouter(ServiceRouter):
    def __init__(self):
        super().__init__('/user_info')
    async def get(self,data: dict = Depends(auth.Certification)):
        return self.res(data=['成功'])
router_data=[UserRouter().router,UserInfoRouter().router]
#批量注册
#单个注册直接router=xxxx
'''
只有使用router_data和router才能进行注册
'''
