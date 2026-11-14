from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import pages
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="SAH QR Code Generator",
    description="Generate and download customized QR codes.",
    version="1.0.0"
)
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
app.include_router(pages.router)
