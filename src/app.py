import logging
from typing import Any

import orjson
import uvicorn
from starlette.requests import Request
from starlette.responses import Response, JSONResponse

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


class ASGIApplication:
    def __init__(self, scope):
        assert scope["type"] == "http"
        self.scope = scope
        self.receive = None
        self.send = None

    async def __call__(self, receive, send):
        self.receive = receive
        self.send = send

        request = Request(self.scope, self.receive)

        if request.url.path == "/healthz":
            return await self.empty_response()

        return await self.response({"test": "test"})

    async def response(self, data):
        response = ORJSONResponse(data)
        return await response(self.scope, self.receive, self.send)

    async def empty_response(self):
        return await Response(status_code=200, content=b"")(self.scope, self.receive, self.send)


class ORJSONResponse(JSONResponse):
    def render(self, content: Any) -> bytes:
        return orjson.dumps(content)


if __name__ == "__main__":
    uvicorn.run(ASGIApplication, host="0.0.0.0", port=8000)
