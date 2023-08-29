from http import HTTPStatus

import pytest as pytest

from backend.tests.functional.testdata import jwt, reviews

pytestmark = pytest.mark.asyncio


@pytest.mark.parametrize(
    "query_data, expected_answer",
    [
        (
            {"review_id": reviews[0]["review_id"], "value": 1},
            {"status": True, "review_id": reviews[0]["review_id"]},
        ),
        (
            {"review_id": reviews[1]["review_id"], "value": 0},
            {"status": True, "review_id": reviews[1]["review_id"]},
        ),
        (
            {"review_id": reviews[2]["review_id"], "value": 1},
            {"status": True, "review_id": reviews[2]["review_id"]},
        ),
        (
            {"review_id": reviews[3]["review_id"], "value": 0},
            {"status": True, "review_id": reviews[3]["review_id"]},
        ),
    ],
)
@pytestmark
async def test_event_like(make_post_request, query_data, expected_answer):
    # Arrange
    headers = {
        "Authorization": f"Bearer {jwt}",
        "Content-Type": "application/json",
    }
    # Act
    response = await make_post_request("reviews", params=query_data, headers=headers)
    # Assert
    assert response["body"]["status"] == expected_answer["status"]
    assert response["body"]["review_id"] == expected_answer["review_id"]


@pytest.mark.parametrize(
    "query_data, expected_answer",
    [
        (
            {"review_id": reviews[0]["review_id"], "value": 1},
            {"status": HTTPStatus.UNAUTHORIZED},
        ),
        (
            {"review_id": reviews[1]["review_id"], "value": 0},
            {"status": HTTPStatus.UNAUTHORIZED},
        ),
        (
            {"review_id": reviews[2]["review_id"], "value": 1},
            {"status": HTTPStatus.UNAUTHORIZED},
        ),
        (
            {"review_id": reviews[3]["review_id"], "value": 0},
            {"status": HTTPStatus.UNAUTHORIZED},
        ),
    ],
)
@pytestmark
async def test_event_like_unauthorized(make_post_request, query_data, expected_answer):
    # Arrange
    # Act
    response = await make_post_request("reviews", params=query_data)
    # Assert
    assert response["status"] == expected_answer["status"]


@pytest.mark.parametrize(
    "query_data, expected_answer",
    [
        (
            {"review_id": reviews[0]["review_id"], "value": 10},
            {"status": HTTPStatus.UNPROCESSABLE_ENTITY},
        ),
        (
            {"review_id": reviews[1]["review_id"], "value": ""},
            {"status": HTTPStatus.UNPROCESSABLE_ENTITY},
        ),
        (
            {"review_id": reviews[2]["review_id"], "value": -1},
            {"status": HTTPStatus.UNPROCESSABLE_ENTITY},
        ),
        (
            {"review_id": reviews[3]["review_id"], "value": "sadsadas"},
            {"status": HTTPStatus.UNPROCESSABLE_ENTITY},
        ),
        ({"review_id": "", "value": 1}, {"status": HTTPStatus.UNPROCESSABLE_ENTITY}),
        (
            {"review_id": "asasfs", "value": 0},
            {"status": HTTPStatus.UNPROCESSABLE_ENTITY},
        ),
        ({"review_id": 1, "value": 1}, {"status": HTTPStatus.UNPROCESSABLE_ENTITY}),
        (
            {"review_id": "92336d84-e39d-4c43-a40b-565821551b21", "value": 0},
            {"status": HTTPStatus.UNPROCESSABLE_ENTITY},
        ),
    ],
)
@pytestmark
async def test_event_like_validation(make_post_request, query_data, expected_answer):
    # Arrange
    headers = {
        "Authorization": f"Bearer {jwt}",
        "Content-Type": "application/json",
    }
    # Act
    response = await make_post_request("reviews", params=query_data, headers=headers)
    # Assert
    assert response["status"] == expected_answer["status"]
