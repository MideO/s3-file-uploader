import logging
import os.path
from logging.config import dictConfig

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from prometheus_fastapi_instrumentator import Instrumentator
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import RedirectResponse

from dependency_factory import dependencies
from routers import index

app_config = dependencies.config
middleware = [Middleware(SessionMiddleware, secret_key=app_config.secret)]
dictConfig(app_config.logging.config)

app = FastAPI(middleware=middleware)

cur_dir = os.path.dirname(__file__)
app.mount(
    "/static",
    StaticFiles(directory=os.path.join(cur_dir, "static/"), html=True),
    name="static",
)
app.include_router(index.router)


@app.exception_handler(404)
async def custom_404_handler(_, __):
    return RedirectResponse("/")


# Instrument the FastAPI app to expose Prometheus metrics
Instrumentator().instrument(app).expose(app)

LOG = logging.getLogger("app")

if __name__ == "__main__":
    LOG.info("App running at %s", app_config.app.url)
    uvicorn.run(app, host=app_config.app.host, port=app_config.app.port)
