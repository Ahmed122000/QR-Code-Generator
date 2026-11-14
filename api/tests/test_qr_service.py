import io
from PIL import Image
from app.service.qr_service import generate_qr
import pytest
from qrcode.exceptions import DataOverflowError


def test_generate_qr_returns_valid_png():
    data = "https://exmaple.com" 
    bg_color = "white"
    fg_color = "black"
    buffer = generate_qr(
        data, 
        bg_color=bg_color, 
        fg_color=fg_color)

    assert isinstance(buffer,io.BytesIO)

    img = buffer.getvalue()
    assert isinstance(img, bytes)
    assert len(img) > 0

    image = Image.open(buffer)
    assert image.format == "PNG"
    assert image.width > 0
    assert image.height > 0

def test_generate_qr_rejects_empty_data():
    with pytest.raises(ValueError): 
        generate_qr(
            "", 
            bg_color="white", 
            fg_color="black"
        )

def test_generate_qr_code_rejects_too_large_data():
    data = "A"*100000
    with pytest.raises(ValueError):
        generate_qr(
            data, 
            bg_color="white",
            fg_color="black"
        )