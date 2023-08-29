from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Body, Depends, HTTPException
from pydantic import BaseModel, Field

from backend.src.local.api import errors
from backend.src.services.service_event import EventService, get_event_service

router = APIRouter()


class Event(BaseModel):
    user_ids: list[UUID] = Field(
        title="ID пользователей", example=["3fa85f64-5717-4562-b3fc-2c963f66afa6"]
    )
    template_id: UUID = Field(
        title="ID Шаблона", example="3fa85f64-5717-4562-b3fc-2c963f66afa6"
    )
    delay: bool = Field(title="Задержка", example=False)


class EventResponse(BaseModel):
    user_ids: list[UUID] | None = Field(
        title="ID пользователей", example=["3fa85f64-5717-4562-b3fc-2c963f66afa6"]
    )
    status: bool = Field(title="Успех", example=True)


@router.post(
    "/",
    response_description="Add event",
    response_model=EventResponse,
    summary="Отправка события",
)
async def add_event(
    event: Event = Body(...),
    event_service: EventService = Depends(get_event_service),
):
    response = await event_service.send_event(
        event.user_ids, event.template_id, event.delay
    )
    if response:
        return EventResponse(user_ids=event.user_ids, status=True)
    else:
        raise HTTPException(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail=errors.SAVE_ERROR
        )
