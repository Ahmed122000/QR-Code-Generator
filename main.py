from qr_generator import QRGenerator
import argparse
from urllib.parse import urlparse

if __name__ == "__main__":
    qr_generator = QRGenerator()
    parser = argparse.ArgumentParser()
    parser.add_argument("--url")
    parser.add_argument("--txt")
    parser.add_argument("--color", type=str, default='black')
    parser.add_argument("--output", type=str, default="qrcode")
    args = parser.parse_args()
    
    if(not args.url and not args.txt):
        print("there is no input!! \n exit")
        exit()

    if(args.url and args.txt):
        print("Can't take both, only url or txt\n exit")
        exit()

    data = None
    if(args.url):
        parsed = urlparse(args.url)
        if parsed.scheme and parsed.netloc:
            data = args.url
        else:
            print("Invalid Url!\n exit")
            exit()        

    if(args.txt):
        data = args.txt

    img  = qr_generator.generate_qrcode(data, color=args.color)

    if img: 
        print("QR code generated successfully!")