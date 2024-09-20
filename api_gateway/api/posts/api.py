from google.protobuf.json_format import MessageToDict
from starlette.responses import JSONResponse
from .controllers import PostService
from ..base import BaseRouter
from uuid import UUID


class PostRouter(BaseRouter):
    prefix = "/posts"
    tags = ["posts"]
    service = PostService()

    @classmethod
    async def get_posts(cls):
        post = await cls.service.get_posts()
        return JSONResponse(MessageToDict(post))

    @classmethod
    async def get_post_by_id(cls, post_id: UUID):
        post = await cls.service.get_post_by_id(post_id)
        return JSONResponse(MessageToDict(post))

    @classmethod
    async def post_create_post(cls, author_id: UUID, title: str):
        post = await cls.service.create_post(author_id, title)
        return JSONResponse(MessageToDict(post))

    @classmethod
    async def delete_post(cls, post_id: UUID):
        post = await cls.service.delete_post(post_id)
        return JSONResponse(MessageToDict(post))
