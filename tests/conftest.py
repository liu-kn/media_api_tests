import pytest
import requests
from media_api_tests.settings import (
    BASE_URL,
    ADMIN_EMAIL, ADMIN_PASSWORD,
    USER_EMAIL, USER_PASSWORD
)


@pytest.fixture
def base_url():
    return BASE_URL


def _login(email, password):
    response = requests.post(
        f"{BASE_URL}/api/auth/login",
        json={"email": email, "password": password}
    )
    assert response.status_code == 200, f"Login failed: {response.text}"
    token = response.json().get("access_token")
    assert token, "No access_token in login response"
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def admin_headers():
    """Хедеры с токеном админа."""
    return _login(ADMIN_EMAIL, ADMIN_PASSWORD)


@pytest.fixture
def user_headers():
    """Хедеры с токеном обычного пользователя."""
    return _login(USER_EMAIL, USER_PASSWORD)

