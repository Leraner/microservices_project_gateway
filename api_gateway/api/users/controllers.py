from grpc_loader import ClientGRPCLoader, ClientInterface
from settings import microservices


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
    async def delete_user(self, user_id: str, interface: ClientInterface):
        return await interface.client.DeleteUser(
            interface.protos.DeleteUserRequest(id=user_id),
            timeout=5,
        )
