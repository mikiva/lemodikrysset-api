from fastapi import FastAPI
from supertokens_python import init
from supertokens_python.framework.fastapi import get_middleware
from supertokens_python.recipe import thirdpartyemailpassword, session, dashboard, usermetadata
from supertokens_python import (
    InputAppInfo,
    SupertokensConfig,
)

from settings import AuthSettings


def init_auth(app: FastAPI):
    config = AuthSettings()
    init(
        supertokens_config=SupertokensConfig(
            connection_uri=config.connection_uri,
            api_key=config.api_key),
        app_info=InputAppInfo(
            app_name="Lemodikrysset API",
            api_domain=config.api_domain,
            website_domain=config.website_domain,
            api_base_path=config.api_base_path
        ),
        framework="fastapi",
        recipe_list=[
            session.init(),
            thirdpartyemailpassword.init(),
            dashboard.init(),
            usermetadata.init()
        ],
        mode="asgi",
    )
    app.add_middleware(get_middleware())
