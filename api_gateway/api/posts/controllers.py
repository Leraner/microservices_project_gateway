from grpc_loader import ClientGRPCLoader, ClientInterface
from settings import microservices
from uuid import UUID


class PostService(metaclass=ClientGRPCLoader):
    address: str = microservices["post"]["address"]
    path_to_proto: str = microservices["post"]["path_to_proto"]

    @ClientGRPCLoader.annotate
    async def get_posts(self, interface: ClientInterface):
        response = await interface.client.GetPosts(
            interface.protos.GetPostsRequest(),
            timeout=5,
        )
        return response

    @ClientGRPCLoader.annotate
    async def get_post_by_id(self, post_id: UUID, interface: ClientInterface):
        response = await interface.client.GetPostById(
            interface.protos.GetPostByIdRequest(id=str(post_id)), timeout=5
        )
        return response

    @ClientGRPCLoader.annotate
    async def create_post(
        self, author_id: UUID, title: str, interface: ClientInterface
    ):
        response = await interface.client.CreatePost(
            interface.protos.CreatePostRequest(author_id=str(author_id), title=title),
            timeout=5,
        )
        return response

    @ClientGRPCLoader.annotate
    async def delete_post(self, post_id: UUID, interface: ClientInterface):
        response = await interface.client.DeletePost(
            interface.protos.DeletePostRequest(id=str(post_id)),
            timeout=5,
        )
        return response
