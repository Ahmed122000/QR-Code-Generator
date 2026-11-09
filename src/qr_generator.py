import qrcode
from PIL import Image 

import traceback
from typing import Optional

from pathlib import Path
from typing import Union


class QRGenerator():
    """QR Code generator with optional watermark support"""
    
    SUPPORTED_FORMATS = {'png': 'png',
                        'jpg' : 'jpeg',
                        'jpeg' : 'jpeg'}

    @staticmethod
    def generate_qrcode( 
            data:str,
            color:str = "black",
            background_color:str = "white",
            box_size:int = 10, 
            border:int = 4,
            icon_path:Union[str, Path, None]=None, 
        ) -> Image.Image:
        
        """
        Generate a QR code and return it as a PIL Image.

        Args:
            data: Text or URL to encode.
            color: QR code foreground color.
            background_color: QR code background color.
            box_size: Size of each QR module in pixels.
            border: Width of the QR border in modules.
            icon_path: Optional path to a center icon.

        Returns:
            Generated QR code as a PIL Image.

        Raises:
            ValueError: If the input or configuration is invalid.
            FileNotFoundError: If the requested icon does not exist.
            qrcode.exceptions.DataOverflowError: If the data
                exceeds the QR code's capacity.
        """

        if not isinstance(data, str) or not data.strip():
            raise ValueError("QR code data connot be empty")
        
        if box_size <= 0: 
            raise ValueError("box_size must be greater than zero.")
        
        if border <0:
            raise ValueError("border cannot be negative.")
        
        qr = qrcode.QRCode(
                version= None, 
                error_correction = qrcode.constants.ERROR_CORRECT_H, 
                box_size = box_size, 
                border= border
            )
            
        qr.add_data(data)
        qr.make(fit=True)

        #create image
        image = qr.make_image(
            fill_color=color, 
            back_color=background_color
        ).convert("RGBA")
            
        #add icon if requested
        if icon_path is not None:
            icon_path = Path(icon_path)

            if not icon_path.is_file():
                    raise FileNotFoundError(f"Icon file not found: {icon_path}")

            with Image.open(icon_path) as icon_file:
                    icon = icon_file.convert("RGBA")
            
            icon_size = (
                image.width //4, 
                image.height//4
            )
            icon = icon.resize(
                icon_size, 
                Image.LANCZOS
            )
            
            #center the watermark            
            position = (
                (image.width - icon.width)//2, 
                (image.height- icon.height)//2
            )
                    
            #paste using watermakr as mask (supports alpha)
            image.paste(
                icon, 
                position, 
                mask=icon.getchannel("A")
            )

        return image
        

    @staticmethod
    def save_qrcode(
         image: Image.Image, 
         output: str = 'qrcode', 
         output_path: Union[str, Path] = "assets/output", 
         img_format:str = "png"
    ) -> Path: 
         
        """
        Save a generated QR code to disk.

        Returns:
            Path to the saved image.
        """

        img_format = img_format.lower()

        if img_format not in QRGenerator.SUPPORTED_FORMATS.keys(): 
            raise ValueError(
                f"Unsupported format: {img_format}"
            )
        
        if not output.strip():
            raise ValueError("Output filename cannot be empty.")

        output_directory = Path(output_path)
        output_directory.mkdir(parents=True, exist_ok=True)

        output_file = output_directory / f"{output}.{img_format}"

        image_to_save = (
             image.convert("RGB") if img_format in {"jpg", "jpeg"}
             else image
        )

        image_to_save.save(
            output_file, 
            format=QRGenerator.SUPPORTED_FORMATS[img_format].upper()
        )

        return output_file