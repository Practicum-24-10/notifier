from http import HTTPStatus

import pytest as pytest

from backend.tests.functional.testdata import users

pytestmark = pytest.mark.asyncio


@pytest.mark.parametrize(
    "query_data, expected_answer",
    [
        (
                {"user_ids": users[0]["user_ids"],
                 "template_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                 "delay": False},
                {"status": True, "user_ids": users[0]["user_ids"]},
        ),
        (
                {"user_ids": users[1]["user_ids"],
                 "template_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                 "delay": False},
                {"status": True, "user_ids": users[1]["user_ids"]},
        ),
        (
                {"user_ids": users[2]["user_ids"],
                 "template_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                 "delay": True},
                {"status": True, "user_ids": users[2]["user_ids"]},
        ),
        (
                {"user_ids": users[3]["user_ids"],
                 "template_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                 "delay": True
                 },
                {"status": True, "user_ids": users[3]["user_ids"]},
        ),
    ],
)
@pytestmark
async def test_event(make_post_request, query_data, expected_answer):
    # Arrange
    body = {
        "user_ids": query_data["user_ids"],
        "template_id": query_data["template_id"],
        "delay": query_data["delay"]
    }
    # Act
    response = await make_post_request("event", params=body)
    # Assert
    assert response["body"]["status"] == expected_answer["status"]
    assert response["body"]["user_ids"] == expected_answer["user_ids"]


@pytest.mark.parametrize(
    "query_data, expected_answer",
    [
        (
                {"user_ids": users[0]["user_ids"],
                 "template_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                 "delay": ""},
                {"status": HTTPStatus.UNPROCESSABLE_ENTITY},
        ),
        (
                {"user_ids": users[1]["user_ids"],
                 "template_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                 "delay": "fdfsfs"},
                {"status": HTTPStatus.UNPROCESSABLE_ENTITY},
        ),
        (
                {"user_ids": users[2]["user_ids"],
                 "template_id": "fsdafasdf",
                 "delay": True},
                {"status": HTTPStatus.UNPROCESSABLE_ENTITY},
        ),
        (
                {"user_ids": users[3]["user_ids"],
                 "template_id": "",
                 "delay": True},
                {"status": HTTPStatus.UNPROCESSABLE_ENTITY},
        ),
        (
                {"user_ids": users[0]["user_ids"],
                 "template_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                 "delay": 11},
                {"status": HTTPStatus.UNPROCESSABLE_ENTITY},
        ),
        (
                {"user_ids": users[1]["user_ids"],
                 "template_id": 11,
                 "delay": True},
                {"status": HTTPStatus.UNPROCESSABLE_ENTITY},
        ),
        (
                {"user_ids": users[3]["user_ids"][0],
                 "template_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                 "delay": True},
                {"status": HTTPStatus.UNPROCESSABLE_ENTITY},
        ),
(
                {"user_ids": [],
                 "template_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                 "delay": True},
                {"status": HTTPStatus.UNPROCESSABLE_ENTITY},
        ),

(
                {"user_ids": 1,
                 "template_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                 "delay": True},
                {"status": HTTPStatus.UNPROCESSABLE_ENTITY},
        ),
(
                {"user_ids": "",
                 "template_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                 "delay": True},
                {"status": HTTPStatus.UNPROCESSABLE_ENTITY},
        ),
(
                {"user_ids": "rqew",
                 "template_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                 "delay": True},
                {"status": HTTPStatus.UNPROCESSABLE_ENTITY},
        ),
    ],
)
@pytestmark
async def test_event_signup_validation(make_post_request, query_data, expected_answer):
    # Arrange
    body = {
        "user_ids": query_data["user_ids"],
        "template_id": query_data["template_id"],
        "delay": query_data["delay"]
    }
    # Act
    response = await make_post_request("event", params=query_data)
    # Assert
    assert response["status"] == expected_answer["status"]
