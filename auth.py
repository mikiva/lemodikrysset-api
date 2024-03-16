from typing import Dict, Any

from fastapi import FastAPI, Request, Depends
from supertokens_python import init
from supertokens_python.framework.fastapi import get_middleware
from supertokens_python.ingredients.emaildelivery.types import EmailDeliveryConfig
from supertokens_python.recipe import thirdpartyemailpassword, session, dashboard, usermetadata, emailverification
from supertokens_python.recipe.emailverification import EmailVerificationClaim
from supertokens_python.recipe.session import SessionContainer
from supertokens_python.recipe.session.framework.fastapi import verify_session
from supertokens_python.recipe.thirdpartyemailpassword.types import EmailDeliveryOverrideInput, EmailTemplateVars
from supertokens_python import (
    InputAppInfo,
    SupertokensConfig,
)
from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth")
from settings import AuthSettings


@auth_router.post("/u/email/send")
async def send_verififaction_email(request: Request, sess: SessionContainer = Depends(verify_session(
    override_global_claim_validators=lambda global_validators, session, user_context: [
        validators for validators in global_validators if validators.id != EmailVerificationClaim.key]
))):
    body = {
        "rid": "emailverification",
        "apiBasePath": f"{request.base_url}verify-email"

    }
    print(sess.get_user_id())
    #requests.post(auth_url, data=body)


@auth_router.get("/u/email/verify")
async def verify_email(token: str):
    print(token)

    return "ok"


def custom_email_delivery(original_implementation: EmailDeliveryOverrideInput) -> EmailDeliveryOverrideInput:
    original_send_email = original_implementation.send_email

    async def send_email(template_vars: EmailTemplateVars, user_context: Dict[str, Any]) -> None:
        # This is: `${websiteDomain}${websiteBasePath}/verify-email`
        #template_vars.email_verify_link = template_vars.email_verify_link.replace(
        #    "http://localhost:3390/auth/verify-email", "http://localhost:3390/api/v1/auth/user/email/verify")

        return await original_send_email(template_vars, user_context)

    original_implementation.send_email = send_email
    return original_implementation


def init_auth(app: FastAPI):
    config = AuthSettings()
    init(
        supertokens_config=SupertokensConfig(
            connection_uri=config.connection_uri,
            api_key=config.api_key),
        app_info=InputAppInfo(
            app_name="Lemodikrysset",
            api_domain=config.api_domain,
            website_domain=config.website_domain,
            api_base_path=config.api_base_path
        ),
        framework="fastapi",
        recipe_list=[
            emailverification.init(mode="OPTIONAL"),
            thirdpartyemailpassword.init(),
            dashboard.init(),
            usermetadata.init(),
            session.init()
        ],
        mode="asgi",
    )
    app.add_middleware(get_middleware())
    app.include_router(auth_router, prefix="/api/v1")
