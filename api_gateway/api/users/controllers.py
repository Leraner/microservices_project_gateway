from grpc_loader import ClientGRPCLoader, ClientInterface
from settings import microservices
from uuid import UUID


class UserService(metaclass=ClientGRPCLoader):
    address: str = microservices["user"]["address"]
    path_to_proto: str = microservices["user"]["path_to_proto"]

    @ClientGRPCLoader.annotate
    async def create_user(self, name: str, surname: str, interface: ClientInterface):
        return await interface.client.CreateUser(
            interface.protos.CreateUserRequest(name=name, surname=surname),
            timeout=5,
        )

    @ClientGRPCLoader.annotate
    async def get_users(self, interface: ClientInterface):
        return await interface.client.GetUsers(
            interface.protos.GetUsersRequest(),
            timeout=5,
        )

    @ClientGRPCLoader.annotate
    async def get_user_by_id(self, user_id: UUID, interface: ClientInterface):
        return await interface.client.GetUserById(
            interface.protos.GetUserByIdRequest(id=str(user_id)),
            timeout=5,
        )

    @ClientGRPCLoader.annotate
    async def delete_user(self, user_id: UUID, interface: ClientInterface):
        return await interface.client.DeleteUser(
            interface.protos.DeleteUserRequest(id=str(user_id)),
            timeout=5,
        )
