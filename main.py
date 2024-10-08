from fastapi import FastAPI

from api import alive, pdf2md

app = FastAPI()

app.include_router(alive.router)
app.include_router(pdf2md.router)

