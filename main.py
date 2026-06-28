from qr_generator import QRGenerator

if __name__ == "__main__":
    qr_generator = QRGenerator()

    data = input("enter text/URL to get QR Code: ")
    img  = qr_generator.generate_qrcode(data)

    if img: 
        print("QR code generated successfully!")