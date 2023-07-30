from http import HTTPStatus

from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException, Body
from pydantic import BaseModel, Field, validator

from event_app.src.local.api import errors
from event_app.src.models.jwt import JWTPayload
from event_app.src.services.autorization import get_token_payload
from event_app.src.services.service_review import ReviewService, get_reviews_service

router = APIRouter()


class LikeReview(BaseModel):
    review_id: str = Field(title="ID Рецензии", example="64c046134ba01daa94d5e59c"
                           )
    value: int = Field(title="Лайк", ge=0, le=1, example=1)

    @validator('review_id')
    def validate_object_id(cls, id_value):
        if not ObjectId.is_valid(id_value):
            raise ValueError('id field must be a valid ObjectId')
        return id_value

    class Config:
        validate_all = True
        arbitrary_types_allowed = True


class ReviewsResponse(BaseModel):
    review_id: str | None = Field(title="ID Рецензии",
                                  example="64c046134ba01daa94d5e59c")
    status: bool = Field(title="Успех", example=True)


@router.post(
    "/",
    response_description="Add like review",
    response_model=ReviewsResponse,
    summary="Отправка события о лайке рецензии",
)
async def add_like_event(
        like_review: LikeReview = Body(...),
        jwt: None | JWTPayload = Depends(get_token_payload),
        review_service: ReviewService = Depends(get_reviews_service),
):
    if jwt is None:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED, detail=errors.NO_AUTHORIZED
        )
    user_id = jwt.user_id
    response = await review_service.send_review_like(user_id, like_review.review_id,
                                                     like_review.value)
    if response:
        return ReviewsResponse(review_id=like_review.review_id, status=True)
    else:
        raise HTTPException(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail=errors.SAVE_ERROR
        )
