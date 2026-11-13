from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from typing import Annotated
import io
import base64
from qrcode.exceptions import DataOverflowError
from api.app.service.qr_service import generate_qr


templates = Jinja2Templates(directory='templates')
router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name='index.html',
        context={"colors": ["black", "white", "red", "blue", "green", "orange", "yellow", "Purple"],
                 "fg_color":"black", 
                 "bg_color":"white"}
    )


@router.post("/generate-qr", response_class=HTMLResponse)
async def generate_qr(
request: Request, 
data:Annotated[str, Form()],
fg_color:Annotated[str, Form()], 
bg_color:Annotated[str, Form()]):
    error_message = None
    img_str = None
    try:
        buffer = generate_qr(data, fg_color, bg_color)
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

@router.post("/download-qr")
async def download_qr(
data:Annotated[str, Form()],
fg_color:Annotated[str, Form()], 
bg_color:Annotated[str, Form()]):
    try:
        
        buffer = generate_qr(data, fg_color, bg_color)
        
        return StreamingResponse(
        buffer,  
        media_type="image/png",
        headers={
            "Content-Disposition": 'attachment; filename="qr.png"'
            }
        )
    except ValueError as val_ex:
        raise HTTPException(
        status_code=422,
        detail=str(val_ex)
    )
    except DataOverflowError as data_er:
        raise HTTPException(
        status_code=422,
        detail=str(data_er)
    )

