"""Application implementation - ASGI."""
import logging

from fastapi import FastAPI
from auth.config import settings
from auth.app.router import root_api_router
from auth.app.exceptions import (
    HTTPException,
    http_exception_handler,
)


log = logging.getLogger(__name__)


async def on_startup():
    """Define FastAPI startup event handler.

    Resources:
        1. https://fastapi.tiangolo.com/advanced/events/#startup-event

    """
    log.debug("Execute FastAPI startup event handler.")
    pass


async def on_shutdown():
    """Define FastAPI shutdown event handler.

    Resources:
        1. https://fastapi.tiangolo.com/advanced/events/#shutdown-event

    """
    log.debug("Execute FastAPI shutdown event handler.")
    # Gracefully close utilities.
    pass


def get_application():
    """Initialize FastAPI application.

    Returns:
       FastAPI: Application object instance.

    """
    log.debug("Initialize FastAPI application node.")
    app = FastAPI(
        title=settings.PROJECT_NAME,
        debug=settings.DEBUG,
        version=settings.VERSION,
        docs_url=settings.DOCS_URL,
        on_startup=[on_startup],
        on_shutdown=[on_shutdown],
    )
    log.debug("Add application routes.")
    app.include_router(root_api_router)
    log.debug("Register global exception handler for custom HTTPException.")
    app.add_exception_handler(HTTPException, http_exception_handler)

    return app
