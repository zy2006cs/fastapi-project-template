from redis.asyncio import Redis
from core.setting import conf
from fastapi.exceptions import HTTPException
from typing import Optional,Awaitable
import random,uuid
class RedisClient:
    def __init__(self,):
         self.redis_url=conf.REDIS_URL
    async def connect(self):
        if self.redis_url is None:
            raise HTTPException(status_code=500,detail={'message':'redis connection error'})
        self.redis = Redis.from_url(self.redis_url)

    async def close(self):
        if self.redis:
            await self.redis.aclose()
    async def set(self, key, value,timeout:Optional[int]=None,min:int=100,max:int=200):
        if timeout is None:
            res= self.redis.setex(key,random.randint(min,max),value)
            return res
        res= self.redis.setex(key,timeout,value)
        return res
    async def get_lock(self,key:str,lock_value:Optional[bool]=False):
        if not lock_value:
            lock=self.redis.lock(uuid.uuid4(),timeout=5)
            async with lock:
                value=self.redis.get(key)
            return value
        value=self.redis.get(key)
        return value

async def get_redis_client() -> RedisClient:
    client = RedisClient()
    await client.connect()
    try:
        yield client
    finally:
        await client.close()