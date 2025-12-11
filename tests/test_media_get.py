import requests


def test_get_media_by_id_admin(base_url, admin_headers):
    media_id = 1
    response = requests.get(f"{base_url}/api/media/{media_id}", headers=admin_headers)

    assert response.status_code in (200, 404), (
        f"Unexpected status {response.status_code}: {response.text}"
    )


def test_get_media_by_id_user(base_url, user_headers):
    media_id = 1
    response = requests.get(f"{base_url}/api/media/{media_id}", headers=user_headers)

    assert response.status_code in (200, 404, 403), (
        f"Unexpected status {response.status_code}: {response.text}"
    )
