from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import items

app = FastAPI(title="FastAPI on AWS Elastic Beanstalk")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(items.router)

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI on AWS Elastic Beanstalk!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}