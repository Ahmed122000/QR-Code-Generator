from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api.app.routers import pages


app = FastAPI(title="SAH QR Code Generator"              )
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(pages.router)








    