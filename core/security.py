from fastapi.security.oauth2 import OAuth2PasswordBearer
from fastapi.exceptions import HTTPException
from fastapi import Depends,Request
from core.setting import conf
from datetime import timedelta, datetime
from typing import Dict
from db import User
from utils.encrypto import create_md5
from .Permissions import Permissions
from jwt import PyJWT

Scheme = OAuth2PasswordBearer(tokenUrl=conf.TOKEN_URL)

class Authentication(PyJWT):
    def __init__(self):
        self.key = conf.SERCT_KEY
        self.algorithm = conf.ALGORITHM
        super().__init__()
    def create_access_token(self, payload: Dict, expires=timedelta(hours=24)) -> str:
        payload['exp'] = (datetime.now() + expires).timestamp()
        payload = self.__create_signature__(payload)
        token = super().encode(payload=payload, key=self.key, algorithm=self.algorithm)
        return token
    def decode_token(self, token: str) -> Dict:
        algorithm_data = None
        if isinstance(self.algorithm, str):
            algorithm_data = [self.algorithm]
        else:
            raise HTTPException(status_code=401, detail={"code": 401, "message": 'Invalid token'})
        try:
            payload = super().decode(token, algorithms=algorithm_data, key=self.key)
            if payload['exp'] < datetime.now().timestamp():
                raise HTTPException(status_code=401, detail={'code': 401, 'message': 'JWT timeout'})
        except Exception:
            raise HTTPException(status_code=401, detail={'code': 401, 'message': "Token error "})

        signature = payload.get('signature')
        del payload['signature']
        payload = self.__create_signature__(payload)
        if signature != payload['signature']:
            raise HTTPException(status_code=401, detail={'code': 401, 'message': 'Signature error'})
        return payload

    def __create_signature__(self, payload: Dict) -> Dict[str, any]:
        text = ''
        for key, value in payload.items():
            text += str(key) + ';' + str(value)
        signature = create_md5(text)
        payload['signature'] = signature
        return payload

    async def Certification(self, request:Request,token: str = Depends(Scheme)) -> User:
        accessList=['all','add','delete','get','put','open']
        f=self.decode_token(token)
        route=request.scope.get("route")
        description: str = route.description
        key = description.split(':')
        permissions = Permissions()
        if len(key) < 2 or not (key[0] in accessList):
            raise HTTPException(status_code=403, detail={'message': '权限错误'})
        user = await permissions.get_username(f['username'])
        if key[0] == 'open':
            return user
        await permissions.get_rules(path=str(request.url).replace(str(request.base_url),'/'),user=user,rule=key[0])
        return user

'''
规则 all add delete get put open
'''

