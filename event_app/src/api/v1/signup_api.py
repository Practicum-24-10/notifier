from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Body, Depends, HTTPException
from pydantic import BaseModel, Field

from event_app.src.local.api import errors
from event_app.src.services.service_signup import SignUpService, get_signup_service

router = APIRouter()


class SignUp(BaseModel):
    user_id: UUID = Field(
        title="ID пользователя", example="3fa85f64-5717-4562-b3fc-2c963f66afa6"
    )
    email: str = Field(title="Email", example="example@mail.ru")


class SignUpResponse(BaseModel):
    user_id: UUID | None = Field(
        title="ID пользователя", example="3fa85f64-5717-4562-b3fc-2c963f66afa6"
    )
    status: bool = Field(title="Успех", example=True)


@router.post(
    "/",
    response_description="Registration",
    response_model=SignUpResponse,
    summary="Отправка события о регистрации",
)
async def add_registration_event(
    registration: SignUp = Body(...),
    signup_service: SignUpService = Depends(get_signup_service),
):
    response = await signup_service.send_signup(
        registration.user_id, registration.email
    )
    if response:
        return SignUpResponse(user_id=registration.user_id, status=True)
    else:
        raise HTTPException(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail=errors.SAVE_ERROR
        )
