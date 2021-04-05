from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI

from _3Words.Controllers import userController , wordsController


app = FastAPI()
app.include_router(userController.router)
app.include_router(wordsController.router)

if __name__ == "__main__":
    uvicorn.run(app , host="127.0.0.1", port=8000)