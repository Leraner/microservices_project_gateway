from typing import Any, Callable

import grpc


class ClientInterface:
    client: Any
    protos: Any


class ClientGRPCLoader(type):
    __attrs = {}

    def __new__(cls, name: str, bases: tuple, dct: dict) -> type:
        cls.__attrs |= {
            "address": dct.get("address", None),
            "path_to_proto": dct.get("path_to_proto", None),
        }

        if any(map(lambda x: cls.__attrs[x], cls.__attrs)) is None:
            raise Exception("Missing required attributes")

        for method_name, method in dct.items():
            if callable(method):
                dct[method_name] = cls.load_client(
                    method, cls.__attrs["address"], cls.__attrs["path_to_proto"]
                )
        return super().__new__(cls, name, bases, dct)

    @staticmethod
    def annotate(func) -> Callable:
        async def inner(*args, **kwargs):
            return await func(*args, **kwargs)

        return inner

    @staticmethod
    def load_client(func, address: str, path_to_proto: str):
        async def inner(*args, **kwargs):
            protos, services = grpc.protos_and_services(path_to_proto)  # type: ignore
            channel = grpc.aio.insecure_channel(address)
            stub_service_name = next(filter(lambda x: "Stub" in x, services.__dict__))
            client = services.__dict__[stub_service_name](channel)

            client_and_protos_object = ClientInterface()
            client_and_protos_object.__dict__.update(
                {"client": client, "protos": protos}
            )
            return await func(*args, **kwargs, interface=client_and_protos_object)

        return inner
