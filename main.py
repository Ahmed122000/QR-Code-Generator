from qr_generator import QRGenerator

if __name__ == "__main__":
    qr_generator = QRGenerator()

    img  = qr_generator.generate_qrcode("I love you")

    if img: 
        print("QR code generated successfully!")