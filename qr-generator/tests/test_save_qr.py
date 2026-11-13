from PIL import Image
from qr_generator import QRGenerator
import pytest


def test_save_qrcode_creates_file(tmp_path):
    image = QRGenerator.generate_qrcode("Hello, pytest!")

    saved_path = QRGenerator.save_qrcode(
        image,
        output="test_qr",
        output_path=tmp_path,
        img_format="png",
    )

    assert saved_path.exists()
    assert saved_path.suffix == ".png"

    with Image.open(saved_path) as saved_image:
        assert saved_image.format == "PNG"
        assert saved_image.mode == "RGBA"


def test_save_qrcode_as_jpeg(tmp_path):
    image = QRGenerator.generate_qrcode("Hello, pytest!")

    saved_path = QRGenerator.save_qrcode(
        image,
        output="test_qr",
        output_path=tmp_path,
        img_format="jpg",
    )

    assert saved_path.exists()
    assert saved_path.suffix == ".jpg"

    saved_image = Image.open(saved_path)
    assert saved_image.format == "JPEG"
    assert saved_image.mode == "RGB"

def test_save_qrcode_with_unsupported_format(tmp_path):
    image = QRGenerator.generate_qrcode("Hello")

    with pytest.raises(ValueError):
        QRGenerator.save_qrcode(
            image,
            output="test",
            output_path=tmp_path,
            img_format="gif",
        )
        
def test_save_qrcode_with_empty_output_name(tmp_path):
    image = QRGenerator.generate_qrcode("Hello")

    with pytest.raises(ValueError):
        QRGenerator.save_qrcode(
            image,
            output="",
            output_path=tmp_path,
            img_format="png",
        )

def test_save_qrcode_with_invalid_image(tmp_path):
    with pytest.raises(TypeError):
        QRGenerator.save_qrcode(
            image="not an image",
            output_path=tmp_path,
        )

def test_save_qrcode_with_whitespace_output_name(tmp_path):
    image = QRGenerator.generate_qrcode("Hello")

    with pytest.raises(ValueError):
        QRGenerator.save_qrcode(
            image,
            output="   ",
            output_path=tmp_path,
        )