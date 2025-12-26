import requests
from media_api_tests.settings import BASE_URL
from pathlib import Path


TEST_IMAGE = Path("tests/resources/test_image.png")


def test_upload_media_admin_success(admin_headers):
    response = requests.post(
        f"{BASE_URL}/api/media/upload",
        headers=admin_headers,
        files={"file": TEST_IMAGE.open("rb")},
        data={
            "entityType": "YARN",
            "entityId": 1,
            "variant": "MAIN",
            "altText": "Тестовое изображение",
            "sortOrder": 1,
        }
    )

    assert response.status_code == 201

    body = response.json()
    assert "id" in body
    assert "url" in body
    assert body["format"] in {"PNG", "JPG", "WEBP", "GIF"}
    assert body["widthPx"] > 0
    assert body["heightPx"] > 0
    assert body["sizeBytes"] > 0


def test_upload_media_nonexistent_entity(admin_headers):
    response = requests.post(
        f"{BASE_URL}/api/media/upload",
        headers=admin_headers,
        files={"file": TEST_IMAGE.open("rb")},
        data={
            "entityType": "YARN",
            "entityId": 999999,
        }
    )

    assert response.status_code in (400, 404)


def test_upload_same_file_twice(admin_headers):
    response_1 = requests.post(
        f"{BASE_URL}/api/media/upload",
        headers=admin_headers,
        files={"file": TEST_IMAGE.open("rb")},
        data={"entityType": "YARN", "entityId": 1}
    )

    response_2 = requests.post(
        f"{BASE_URL}/api/media/upload",
        headers=admin_headers,
        files={"file": TEST_IMAGE.open("rb")},
        data={"entityType": "YARN", "entityId": 1}
    )

    assert response_1.status_code == 201
    assert response_2.status_code == 201
    assert response_1.json()["id"] != response_2.json()["id"]


def test_upload_media_without_optional_fields(admin_headers):
    response = requests.post(
        f"{BASE_URL}/api/media/upload",
        headers=admin_headers,
        files={"file": TEST_IMAGE.open("rb")},
        data={
            "entityType": "YARN",
            "entityId": 1,
        }
    )

    assert response.status_code == 201


def test_upload_media_when_primary_exists(admin_headers):
    response = requests.post(
        f"{BASE_URL}/api/media/upload",
        headers=admin_headers,
        files={"file": TEST_IMAGE.open("rb")},
        data={
            "entityType": "YARN",
            "entityId": 1,
            "variant": "MAIN",
        }
    )

    assert response.status_code == 201


