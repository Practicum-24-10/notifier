import logging

import sentry_sdk
import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from sentry_sdk.integrations.fastapi import FastApiIntegration

from backend.src.api.v1.api_some import router as some_router
from backend.src.auth import rsa_key
from backend.src.auth.abc_key import RsaKey
from backend.src.core.config import DSN, PUBLIC_KEY, config
from backend.src.core.logger import LOGGING


if config.logging_on:
    sentry_sdk.init(dsn=DSN, integrations=[FastApiIntegration()])

    logging.basicConfig(**LOGGING)
    log = logging.getLogger(__name__)

app = FastAPI(
    title=config.project_name,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
)


@app.on_event("startup")
async def startup():
    rsa_key.pk = RsaKey(path=PUBLIC_KEY, algorithms=["RS256"])


@app.on_event("shutdown")
async def shutdown():
    pass

app.include_router(some_router, prefix="/api/v1/some", tags=["some"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
