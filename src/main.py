import sys
import argparse
from urllib.parse import urlparse

from qrcode.exceptions import DataOverflowError
from PIL import UnidentifiedImageError

from src.qr_generator import QRGenerator


def validate_url(url:str) -> bool:
    """validate URL format"""
    parsed = urlparse(url)
    return bool(parsed.scheme and parsed.netloc)


def main() -> int:
        
    parser = argparse.ArgumentParser( 
        description="Generate QR codes with custom colors and an optional center icon.",
        epilog="Example: qr --url https://example.com --color blue"
    )
    
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("--url",       help="URL to encode in QR")
    input_group.add_argument("--txt",       help="Text to encode in QR")
    
    parser.add_argument(
        "--color",      
        default='black',
        choices=['white', 'red', 'blue', 'green', 'orange', 'purple', 'yellow', 'black'],
        help="QR code color (default: black)"
    )
                      
    parser.add_argument(
        "--bg-color",   
        default='white',            
        choices=['white', 'red', 'blue', 'green', 'orange', 'purple', 'yellow', 'black'],
        help="QR code background color (default: white)"
    )
    
    parser.add_argument(
        "--icon",                                   
        help = "Path to the icon to set in the center of the qr code"
    )
    
    parser.add_argument(
        "--output",     
        default='qrcode',           
        help="Output filename without extension"
    )

    parser.add_argument(
        "--path",       
        default='assets/output',    
        help="Output directory path"
    )
    
    parser.add_argument(
        "--format",     
        default='png',              
        choices=['png', 'jpg', 'jpeg'],
        help="Output image format (default: png)"  
        )
    
    
    args = parser.parse_args()
    data = args.url or args.txt

    #validate data
    if not data or not data.strip(): 
        print("Error: Input data cannot be empty!")
        return 1
    
    #validate URL if provided
    if(args.url and not validate_url(args.url)):
        print("Error: Invalid URL format!")
        print("Example: https://example.com")
        return 1        

    try: 
        image = QRGenerator.generate_qrcode(
            data, 
            color=args.color, 
            background_color=args.bg_color,
            icon_path=args.icon, 
        )
    except FileNotFoundError as error:
        print(f"Error: File not found: {error}")
        return 1
    except UnidentifiedImageError as error:
        print(f"Error: The icon file is not a supported image: {error}")
        return 1
    except DataOverflowError as error:
        print(f"Error: The input is too large to encode in a QR code: {error}")
        return 1
    except ValueError as error:
        print(f"Error: Invalid QR code configuration: {error}")
        return 1
    
    try:      
        saved_file_path = QRGenerator.save_qrcode(
            image, 
            output = args.output, 
            output_path= args.path, 
            img_format=args.format
        )

    except PermissionError as error:
        print("Error: Permission denied while saving the QR code.")
        print(error)
        return 1
    except ValueError as error:
        print(f"Error: Invalid output configuration: {error}")
        return 1
    except OSError as error:
        print(f"Error: Could not save the QR code: {error}")
        return 1

    print("QR code generated successfully!")
    print(f"Saved to: {saved_file_path}")

    return 0

if __name__ == "__main__":
    sys.exit(main())