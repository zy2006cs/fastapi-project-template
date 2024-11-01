from urllib.request import Request

from fastapi import Depends
from utils.service import ServiceRouter
def get():
    return '111'
class UserRouter(ServiceRouter):
    def __init__(self):
        super().__init__('/users',data={'description':{'post':'open:获取当前信息'},'summary':{"get":"测试接口1"}})
    async def post(self,jwt=Depends(ServiceRouter.auth.Certification)):

        return self.res()

