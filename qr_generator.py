import qrcode
from PIL import Image 
import os

class QRGenerator():
    
    def generate_qrcode(
            self, 
            data:str,
            file_path: str= "./",
            output:str = "qrcode",
            version:int = 1, 
            box_size:int = 10, 
            border:int = 2, 
            color:str = "black"):
        
        try:
            qr = qrcode.QRCode(
                version= version, 
                error_correction = qrcode.constants.ERROR_CORRECT_H, 
                box_size = box_size, 
                border= border
            )
            qr.add_data(data)
            qr.make(fit=True)

            img = qr.make_image(fill_color=color, back_color="white").convert("RGBA")

            watermark = Image.open('icon.png')
            watermark_size = (img.size[0] //4, img.size[1]//4)
            watermark = watermark.resize(watermark_size, Image.LANCZOS)
            
            pos = ((img.size[0]- watermark.size[0])//2, (img.size[1] - watermark.size[1])//2)
            img.paste(watermark, pos, mask=watermark.split()[3])
            
            img.save(os.path.join(file_path, (output+".png")))

            return img
        except Exception as e:
            print(f"Error generating QR code: {e}")
            return None
