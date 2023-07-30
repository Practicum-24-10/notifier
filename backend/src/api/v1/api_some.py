from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException

from backend.src.local.api.v1 import authorization as errors
from backend.src.models.jwt import JWTPayload
from backend.src.services.autorization import get_token_payload


router = APIRouter()


@router.get(
    "/",
    response_description="Some description",
    summary="Summary",
)
async def get_some(
    jwt: None | JWTPayload = Depends(get_token_payload),
):
    if jwt is None:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED, detail=errors.NO_AUTHORIZED
        )

    return {'key': 'value'}

x = 'ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc'