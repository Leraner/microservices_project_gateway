from typing import Any

import grpc


class ClientInterface:
    client: Any
    protos: Any


class ClientGRPCLoader:
    address: str
    path_to_proto: str

    @staticmethod
    def load_client(address, path_to_proto):
        # TODO: подумать над этим
        def load_client_inner(func):
            async def inner(*args, **kwargs):
                protos, services = grpc.protos_and_services(path_to_proto)  # type: ignore
                channel = grpc.aio.insecure_channel(address)
                stub_service_name = next(
                    filter(lambda x: "Stub" in x, services.__dict__)
                )
                client = services.__dict__[stub_service_name](channel)

                client_and_protos_object = ClientInterface()
                client_and_protos_object.__dict__.update(
                    {"client": client, "protos": protos}
                )
                return await func(*args, **kwargs, interface=client_and_protos_object)

            return inner

        return load_client_inner
