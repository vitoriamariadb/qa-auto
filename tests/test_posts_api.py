import pytest

@pytest.mark.api
def test_get_posts(http_session, api_base_url):
    response = http_session.get(f"{api_base_url}/posts")
    assert response.status_code == 200
    posts = response.json()
    assert len(posts) > 0

@pytest.mark.api
def test_get_post_by_id(http_session, api_base_url):
    post_id = 1
    response = http_session.get(f"{api_base_url}/posts/{post_id}")
    assert response.status_code == 200
    post = response.json()
    assert post["id"] == post_id
    assert "title" in post
    assert "body" in post

@pytest.mark.api
def test_get_post_comments(http_session, api_base_url):
    post_id = 1
    response = http_session.get(f"{api_base_url}/posts/{post_id}/comments")
    assert response.status_code == 200
    comments = response.json()
    assert len(comments) > 0
    assert all(comment["postId"] == post_id for comment in comments)
