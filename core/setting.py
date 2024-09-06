from typing import Optional,List
ALLOW_ORIGINS_DATA=['http://localhost:5173',]
CACHE_TIME=3600 #浏览器缓存时间 s

class Cors:
    ALLOW_ORIGINS:str=ALLOW_ORIGINS_DATA
    ALLOW_CREDENTIALS=True
    ALLOW_METHODS=["*",]
    ALLOW_HEADERS=['*',]
class Setting(Cors):
    HOST:str='0.0.0.0'
    PORT:int=8000
    DATABASE_URL:Optional[str]='sqlite:///test.db'
    REDIS_URL:Optional[str]='redis://localhost:6379/0'
    SERCT_KEY:str='adskc dscjiojdcwedkcskddfcecdfjhnjnsdcdiwkiwoskwposldx fcgvhbjmnk'
    ALGORITHM:str='HS256'#jwt校验算法
    CACHE_TIME:str="public, max-age={}".format(CACHE_TIME)
    MINIMUM_SIZE:int=1024
    TOKEN_URL:Optional[str]='/token'
    WRITER_LOG:bool=True#是否开启日志
    INDEX_URL:Optional[str]='http://127.0.0.1:{}/docs'.format(PORT)#常规错误视图跳转url
    GENERAL_STATUS_CODE_DATA:List=[404,400,500,405,502,404]#常规错误视图处理
conf=Setting()#oautu2获取access_token接口