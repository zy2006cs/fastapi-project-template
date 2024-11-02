from fastapi import HTTPException
from tortoise.queryset import Q
from db import User,Roles
class Permissions():
    async def get_username(self,username)-> User:
        user=await User.filter(username=username).first()
        if user is None:
            raise HTTPException(status_code=401,detail={'message':"用户不存在"})
        return user
    async def get_rules(self,path,rule,user:User):
        role = (await user.role)

        if len(role)==0:
            raise HTTPException(status_code=403,detail={'message':"权限不存在"})
        role=role[0]
        permissions = await role.permissions.filter(
            ( Q(rule="all") | Q(rule=rule) )& Q(path=path)
        ).all()
        if len(permissions)==0:
            raise HTTPException(status_code=403,detail={'message':'权限错误'})
        return permissions

