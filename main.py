from qr_generator import QRGenerator
import argparse
from urllib.parse import urlparse
import os 
import sys

def validate_url(url:str) -> bool:
    """validate URL format"""
    parsed = urlparse(url)
    return bool(parsed.scheme and parsed.netloc)


def main():
        
    parser = argparse.ArgumentParser( 
        description="Generate QR codes with custom colors and watermark",
        epilog="Example: python main.py --url https://example.com --color blue"
    )
    
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("--url",                       help="URL to encode in QR")
    input_group.add_argument("--txt",                       help="Text to encode in QR")
    
    parser.add_argument("--color",      default='black',    help="QR code color (default: black)",      choices=['red', 'blue', 'green', 'orange', 'purple', 'yellow', 'black'])
    parser.add_argument("--output",     default="qrcode",   help="Output filename without extension")
    parser.add_argument("--icon",                           help = "Path to the icon to set in the center of the qr code")
    parser.add_argument("--path",       default="./assets/output", help="Output directory path")
    parser.add_argument("--format",     default='png',      help="Output image format (default: png)",  choices=['png', 'jpg', 'jpeg'])
    
    args = parser.parse_args()
    
   
    data = args.url or args.txt

    #validate data
    if not data or not data.strip(): 
        print("Error: Input data cannot be empty!")
        sys.exit(1)
    
    #validate URL if provided
    if(args.url and not validate_url(args.url)):
        print("Error: Invalid URL format!")
        print("Example: https://example.com")
        sys.exit(1)        

    #create output directory if needed    
    if args.path != './':
        try: 
            os.makedirs(args.path, exist_ok=True)
        except PermissionError: 
            print(f"Error: Cannot create directory `{args.path}`")
            sys.exit(1)
    
    
    
    img  = QRGenerator.generate_qrcode(
        data, 
        color=args.color, 
        icon_path=args.icon, 
        output=args.output, 
        output_path=args.path, 
        img_format=args.format
    )

    if img: 
        full_path = os.path.join(args.path, f"{args.output}.{args.format}")
        print("QR code generated successfully!")
        print(f'QR code saved to: {full_path}')
        sys.exit(0)
    else: 
        print("Failed to generate QR Code")
        sys.exit(1)

    
if __name__ == "__main__":
    main()