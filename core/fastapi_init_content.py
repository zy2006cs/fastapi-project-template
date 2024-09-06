from .setting import conf
from tortoise import Tortoise
async def datebase_connect():
    await Tortoise.init({
        "connections": {
            "default": conf.DATABASE_URL
        },
        "apps": {
            "models": {
                "models": ["db.models"],
                "default_connection": "default",
            }
        }
    })
    await Tortoise.generate_schemas()
async def init():
    await datebase_connect()
    pass
async def shutdown():
    await Tortoise.close_connections()