import pytest
from utils.data_loader import load_users, load_api_endpoints


@pytest.mark.api
@pytest.mark.parametrize("user", load_users())
def test_user_data_validation(user):
    assert "name" in user
    assert "email" in user
    assert "age" in user
    assert "@" in user["email"]
    assert user["age"] > 0


@pytest.mark.api
@pytest.mark.parametrize("endpoint_data", load_api_endpoints())
def test_api_endpoints(http_session, api_base_url, endpoint_data):
    url = f"{api_base_url}{endpoint_data['endpoint']}"
    method = endpoint_data["method"]
    expected_status = endpoint_data["expected_status"]

    if method == "GET":
        response = http_session.get(url)

    assert response.status_code == expected_status

