"""Application configuration - FastAPI."""
from pydantic import BaseSettings

from auth.config.database import MongoSettings
from auth.version import __version__

import os
from pathlib import Path

from dotenv import load_dotenv

default_dot_env_path = Path(os.path.abspath(os.path.dirname(__file__))).parent.parent.absolute().joinpath(".env")
load_dotenv(os.getenv("DOTENV_PATH", default_dot_env_path))


class Application(BaseSettings):
    """Define application configuration model.

    Constructor will attempt to determine the values of any fields not passed
    as keyword arguments by reading from the environment. Default values will
    still be used if the matching environment variable is not set.

    Environment variables:
        * FASTAPI_DEBUG
        * FASTAPI_PROJECT_NAME
        * FASTAPI_VERSION
        * FASTAPI_DOCS_URL
        * FASTAPI_USE_REDIS

    Attributes:
        DEBUG (bool): FastAPI logging level. You should disable this for
            production.
        PROJECT_NAME (str): FastAPI project name.
        VERSION (str): Application version.
        DOCS_URL (str): Path where swagger ui will be served at.
        USE_REDIS (bool): Whether or not to use Redis.

    """

    DEBUG: bool = True
    PROJECT_NAME: str = "auth"
    VERSION: str = __version__
    DOCS_URL: str = "/"
    USE_REDIS: bool = False
    # All your additional application configuration should go either here or in
    # separate file in this submodule.
    mongo_settings: MongoSettings = MongoSettings()

    AUTH_REDIRECT_URI: str = "http://localhost:8001/auth/callback"
    JWT_SECRET: str

    class Config:
        """Config sub-class needed to customize BaseSettings settings.

        Attributes:
            case_sensitive (bool): When case_sensitive is True, the environment
                variable names must match field names (optionally with a prefix)
            env_prefix (str): The prefix for environment variable.

        Resources:
            https://pydantic-docs.helpmanual.io/usage/settings/

        """

        case_sensitive = True


settings = Application()
