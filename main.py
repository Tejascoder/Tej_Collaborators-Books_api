# ====    This is going to become a BOOk Store ! ========
from fastapi import FastAPI
from .routes import router as bookdisplay

if __name__ == "__main__":
    app = FastAPI()
    app.include_router(bookdisplay)