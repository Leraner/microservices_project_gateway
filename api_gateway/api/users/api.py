from google.protobuf.json_format import MessageToDict
from starlette.responses import JSONResponse
from .controllers import UserService
from ..base import BaseRouter


class UserRouter(BaseRouter):
    prefix = "/user"
    tags = ["users"]
    service = UserService()

    @classmethod
    async def post_create_user(cls, name: str, surname: str):
        user = await cls.service.create_user(name=name, surname=surname)
        return JSONResponse(MessageToDict(user))

    @classmethod
    async def get_users(cls):
        users = await cls.service.get_users()
        return JSONResponse(MessageToDict(users))

    @classmethod
    async def delete_user(cls, user_id: str):
        user = await cls.service.delete_user(user_id=user_id)
        return JSONResponse(MessageToDict(user))
