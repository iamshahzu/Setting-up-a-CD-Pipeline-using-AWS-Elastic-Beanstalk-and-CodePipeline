from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from .routers import items
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI(title="FastAPI on AWS Elastic Beanstalk")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPLICATION_DIR = os.path.join(BASE_DIR, "application")

# Set up templates and static files
templates = Jinja2Templates(
    directory=os.path.join(APPLICATION_DIR, "templates"))
app.mount("/static", StaticFiles(directory=os.path.join(APPLICATION_DIR,
          "static")), name="static")


app.include_router(items.router)


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/health")
async def health_check():
    return {"status": "healthy"}