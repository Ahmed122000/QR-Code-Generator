import qrcode
from PIL import Image 
import os
import traceback
from typing import Optional

class QRGenerator():
    """QR Code generator with optional watermark support"""
    @staticmethod
    def generate_qrcode( 
            data:str,
            output:str = "qrcode", 
            output_path:str = "assets/output",
            box_size:int = 10, 
            border:int = 2, 
            color:str = "black", 
            icon_path:Optional[str]=None, 
            img_format: str = 'png',
            download_api: bool = False
        ) -> Optional[Image.Image]:
        
        """
        Generate a QR code with optional icon watermark.
        
        Args:
            data: Text or URL to encode
            output: Output filename without extension
            output_path: Output directory path
            box_size: Size of each QR box in pixels
            border: Border width in boxes
            color: QR code color
            icon_path: Path to icon image
            img_format: Output format (png, jpg, jpeg)
        
        Returns:
            PIL Image object or None if failed
        """
        try:
            qr = qrcode.QRCode(
                version= None, 
                error_correction = qrcode.constants.ERROR_CORRECT_H, 
                box_size = box_size, 
                border= border
            )
            
            qr.add_data(data)
            qr.make(fit=True)

            #create image
            img = qr.make_image(fill_color=color, back_color="white").convert("RGBA")
            

            #add icon if requested
            if icon_path:
                try: 
                    watermark = Image.open(icon_path).convert("RGBA")
                    watermark_size = (img.size[0] //4, img.size[1]//4)
                    watermark = watermark.resize(watermark_size, Image.LANCZOS)

                    #center the watermark            
                    pos = ((img.size[0]- watermark.size[0])//2, (img.size[1] - watermark.size[1])//2)
                    
                    #paste using watermakr as mask (supports alpha)
                    img.paste(watermark, pos, mask=watermark.split()[3])

                except FileNotFoundError:
                    print("Warning: Icon file not found, proceeding without icon")
                except Exception as e: 
                    print(f"Warning: Could not add icon: {e}")  
            
            if not download_api: 
                img.save(os.path.join(output_path, f'{output}.{img_format}'), img_format.upper())
            
            return img
        
        except qrcode.exceptions.DataOverflowError:
            print("Error: Data too large for this QR version")
            print("Try reducing the input size")
            return None
        
        except PermissionError:
            print(f"Error: Permission denied when saving to '{output_path}'")
            return None
        
        except Exception as e:
            print(f"Unexpected error: {e}")
            traceback.print_exc()
            return None
