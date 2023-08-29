from http import HTTPStatus

import pytest as pytest

from backend.tests.functional.testdata import users

pytestmark = pytest.mark.asyncio


@pytest.mark.parametrize(
    "query_data, expected_answer",
    [
        (
            {"user_id": users[0]["user_id"], "email": users[0]["email"]},
            {"status": True, "user_id": users[0]["user_id"]},
        ),
        (
            {"user_id": users[1]["user_id"], "email": users[1]["email"]},
            {"status": True, "user_id": users[1]["user_id"]},
        ),
        (
            {"user_id": users[2]["user_id"], "email": users[2]["email"]},
            {"status": True, "user_id": users[2]["user_id"]},
        ),
        (
            {"user_id": users[3]["user_id"], "email": users[3]["email"]},
            {"status": True, "user_id": users[3]["user_id"]},
        ),
    ],
)
@pytestmark
async def test_event_signup(make_post_request, query_data, expected_answer):
    # Arrange
    # Act
    response = await make_post_request("signup", params=query_data)
    # Assert
    assert response["body"]["status"] == expected_answer["status"]
    assert response["body"]["user_id"] == expected_answer["user_id"]


@pytest.mark.parametrize(
    "query_data, expected_answer",
    [
        (
            {"user_id": "", "email": users[0]["email"]},
            {"status": HTTPStatus.UNPROCESSABLE_ENTITY},
        ),
        (
            {"user_id": 5, "email": users[1]["email"]},
            {"status": HTTPStatus.UNPROCESSABLE_ENTITY},
        ),
        (
            {"user_id": "dfsdfd", "email": users[2]["email"]},
            {"status": HTTPStatus.UNPROCESSABLE_ENTITY},
        ),
        (
            {
                "user_id": "92336d84-e39d-4c43-a40b-565821551b2",
                "email": users[3]["email"],
            },
            {"status": HTTPStatus.UNPROCESSABLE_ENTITY},
        ),
        (
            {"user_id": users[0]["user_id"], "email": ""},
            {"status": HTTPStatus.UNPROCESSABLE_ENTITY},
        ),
        (
            {"user_id": users[1]["user_id"], "email": 1},
            {"status": HTTPStatus.UNPROCESSABLE_ENTITY},
        ),
        (
            {"user_id": users[2]["user_id"], "email": "fasdfsad"},
            {"status": HTTPStatus.UNPROCESSABLE_ENTITY},
        ),
        (
            {"user_id": users[3]["user_id"], "email": "fsda@mail"},
            {"status": HTTPStatus.UNPROCESSABLE_ENTITY},
        ),
    ],
)
@pytestmark
async def test_event_signup_validation(make_post_request, query_data, expected_answer):
    # Arrange
    # Act
    response = await make_post_request("signup", params=query_data)
    # Assert
    assert response["status"] == expected_answer["status"]
