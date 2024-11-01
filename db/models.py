from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(unique=True, max_length=10)
    password = fields.CharField(max_length=256)
    create_time=fields.DatetimeField(auto_now_add=True)
    role = fields.ManyToManyField("models.Roles", related_name="user")

    class Meta:
        table = 'user'

class Roles(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(unique=True, max_length=10)
    permissions = fields.ManyToManyField("models.Permissions", related_name="role")
    description = fields.TextField()
    class Meta:
        table = 'role'

class Permissions(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=10)
    rule = fields.CharField(max_length=10,default='all')
    path=fields.CharField(max_length=30)
    class Meta:
        table = 'permission'
