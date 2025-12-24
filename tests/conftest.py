import pytest
import requests

from media_api_tests.settings import (
    BASE_URL,
    USER_PASSWORD,
    USER_EMAIL,
    ADMIN_PASSWORD,
    ADMIN_EMAIL,
)


def _login(email: str, password: str) -> dict:
    response = requests.post(
        f"{BASE_URL}/api/auth/login",
        json={"email": email, "password": password},
    )

    assert response.status_code == 200, f"Login failed: {response.status_code} {response.text}"

    token = response.json().get("accessToken")
    assert token, (f"No accessToken in response: {response.text}")

    return {"Authorization": f"Bearer {token}"}


@pytest.fixture(scope="session")
def admin_headers():
    return _login(ADMIN_EMAIL, ADMIN_PASSWORD)


@pytest.fixture(scope="session")
def user_headers():
    return _login(USER_EMAIL, USER_PASSWORD)

