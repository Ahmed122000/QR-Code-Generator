from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Annotated
from src.qr_generator import QRGenerator
import io
import base64
from qrcode.exceptions import DataOverflowError
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='templates')

'''
the API should take the input text from the user
then return the qr code code is downlaodable image if the user ever wanted to downlaod it
the system doesn't need any login or registeration, it works on fly
'''



@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name='index.html',
        context={"colors": ["black", "white", "red", "blue", "green", "orange", "yellow", "Purple"],
                 "fg_color":"black", 
                 "bg_color":"white"}
    )

@app.post("/generate-qr", response_class=HTMLResponse)
async def generate_qr(
request: Request, 
data:Annotated[str, Form()],
fg_color:Annotated[str, Form()], 
bg_color:Annotated[str, Form()]):
    error_message = None
    img_str = None
    try:
        qr = QRGenerator.generate_qrcode(
            data = data,
            background_color=bg_color, 
            color=fg_color
        )

        buffer = io.BytesIO()
        qr.save(buffer, format="PNG")
        buffer.seek(0)
        img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
        
    except ValueError:
        error_message = "Please enter valid Non-empty text/URL"
    except DataOverflowError:
        error_message = "The enter data is larger than being encoded into qrcode"


    return templates.TemplateResponse(
            request = request,
            name = 'index.html', 
            context={ "image_data": img_str,
                      "error_message": error_message,
                      "colors":["black", "white", "red", "blue", "green", "orange", "yellow", "Purple"],
                      "data":data, 
                      "bg_color":bg_color, "fg_color":fg_color}
            
        )
    

