import functools
from typing import Any, Callable, Awaitable

import grpc


class ClientInterface:
    client: Any
    protos: Any


class ClientGRPCLoader:
    address: str
    path_to_proto: str

    @classmethod
    def load_client(cls, func):

        async def inner(*args, **kwargs):
            protos, services = grpc.protos_and_services(cls.path_to_proto)  # type: ignore
            channel = grpc.aio.insecure_channel(cls.address)
            stub_service_name = next(filter(lambda x: "Stub" in x, services.__dict__))
            client = services.__dict__[stub_service_name](channel)

            client_and_protos_object = ClientInterface()
            client_and_protos_object.__dict__.update(
                {"client": client, "protos": protos}
            )
            return await func(*args, **kwargs, interface=client_and_protos_object)

        return inner
