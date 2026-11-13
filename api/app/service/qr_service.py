import io
from qr_generator import QRGenerator

def generate_qr(data, bg_color, fg_color):
    qr = QRGenerator.generate_qrcode(
                data = data,
                background_color=bg_color, 
                color=fg_color
            )
    
    buffer = io.BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)

    return buffer