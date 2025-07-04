import pytest


@pytest.mark.api
@pytest.mark.parametrize(
    "endpoint", ["/users", "/posts", "/comments", "/albums", "/photos", "/todos"]
)
def test_endpoint_accessibility(http_session, api_base_url, endpoint):
    response = http_session.get(f"{api_base_url}{endpoint}")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0


@pytest.mark.api
@pytest.mark.parametrize(
    "post_id,expected_comments",
    [
        (1, 5),
        (2, 5),
    ],
)
def test_post_comments_count(http_session, api_base_url, post_id, expected_comments):
    response = http_session.get(f"{api_base_url}/posts/{post_id}/comments")
    assert response.status_code == 200
    comments = response.json()
    assert len(comments) == expected_comments
