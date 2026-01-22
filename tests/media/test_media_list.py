import requests
from media_api_tests.settings import BASE_URL


# ===== POSITIVE =====

def test_get_media_list_existing_entity_admin(admin_headers):
    response = requests.get(
        f"{BASE_URL}/api/media",
        params={"type": "YARN", "id": 1},
        headers=admin_headers
    )

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

    for item in data:
        assert item["deleted"] is False
        assert "id" in item
        assert "url" in item
        assert "variant" in item
        assert "primary" in item
        assert "format" in item
        assert "widthPx" in item
        assert "heightPx" in item
        assert "sizeBytes" in item
        assert "sortOrder" in item


def test_get_media_list_existing_entity_user(user_headers):
    response = requests.get(
        f"{BASE_URL}/api/media",
        params={"type": "YARN", "id": 1},
        headers=user_headers
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)


# ===== NEGATIVE =====

def test_get_media_list_existing_entity_without_media_admin(admin_headers):
    response = requests.get(
        f"{BASE_URL}/api/media",
        params={"type": "YARN", "id": 2},
        headers=admin_headers
    )

    assert response.status_code == 200
    assert response.json() == []


def test_get_media_list_nonexistent_entity(admin_headers):
    response = requests.get(
        f"{BASE_URL}/api/media",
        params={"type": "COLOR", "id": 999},
        headers=admin_headers
    )

    assert response.status_code == 200
    assert response.json() == []


def test_get_media_list_all_media_deleted(admin_headers):
    response = requests.get(
        f"{BASE_URL}/api/media",
        params={"type": "YARN", "id": 1},
        headers=admin_headers
    )

    assert response.status_code == 200
    assert response.json() == []


# ===== IDENTITY / STABILITY =====

def test_get_media_list_idempotent_admin(admin_headers):
    response_1 = requests.get(
        f"{BASE_URL}/api/media",
        params={"type": "YARN", "id": 1},
        headers=admin_headers
    )

    response_2 = requests.get(
        f"{BASE_URL}/api/media",
        params={"type": "YARN", "id": 1},
        headers=admin_headers
    )

    assert response_1.status_code == 200
    assert response_2.status_code == 200
    assert response_1.json() == response_2.json()
