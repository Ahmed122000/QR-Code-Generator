from fastapi.testclient import TestClient
from app.main import app
import io
from PIL import Image
client = TestClient(app)


def test_homepage_returns_successful_response():
    response = client.get("/")
    
    assert response.status_code == 200
    assert "</html>" in response.text
    assert "SAH QR-Code Generator" in response.text


def test_generate_qr_successfu_response():
    response = client.post(
        "/generate-qr", 
        data={
        "data": "https://example.com",
        "fg_color": "black",
        "bg_color": "white"
    })

    assert response.status_code == 200
    assert "SAH QR-Code Generator" in response.text 
    assert "data:image/png;base64," in response.text


def test_generate_qr_rejects_empty_data():
    response = client.post(
        "/generate-qr", 
        data={
        "data":"  ",
        "fg_color": "black",
        "bg_color": "white"
    })

    assert response.status_code == 200
    assert "Please enter valid Non-empty text/URL" in response.text 
    assert "data:image/png;base64," not in response.text


def test_download_qr_successfully():
    response = client.post(
        "/download-qr", 
        data={
        "data":"https://example.com",
        "fg_color": "black",
        "bg_color": "white"
    })

    image = Image.open(io.BytesIO(response.content))

    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'image/png'
    assert "attachment" in response.headers['Content-Disposition']
    assert image.format == "PNG"
    assert image.width > 0
    assert image.height >0


def test_download_qr_rejects_empty_data():
    response = client.post(
        "/download-qr", 
        data={
        "data":"  ",
        "fg_color": "black",
        "bg_color": "white"
    })

    assert response.status_code == 422
    assert 'QR code data cannot be empty' in response.json()['detail']
    