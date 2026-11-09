from PIL import Image
from src.qr_generator import QRGenerator
import pytest

def test_generate_qrcode_returns_image():
    data = "Hello, pytest!"

    image = QRGenerator.generate_qrcode(data)

    assert isinstance(image, Image.Image)


def test_generate_qrcode_with_empty_data():
    with pytest.raises(ValueError):
        QRGenerator.generate_qrcode("")


def test_generate_qrcode_with_whitespace_only():
    with pytest.raises(ValueError):
        QRGenerator.generate_qrcode("   ")


def test_generate_qrcode_with_valid_data():
    image = QRGenerator.generate_qrcode("Hello")
    assert isinstance(image, Image.Image)

def test_generate_qrcode_with_invalid_box_size():
    with pytest.raises(ValueError):
        QRGenerator.generate_qrcode("Hello", box_size=0)


def test_generate_qrcode_with_negative_border():
    with pytest.raises(ValueError):
        QRGenerator.generate_qrcode("Hello", border=-1)


def test_generate_qrcode_with_icon(tmp_path):
    icon_path = tmp_path / "test_icon.png"

    icon = Image.new("RGBA", (100, 100), "red")
    icon.save(icon_path)

    image = QRGenerator.generate_qrcode(
        "Hello, pytest!",
        icon_path=icon_path,
    )

    assert isinstance(image, Image.Image)