from utils.service import ServiceRouter
from db import User,Roles
from models.loginData import LoginData
class LoginRouter(ServiceRouter):
    def __init__(self):
        super().__init__(path='/login',routerInit=False)
        super().set_desc(val='登录',routerInit=True)
    async def post(self,data:LoginData):
        user=await User.filter(username=data.username).first()
        if user is None:
            return self.res(message='当前用户不存在',code=402)
        if data.password!=user.password:
            return self.res(message='密码错误',code=402)
        token=self.create_access_token(payload={'username':user.username})
        return self.res(message='登录成功',data={"token":token})
class RegisterRouter(ServiceRouter):
    def __init__(self):
        super().__init__('/register',routerInit=False)
        super().set_desc(val='注册',method='post',routerInit=True)
    async def post(self,data:LoginData):
        user=await User.filter(username=data.username).first()
        if user is not None:
            return self.res(message='当前账号已经存在',code=402)
        role=await Roles.filter(name="管理员").first()
        user=await User.create(username=data.username,password=data.password)
        await user.role.add(role)
        token = self.create_access_token(payload={'username': data.username})
        return self.res(message='登录成功', data={"token": token})
