import fastapi
from api import UserRouter, PostRouter
from exceptions import ExceptionHandlers

app = fastapi.FastAPI()


routers = [
    UserRouter,
    PostRouter,
]


for exception_handler in ExceptionHandlers.exceptions:
    app.add_exception_handler(
        ExceptionHandlers.exceptions[exception_handler],
        getattr(ExceptionHandlers, exception_handler),
    )

for router in routers:
    app.include_router(router.create_router())
