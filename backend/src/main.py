from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from api.routes.chats import router as chat_router
import logging
from dotenv import load_dotenv
import os
from configs.config import config

load_dotenv()

app = FastAPI()

print("MENU_BACKEND_URL", config.MENU_BACKEND_URL)

origins = [
    "*",
    "http://localhost:3000",
]

# Basic logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router, prefix='/api/chats',
                   tags=['workflows'])


@app.get("/")
def read_root():
    return {"status": "Okay", "message": "Server is Running."}


def main():
    print("Hello from chatbot server!")
    uvicorn.run(app, host="0.0.0.0", port=config.PORT)


if __name__ == "__main__":
    main()
