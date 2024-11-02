from db import to_dict,to_list_dict
from fastapi import Depends,Request
from utils.service import ServiceRouter
class UserRouter(ServiceRouter):
    def __init__(self):
        super().__init__('/userinfo',data={'description':{'get':'get:获取当前信息'}})
    async def get(self,user=Depends(ServiceRouter.auth.Certification)):
        role=(await user.role)[0]
        data=to_dict(user,fields_data=['password','create_time','_role'])
        data['role_id']=role.id
        data['name']=role.name
        return self.res(data=data)
