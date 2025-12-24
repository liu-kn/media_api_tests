from media_api_tests.settings import BASE_URL
import requests


def test_get_media_existing_admin(admin_headers):
    response = requests.get(
        f"{BASE_URL}/api/media/1",
        headers=admin_headers
    )
    assert response.status_code == 200


def test_get_media_existing_user(user_headers):
    response = requests.get(
        f"{BASE_URL}/api/media/1",
        headers=user_headers
    )
    assert response.status_code == 200

def test_get_media_nonexistent_admin(admin_headers):
        response = requests.get(
            f"{BASE_URL}/api/media/999999",
            headers=admin_headers
        )
        assert response.status_code == 404

def test_get_media_deleted_admin(admin_headers):
        response = requests.get(
            f"{BASE_URL}/api/media/2",
            headers=admin_headers
        )
        assert response.status_code == 404


def test_get_media_idempotent_admin(admin_headers):
    r1 = requests.get(f"{BASE_URL}/api/media/1", headers=admin_headers)
    r2 = requests.get(f"{BASE_URL}/api/media/1", headers=admin_headers)

    assert r1.status_code == 200
    assert r1.json() == r2.json()


def test_get_media_response_structure_admin(admin_headers):
    response = requests.get(
        f"{BASE_URL}/api/media/1",
        headers=admin_headers
    )

    body = response.json()

    # обязательные поля
    expected_fields = {
        "id",
        "url",
        "altText",
        "variant",
        "primary",
        "format",
        "widthPx",
        "heightPx",
        "sizeBytes",
        "sortOrder",
        "deleted",
        "createdAt",
    }

    assert expected_fields.issubset(body.keys())