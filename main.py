import logging
from fastapi import FastAPI

from api import alive, pdf2md

app = FastAPI()


# turn off log-spamming for each "get alive"
logging.basicConfig(level=logging.INFO)
uvicorn_access_logger = logging.getLogger("uvicorn.access")


class ExcludeHealthCheckFilter(logging.Filter):
    def filter(self, record):
        # Exclude the /alive endpoint from logs
        return "/pdf2md/api/common/alive/" not in record.getMessage()


app.include_router(alive.router)
app.include_router(pdf2md.router)

