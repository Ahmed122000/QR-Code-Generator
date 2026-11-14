import io
from qr_generator import QRGenerator
from app.exceptions import InvalidColorError
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parents[2]

AVAILABLE_COLORS = ["black", "white", "red", "blue", "green", "orange", "yellow", "purple"]

def generate_qr(
    data: str,
    bg_color: str,
    fg_color: str
) -> io.BytesIO:

    if not bg_color or not bg_color.strip():
        raise InvalidColorError("Background color must be provided.")
    if not fg_color or not fg_color.strip():
        raise InvalidColorError("QR code color must be provided.")
    
    normalized_bg = bg_color.strip().lower()
    normalized_fg = fg_color.strip().lower()

    if normalized_bg not in AVAILABLE_COLORS: 
        raise InvalidColorError("your background color is not supported")
    if normalized_fg not in AVAILABLE_COLORS:
        raise InvalidColorError("your qr code color is not supported")
    
    qr = QRGenerator.generate_qrcode(
                data = data,
                background_color=normalized_bg, 
                color=normalized_fg,
                icon_path= BASE_DIR / "assets" / "logo" / "icon_bw.png"
            )
    
    buffer = io.BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)

    return buffer